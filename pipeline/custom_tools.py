import os
import json
import pandas as pd
import random
from datasets import load_dataset, DatasetDict, Dataset,get_dataset_config_names,get_dataset_split_names
from typing import Optional, List, Callable
# from smolagents import tool
# from litellm import completion
import ast
import re
import difflib
from langchain_openai import ChatOpenAI
from models import ChatModel
judge = ChatModel.create_model(
"gemini-2.0-flash",

)

# -------------------------------------------
# Agent-safe decorator
# -------------------------------------------
# def tool_safe(func: Callable) -> Callable:
#     """
#     Smolagent tool decorator with auto docstring generator.
#     """
#     # 원본 function 가져오기
#     raw_func = func
#     if hasattr(func, "__wrapped__"):
#         raw_func = func.__wrapped__

#     if not getattr(raw_func, "__doc__", None):
#         auto_doc = generate_google_style_docstring(raw_func)
#         print(f"[tool_safe] Auto-generating docstring for '{raw_func.__name__}':\n{auto_doc}\n")
#         raw_func = set_docstring(raw_func, auto_doc)

#     return tool(raw_func)

# -------------------------------------------
# Utility - Load JSONL
# -------------------------------------------

# @tool_safe
def load_dataset_tool(path: str) -> dict:
    """
    Load dataset from JSONL file.

    Args:
        path (str): Path to JSONL file.

    Returns:
        dict: Loaded dataset records.
    """
    with open(path, "r", encoding="utf-8") as f:
        records = [json.loads(line) for line in f]

    return {
        "total_records": len(records),
        "sample_records": records[:5]  # agent-safe sample only
    }

# -------------------------------------------
# Step 1 - Download dataset
# -------------------------------------------
# ------------------------------
# Tool 0: Check if dataset has subsets
# ------------------------------
# @tool_safe
def check_hf_dataset_subset(dataset_key: str) -> dict:
    """
    Check whether the Hugging Face dataset has subsets (configs).

    Args:
        dataset_key (str): The Hugging Face dataset identifier.

    Returns:
        dict: List of available subsets (configs). Empty list means no subsets.
    """
    subsets = get_dataset_config_names(dataset_key)
    return {"subsets": subsets}
# ------------------------------
# Tool 1: Download the dataset
# ------------------------------

# ---------------------------------------------
# Smart analyzer: subset/split 판단
# ---------------------------------------------

def smart_subset_split_analyzer(dataset_key):
    subsets = get_dataset_config_names(dataset_key)
    subset_is_split = False

    if subsets and all(x.lower() in ["train", "test", "dev", "validation"] for x in subsets):
        subset_is_split = True

    tasks = []

    if subset_is_split:
        splits = subsets

        # ✅ split이 train 하나일 때도 train 그대로 유지
        for split in splits:
            tasks.append((None, split))

    elif subsets:
        # subsets + splits 조합인 경우
        for subset in subsets:
            try:
                splits = get_dataset_split_names(dataset_key, subset)
            except:
                splits = ["default"]  # 없으면 train 하나로 간주

            for split in splits:
                tasks.append((subset, split))
    else:
        # subsets 없음 → split만 있는 경우
        try:
            splits = get_dataset_split_names(dataset_key)
        except:
            splits = ["default"]

        for split in splits:
            tasks.append((None, split))


    return tasks

# ---------------------------------------------
# Dataset download + save
# ---------------------------------------------

def dataset_download_tool(dataset_key: str, subset: Optional[str] = None, split: Optional[str] = None) -> dict:
    """
    Download dataset from Hugging Face with subset and split.

    Returns:
        dict: saved_path, total_records, sample_records, subset, split
    """

    available_subsets = get_dataset_config_names(dataset_key)


    if available_subsets:
        if subset is None:
            raise ValueError(f"This dataset requires a subset (config). Available subsets: {available_subsets}")
        
        dataset = load_dataset(dataset_key, subset,download_mode="force_redownload")
    else:
        dataset = load_dataset(dataset_key,download_mode="force_redownload")

    splits = list(dataset.keys()) if isinstance(dataset, DatasetDict) else ["default"]

    if split is None:
        split = "train" if "train" in splits else splits[0]

    data = dataset[split] if split != "default" else dataset

    records = []
    for x in data:
        row = dict(x)
        row["_split"] = split
        row["_splits"] = splits
        records.append(row)

    sample_records = random.sample(records, min(20, len(records)))

    safe_dataset_key = dataset_key.replace("/", "_")
    subset_name = subset or "default"
    split_name = split or "default"
    os.makedirs("data_temp", exist_ok=True)
    save_path = f"data_temp/{safe_dataset_key}/{subset_name}_{split_name}_raw.jsonl"

    with open(save_path, "w", encoding="utf-8") as f:
        for row in records:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    return {
        "saved_path": save_path,
        "total_records": len(records),
        "sample_records": sample_records,
        "subset": subset_name,
        "split": split_name
    }

