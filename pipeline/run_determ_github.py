import os
import json
import pandas as pd
from collections import defaultdict
from custom_tools import (
    dataset_download_tool,
    smart_subset_split_analyzer,
    check_hf_dataset_subset,
    validate_dataset_tool,
    save_dataset_tool,
    detect_problem_type_tool,
    load_dataset_tool,
    generate_mapping_schema,
    map_row_with_schema,
    reformat_dataset_tool
)
import glob

def deterministic_pipeline(dataset_key):
    """
    Run deterministic processing pipeline.
    """

    safe_dataset_key = dataset_key[0].replace(".jsonl", "")
    safe_dataset_key = safe_dataset_key.replace(".json", "")
    dataset_dir = dataset_key[0]
    data_name = dataset_key[1]
    reformatted_dir = f"{safe_dataset_key}/reformatted"
    os.makedirs(safe_dataset_key, exist_ok=True)
    os.makedirs(reformatted_dir, exist_ok=True)

    tasks = [['default', 'default']]
    print(f"Detected tasks: {tasks}")
    print(f"Dataset directory: {dataset_dir}")
    print(f"Reformatted directory: {reformatted_dir}")
        # /mnt/ssd/eunsu/home/bench-ops/github_temp/NQ-open.efficientqa.test.1.1.jsonl
  
    previous_keys = None
    previous_problem_type = None
    previous_mapping_schema = None

    for subset, split in tasks:
        print(f"\nProcessing subset={subset} split={split}")

        # if ("short" in subset) or ("anno" in subset):
        #     print(f"Skipping subset={subset} split={split} as it is a short version.")
        #     continue
        # Step 1: download dataset
        
        jsonl_path = dataset_dir
        try:
            if "jsonl" in jsonl_path:
                # JSONL 파일을 읽어 DataFrame으로 변환
                df = pd.read_json(jsonl_path, lines=True)
            else:
                
                df = pd.read_json(jsonl_path)
        except FileNotFoundError:
            print(f"파일을 찾을 수 없습니다: {jsonl_path}")
        raw_path =  jsonl_path
        sample_data = df.sample(5).to_dict(orient='records')
        sample_keys = set(list(sample_data[0].keys())) if sample_data else []
  
        # Step 2: detect problem type
        if sample_keys == previous_keys and previous_problem_type is not None:
            problem_type = previous_problem_type
            mapping_schema = previous_mapping_schema
            print(f"Reusing previous problem type: {problem_type}")
        else:
            detected = detect_problem_type_tool(sample_rows=sample_data)
            problem_type = detected["problem_type"]
            previous_problem_type = problem_type
            previous_keys = sample_keys

            # 새로 generate mapping schema
            mapping_schema = generate_mapping_schema(sample_data[0], problem_type)#{'context': None, 'prompt': 'question', 'answer': 'annotations', 'original_category': None, 'reference': "en_question", 'options': None}
            
            #
            previous_mapping_schema = mapping_schema
            # mapping_schema=  {'context': None, 'prompt': None, 'answer': None, 'original_category': None, 'reference': None, 'options': None}
            print(f"Detected problem type: {problem_type}")
            print(f"Generated mapping schema: {mapping_schema}")
        import pdb;pdb.set_trace()
        # Step 3~5: reformat + validate + move → reformat_dataset_tool 로 통합
        reformat_result = reformat_dataset_tool(
            saved_path=raw_path,
            mapping_schema=mapping_schema,
            problem_type=problem_type,
            dataset_key=data_name,
            subset=subset
        )
        
        reformatted_path = reformat_result["saved_path"]
        
        # Step 4: validate
        validation = validate_dataset_tool(path=reformatted_path)
        if validation["total_issues"] > 0:
            print(f"Validation failed with {validation['total_issues']} issues")
        else:
            print("Validation passed.")

        # Step 5: move reformatted file to final
        final_save_path = f"{reformatted_dir}/{subset or 'default'}_{split or 'default'}_reformatted.jsonl"
        os.rename(reformatted_path, final_save_path)
        print(f"Saved reformatted file to: {final_save_path}")


    print("\n✅ All subsets and splits processed successfully.")

    # Step 6: clean up raw
    raw_files = glob.glob(f"data_temp/{safe_dataset_key}/*_raw*")
    for file_path in raw_files:
        try:
            os.remove(file_path)
            print(f"Deleted raw file: {file_path}")
        except Exception as e:
            print(f"Failed to delete {file_path}: {e}")

if __name__ == "__main__":
    datasets =["", ""],

    error_log_file = "./data_temp/00_error_log.txt"
    for i in datasets:
        print(f"Processing dataset: {i}")
        try:
            deterministic_pipeline(i)
            print("Dataset processed successfully.")
        except Exception as e:
            print(f"Error processing dataset {i}: {e}")
            error_message = f"Error processing dataset {i}: {e}\n"
            print(error_message)  # 콘솔에도 출력
            # 에러 메시지를 텍스트 파일에 저장
            with open(error_log_file, "a") as file:
                file.write(error_message)