# -------------------------------------------
# Step 2 - Detect problem type
# -------------------------------------------

# @tool_safe
def detect_problem_type_tool(sample_rows: List[dict]) -> dict:
    """
    Detect problem type based on sample rows.

    Args:
        sample_rows (List[dict]): Sample records from the dataset.

    Returns:
        dict: {
            "problem_type": str (One of: MCQA, binary, alignment, free-form)
        }
    """

    instruction = """
You are a problem type classifier for dataset records.

Given a few sample rows, your task is to classify the overall problem type into one of the following categories:

- MCQA: If there are multiple choice options and one correct answer among them.
- Binary: If the answers are yes/no or true/false.
- Alignment: If the data is about preference, subjective response, or comparison.
- Free-form: If the answer is open-ended and natural language without fixed choices.

Please analyze the sample data carefully and return only the problem type as "MCQA", "binary", "alignment", or "free-form".
Return as JSON like this:
{"problem_type": "MCQA"}

Sample data:
"""


    # Prepare sample rows as JSON
    sample_text = json.dumps(sample_rows, ensure_ascii=False, indent=2)
    txt = instruction + sample_text
    response = judge.invoke(txt)# (model="gpt-4o", messages=[{"role": "system", "content": instruction},{"role": "user", "content": sample_text}, ])
    try:
        # response_raw = response["choices"][0]["message"]["content"].split('```')[1].strip('json')
        # result = json.loads(response_raw)
        response_raw = response.content.split('```')[1].strip('json')
        result = json.loads(response_raw)
    except IndexError:
        if "MCQA" in response.content:#response["choices"][0]["message"]["content"]:
            result = {"problem_type": "MCQA"}
        elif "binary" in response.content:# response["choices"][0]["message"]["content"]:
            result = {"problem_type": "binary"}
        elif "alignment" in response.content:#response["choices"][0]["message"]["content"]:
            result = {"problem_type": "alignment"}
        elif "free-form" in response.content:#response["choices"][0]["message"]["content"]:
            result = {"problem_type": "free-form"}
        else:
            response = judge.invoke(txt)
            response_raw = response.content.split('```')[1].strip('json')
            result = json.loads(response_raw)
            # response = completion(model="gpt-4o", messages=[{"role": "system", "content": instruction},{"role": "user", "content": sample_text}, ])
            # response_raw = response["choices"][0]["message"]["content"].split('```')[1].strip('json')
            # result = json.loads(response_raw)
    except json.JSONDecodeError:
        if "MCQA" in response.content:#response["choices"][0]["message"]["content"]:
            result = {"problem_type": "MCQA"}
        elif "binary" in response.content:#response["choices"][0]["message"]["content"]:
            result = {"problem_type": "binary"}
        elif "alignment" in response.content:#response["choices"][0]["message"]["content"]:
            result = {"problem_type": "alignment"}
        elif "free-form" in response.content:#response["choices"][0]["message"]["content"]:
            result = {"problem_type": "free-form"}
        else:
            response = judge.invoke(txt)
            response_raw = response.content.split('```')[1].strip('json')
            result = json.loads(response_raw)
            # response = completion(model="gpt-4o", messages=[{"role": "system", "content": instruction},{"role": "user", "content": sample_text}, ])
            # response_raw = response["choices"][0]["message"]["content"].split('```')[1].strip('json')
            # result = json.loads(response_raw)
    except Exception as e:
        print(f"Error parsing response: {e}")
        result = {"problem_type": "unknown"}
    return result


# ------------------------------
# Step 3 : Map dataset row
# ------------------------------

# @tool_safe
def guess_field(row: dict, candidates: list) -> Optional[str]:
    """
    Guess the field based on the candidates.
    Args:
        row (dict): Row to guess.
        candidates (list): List of candidate keys to check.
    Returns:
        str: The guessed field value or None if not found.
    """
    for candidate in candidates:
        for key in row.keys():
            if candidate.lower() in key.lower():
                return key
    return None
# @tool_safe
def extract_mcqa_options(row: dict,raw_key:List, answer_key:str,answers_list:List) -> tuple:
    """
    Extract options from the row.
    Args:
        row (dict): Row to extract options from.
        raw_key (list): List of keys to check for options.
        answer_key (str): Key for the answer.
        answers_list (list): List of possible answers.
    Returns:
        tuple: A tuple containing options, answer, and metadata.
    """
    try:
        answers_list = sorted([ a for a in answers_list])
    except:
        answers_list = None
    
    row =  {key.lower(): value for key, value in row.items()}
    option_keys =  [k for k in row.keys() if k.lower() in ["a", "b", "c", "d","e", "보기", "option","options","choices","choice", "옵션","0", "1", "2", "3", "4", "5", "가", "나", "다", "라", "마"]]
    option_keys = sorted(option_keys)

    if len(option_keys) == 0:
        option_keys = [raw_key]
   
    if len(option_keys) == 1:
        if type(option_keys[0] ) == list:
            option_keys = option_keys[0]
            options = [row[k] for k in option_keys] if option_keys else None
            if options is not None:
                options = [opt for opt in options if opt is not None]
        else:
            options = row[option_keys[0]]
            if isinstance(options, str):
                try:
                    options = ast.literal_eval(options)
                except:
                    if '|' in options:
                        options_raw = options.split("|")
                        options = [x.strip() for x in options_raw]
                    elif ',' in options:
                        options_raw= options.split(",")
                        options = [x.strip() for x in options_raw]
        if isinstance(options, str):
            options = [options]
        if options and isinstance(options, str):
            try:    
                options = ast.literal_eval(options)
            except (ValueError, SyntaxError):
                options = [options]
    else:
        options = [row[k] for k in option_keys] if option_keys else None
        if options is not None:
            options = [opt for opt in options if opt is not None]
    answer_value = row.get(answer_key)
    answer = None

    if options:
        
        if isinstance(answer_value, int):
            if 0 in answers_list:
                index = answer_value
            else:
                index = answer_value - 1
            if 0 <= index < len(options):
                answer = options[index]
        elif isinstance(answer_value, str) and answer_value in option_keys:
            answer = row[answer_value]
        elif isinstance(answer_value, str) and answer_value in options:
            answer = answer_value
        else:
            answer = answer_value

    mcqa_meta = {
        "num_options": len(options) if options else 0,
        "option_keys": option_keys,
        "original_answer": answer_value
    } if options else None
    return options, answer, mcqa_meta


# @tool_safe
def fuzzy_match(candidate: str, choices: List[str], cutoff: float = 0.6) -> Optional[str]:
    """
    Fuzzy match a candidate string against a list of choices.
    Args:
        candidate (str): The candidate string to match.
        choices (list): List of choices to match against.
        cutoff (float): Similarity threshold for matching.
    Returns:
        str: The best match from choices or None if no match found.
    """
    matches = difflib.get_close_matches(candidate, choices, n=1, cutoff=cutoff)
    return matches[0] if matches else None

# @tool_safe
def parse_mapping_from_string(response_raw: str, row_keys :List, valid_mapped_keys:List) -> dict:
    """
    Parse the mapping from the response string.
    Args:
        response_raw (str): The raw response string.
        row_keys (list): List of keys to map.
        valid_mapped_keys (list): List of valid mapped keys.
    Returns:
        dict: Mapped keys and values.
    """
    mapping = {}
    for key in row_keys:
        # 개선된 정규식 → 따옴표 유무 상관 없이 매칭
        pattern = rf"['\"]?{re.escape(key)}['\"]?\s*:\s*['\"]?(\S+)['\"]?"
        match = re.search(pattern, response_raw)
        if match:
            mapped_value_raw = match.group(1).strip('"').strip("'")  # 따옴표 제거
            mapped_value = fuzzy_match(mapped_value_raw, valid_mapped_keys)
            if mapped_value != None:
                if mapped_value in mapping:
                    # 중복된 경우, 기존 값과 비교하여 더 유사한 것을 선택
                    existing_key = mapping[mapped_value]
                    if isinstance(existing_key, str):
                        existing_key = [existing_key]
                        existing_key.append(key)
                        mapping[mapped_value] = existing_key
                    elif isinstance(existing_key, list):
                        existing_key.append(key)
                        mapping[mapped_value] = existing_key
                else:
                    mapping[mapped_value] = key

    return mapping
# @tool_safe    
def agent_smart_map(row: dict, problem_type: str) -> dict:
    """
    Agent-based intelligent key mapping (not value mapping)
    Args:
        row (dict): Row to map.
        problem_type (str): Problem type.
    Returns:
        dict: Mapped row.
    """
    row_keys = list(row.keys())
    row_data = json.dumps(row, ensure_ascii=False, indent=2)
    instruction = f"""
You are a dataset schema mapper.

Your task is to map keys from the following raw dataset row to standardized fields based on the problem_type ({problem_type}).

Standard fields are:

- context (Optional): Background information, passage, paragraph or any supporting text related to the question. If no context exists, set this to None.
- prompt (Required): The main question or query that the user must answer. This is REQUIRED for all problem types.
- options (Conditional): This is REQUIRED if problem_type is MCQA. It should be a list of possible answer choices. If not MCQA, set to None.
- answer (Required): The correct answer to the prompt. For MCQA, should be from options. For binary, should be Yes/No/True/False. For free-form, natural language.
- reference (Optional): Any explanation or justification for the answer. If unavailable, set to None.
- original_category (Optional): The category(subject) info of the dataset row. If unavailable, set to None.

If the key represents a option (MCQA), map it to "options".
If the key represents the question, map to "prompt".
If the key represents the answer, map to "answer".
If the key represents explanation or reference solution, map to "reference".
If the key represents category/subject, map to "original_category".
If the key is not important, map to "ignore".

Raw keys:
{row_keys}

Raw data:
{row_data}

Return as JSON with the mapping like:
{{"question": "prompt", "A": "options", "B": "options", "answer": "answer", "category": "original_category"}}

Ouptput should be a JSON object with the mapping of keys to standardized fields.
"""
    valid_mapped_keys = ["prompt", "answer", "options","original_category", "context", "reference"] 
    response = judge.invoke(instruction)#completion(model="gpt-4o", messages=[{"role": "system", "content": instruction}])
    # try:
    #     response_raw = response["choices"][0]["message"]["content"].split('```')[1].strip('json')
    # except IndexError:
    #     response_raw = response["choices"][0]["message"]["content"]
    try:
        response_raw = response.content.split('```')[1].strip('json')
    except IndexError:
        response_raw = response.content
    try:
        result = parse_mapping_from_string(response_raw, row_keys, valid_mapped_keys)
        # result = json.loads(response_raw)
        # result = {v: k for k, v in result.items()}
    except json.JSONDecodeError:

        result = parse_mapping_from_string(response_raw, row_keys, valid_mapped_keys)

   
    
    return result

# # @tool_safe
# def map_row_tool(row: dict, problem_type: str) -> dict:
#     """
#     Map a raw row to standardized format.
#     Args:
#         row (dict): Row to map.
#         problem_type (str): Problem type.
#     Returns:
#         dict: mapped row
#     """

#     context = row.get("context") or guess_field(row, ["context", "passage", "paragraph"])
#     prompt = row.get("question") or row.get("prompt") or guess_field(row, ["question", "query"])
#     answer = row.get("answer") or guess_field(row, ["answers"])
#     original_category = row.get("category") or guess_field(row, ["subject", "category"])
#     reference = row.get("reference") or guess_field(row, ["reference", "solution", "explanation"])

#     options, mcqa_meta = None, None
#     if problem_type == "MCQA":
#         options, answer, mcqa_meta = extract_mcqa_options(row)

#     mapped = {
#         "context": context,
#         "prompt": prompt,
#         "options": options,
#         "answer": answer,
#         "reference": reference,
#         "original_category": original_category,
#         "split": row.get("_split", "default"),
#         "mcqa_meta": mcqa_meta,
#         "additional_info": {}
#     }

#     # intelligent mapping
#     if not mapped["prompt"] or (problem_type == "MCQA" and not mapped["options"]) or not mapped["answer"]:
#         agent_mapped = agent_smart_map(row=row, problem_type=problem_type)
#         mapped["context"] = mapped["context"] or agent_mapped.get("context")
#         mapped["prompt"] = mapped["prompt"] or agent_mapped.get("prompt")
#         mapped["options"] = mapped["options"] or agent_mapped.get("options")
#         mapped["answer"] = mapped["answer"] or agent_mapped.get("answer")
#         mapped["reference"] = mapped["reference"] or agent_mapped.get("reference")
#         mapped["original_category"] = mapped["original_category"] or agent_mapped.get("original_category")
#     elif not mapped["context"] or not mapped["original_category"] or not mapped["reference"]:
#         # If context or original_category is missing, use agent mapping
#         agent_mapped = agent_smart_map(row=row, problem_type=problem_type)
#         mapped["context"] = mapped["context"] or agent_mapped.get("context")
#         mapped["original_category"] = mapped["original_category"] or agent_mapped.get("original_category")
#         mapped["reference"] = mapped["reference"] or agent_mapped.get("reference")

#     for k, v in row.items():

#         if k not in 
#             mapped["additional_info"][k] = v

#     return mapped
# @tool_safe
def generate_mapping_schema(row: dict, problem_type: str) -> dict:
    """
    Generate a mapping schema for the given row based on the problem type.
    Args:
        row (dict): Row to map.
        problem_type (str): Problem type.
    Returns:
        dict: Mapping schema.
    """
    mapping_schema = {}

    # Step 1: Guess primary fields
    row =  {key.lower(): value for key, value in row.items()}
    candidates = {
        "context": guess_field(row, ["context", "passage", "paragraph"]),
        "prompt": guess_field(row, ["question", "prompt", "query"]),
        "answer": guess_field(row, ["answer", "answers"]),
        "original_category": guess_field(row, ["category", "subject"]),
        "reference": guess_field(row, ["reference", "explanation", "solution"]),
        "options": guess_field(row, ["options", "choices", "choice"]),
    }


    # if problem_type == "MCQA":
    #     options, _, _ = extract_mcqa_options(row)
    #     candidates["options"] = options
        # candidates["answer"] = answer
        # candidates["mcqa_meta"] = mcqa_meta

    # Step 2: 필수/보조 필드 부족 여부 판단 후 agent_smart_map 호출
    agent_mapping = {}

    if not candidates["prompt"] or (problem_type == "MCQA" and not candidates.get("options")) or not candidates["answer"]:
        agent_mapping = agent_smart_map(row=row, problem_type=problem_type)
    elif not candidates["context"] or not candidates["original_category"] or not candidates["reference"]:
        agent_mapping = agent_smart_map(row=row, problem_type=problem_type)


    # Step 2: 후보 필드에 대한 매핑
    for key, value in candidates.items():
        if candidates[key] is None:
            if key in agent_mapping:
                candidates[key] = agent_mapping[key]

    return candidates

# @tool_safe
def map_row_with_schema(row:dict , mapping_schema:dict, problem_type:str,answers_list:List) -> dict:
    """
    Map a raw row to standardized format using a mapping schema.
    Args:
        row (dict): Row to map.
        mapping_schema (dict): Mapping schema.
        problem_type (str): Problem type.
        answers_list (list): List of possible answers.
    Returns:
        dict: mapped row
    """
    row =  {key.lower(): value for key, value in row.items()}
    mapped = {}
    mapped["mcqa_meta"] = None
    
    for mapped_key, raw_key in mapping_schema.items():

        if raw_key is None:
            mapped[mapped_key] = None
            continue
        if mapped_key == "options":
            
            options, answer, mcqa_meta = extract_mcqa_options(row,raw_key,mapping_schema["answer"],answers_list)
            mapped["options"] = options
            mapped["answer"] = answer
            mapped["mcqa_meta"] = mcqa_meta
        if mapped_key in ["context", "prompt",  "answer", "reference", "original_category","category"]:

            try:
                if type(raw_key) != list:
                    value = row.get(raw_key)
                else:
                    value = [{rk: row.get(rk)} for rk in raw_key]
            except:
                import pdb;pdb.set_trace()
            mapped[mapped_key] = value
   
    mapped["split"] = row.get("_split", "default")
    mapped["additional_info"] = {}

    for k, v in row.items():
        if k not in mapping_schema and k not in ["context", "prompt",  "answer", "reference", "original_category","category", "_split", "_splits", mapping_schema["context"], mapping_schema["prompt"], mapping_schema["options"], mapping_schema["answer"], mapping_schema["reference"], mapping_schema["original_category"]]:
            mapped["additional_info"][k] = v

    return mapped

# -------------------------------------------
# Step 4 - Reformat + Save
# -------------------------------------------

# @tool_safe
def reformat_dataset_tool(saved_path: str, mapping_schema: dict, problem_type: str, dataset_key: str, subset: Optional[str] = None) -> dict:
    """
    Reformat dataset from JSONL and save using mapping schema.

    Args:
        saved_path (str): Path to raw JSONL.
        mapping_schema (dict): Raw key -> mapped key schema.
        problem_type (str): Detected problem type.
        dataset_key (str): Dataset ID.
        subset (Optional[str]): Subset name.

    Returns:
        dict: saved_path and total records.
    """
    with open(saved_path, "r", encoding="utf-8") as f:
        records = [json.loads(line) for line in f]

    reformatted = []
    answer_key = mapping_schema.get("answer",None)
    
    if answer_key != None:
        try:
            answers_list= list(set([i['Answer Key'] for i in records if 'Answer Key' in i]))
        except:
            answers_list = []
    else:
        answers_list = []

    for row in records:
        row =  {key.lower(): value for key, value in row.items()}
        # ✅ map_row_with_schema 사용으로 통일
        mapped = map_row_with_schema(row=row, mapping_schema=mapping_schema, problem_type=problem_type,answers_list=answers_list)

        if problem_type in ["MCQA", "binary"] and not mapped["options"]:
            mapped["options"] = ["Yes", "No"] if problem_type == "binary" else ["Option A", "Option B", "Option C", "Option D"]

        split_in_record = row.get("_split", "default")
        splits_in_record = row.get("_splits", ['default'])

        if len(splits_in_record) == 1 and splits_in_record[0] == "train":
            split_for_mapped = "default"
        else:
            split_for_mapped = split_in_record

        reformatted.append({
            "problem_type": problem_type,
            "context": mapped["context"],
            "prompt": mapped["prompt"],
            "options": mapped["options"],
            "answer": mapped["answer"],
            "reference": mapped["reference"],
            "benchmark_name": dataset_key,
            "mcqa_meta": mapped["mcqa_meta"],
            "original_category": mapped["original_category"] or subset,
            "additional_info": mapped["additional_info"],
            "split": split_for_mapped,
        })

    safe_dataset_key = dataset_key.replace("/", "_")
    save_path = f"data_temp/{safe_dataset_key}_{subset or 'default'}_reformatted.jsonl"

    with open(save_path, "w", encoding="utf-8") as f:
        for row in reformatted:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    return {
        "saved_path": save_path,
        "total_records": len(reformatted)
    }


# -------------------------------------------
# Step 5 - Validate
# -------------------------------------------

# @tool_safe
def validate_dataset_tool(path: str) -> dict:
    """
    Validate reformatted dataset JSONL.

    Args:
        path (str): Path to reformatted dataset.

    Returns:
        dict: number of total_records, number of total issues, and Validation issues.
    """
    with open(path, "r", encoding="utf-8") as f:
        records = [json.loads(line) for line in f]

    issues = []
    
    for idx, row in enumerate(records):
        problem_type = row.get("problem_type")
        prompt = row.get("prompt")
        options = row.get("options")
        answer = row.get("answer")

        if not prompt:
            issues.append(f"Row {idx}: Missing prompt.")
        if answer == None:
            issues.append(f"Row {idx}: Missing answer.")
        if problem_type in ["MCQA", "binary"]:
            if not options:
                issues.append(f"Row {idx}: No options provided.")
            if problem_type == "binary" and options:
                valid_binary = {"Yes", "No", "True", "False"}
                if not all(opt in valid_binary for opt in options):
                    issues.append(f"Row {idx}: Invalid binary options -> {options}")

    return {
        "total_records": len(records),
        "total_issues": len(issues),
        "issues": issues[:5]
    }


# ------------------------------
# Step 6: Save Final dataset
# ------------------------------
# @tool_safe
def save_dataset_tool(reformatted_data: list, save_path: str = "reformatted_dataset.jsonl") -> dict:
    """
    Save the reformatted dataset to JSONL and return summary.

    Args:
        reformatted_data (list): Reformatted dataset records.
        save_path (str): Path to save JSONL file.

    Returns:
        dict: Summary of saved dataset.
    """
    # with open(save_path, "w", encoding="utf-8") as f:
    #     for row in reformatted_data:
    #         f.write(json.dumps(row, ensure_ascii=False) + "\n")
    if not os.path.exists(save_path):
        raise FileNotFoundError(f"{save_path} does not exist. Saving probably failed.")

    summary = {
        "total_samples": len(reformatted_data),
        "problem_types": list(set([r["problem_type"] for r in reformatted_data])),
        "saved_path": save_path
    }

    return summary

