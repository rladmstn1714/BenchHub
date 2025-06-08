import os
import json
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

def deterministic_pipeline(dataset_key: str):
    """
    Run deterministic processing pipeline.
    """
    if 'github' in dataset_key:
        safe_dataset_key = dataset_key.split("/")[-1].replace(".jsonl", "")
        dataset_dir = f"data_temp/{safe_dataset_key}"
        reformatted_dir = f"{dataset_dir}/reformatted"
        os.makedirs(dataset_dir, exist_ok=True)
        os.makedirs(reformatted_dir, exist_ok=True)

        tasks = [['default', 'default']]
        print(f"Detected tasks: {tasks}")
        print(f"Dataset directory: {dataset_dir}")
        print(f"Reformatted directory: {reformatted_dir}")
        # /mnt/ssd/eunsu/home/bench-ops/github_temp/NQ-open.efficientqa.test.1.1.jsonl
    else:
        safe_dataset_key = dataset_key.replace("/", "_")
        dataset_dir = f"data_temp/{safe_dataset_key}"
        reformatted_dir = f"{dataset_dir}/reformatted"
    
        os.makedirs(dataset_dir, exist_ok=True)
        os.makedirs(reformatted_dir, exist_ok=True)

        tasks = smart_subset_split_analyzer(dataset_key)
        print(f"Detected tasks: {tasks}")
        print(f"Dataset directory: {dataset_dir}")
        print(f"Reformatted directory: {reformatted_dir}")

    previous_keys = None
    previous_problem_type = None
    previous_mapping_schema = None

    for subset, split in tasks:
        previous_keys = None
        previous_problem_type = None
        previous_mapping_schema = None
        print(f"\nProcessing subset={subset} split={split}")

        # if ("short" in subset) or ("anno" in subset):
        #     print(f"Skipping subset={subset} split={split} as it is a short version.")
        #     continue
        # Step 1: download dataset
        if 'github' in dataset_key:
            jsonl_path = f"/path/to/jsonl/files/{dataset_key}.jsonl"  # 필요에 맞게 경로 수정

            try:
                with open(jsonl_path, 'r', encoding='utf-8') as f:
                    for line in f:
                        try:
                            data = json.loads(line)
                            # 원하는 처리 수행
                            print(data)
                        except json.JSONDecodeError:
                            continue  # 깨진 라인 무시
            except FileNotFoundError:
                print(f"파일을 찾을 수 없습니다: {jsonl_path}")
        else:
            try:
                download_result = dataset_download_tool(dataset_key=dataset_key, subset=subset, split=split)
            except Exception as e:
                print(f"Error downloading dataset: {e}")
                continue
            raw_path = download_result["saved_path"]
            sample_data = download_result["sample_records"]
            sample_keys = set(list(sample_data[0].keys())) if sample_data else []

        # Step 2: detect problem type
        if sample_keys == previous_keys and previous_problem_type is not None:
            problem_type = previous_problem_type
            mapping_schema = previous_mapping_schema
            print(f"Reusing previous problem type: {problem_type}")
        else:
            detected = detect_problem_type_tool(sample_rows=sample_data)
            problem_type = 'MCQA'#detected["problem_type"]
            previous_problem_type = problem_type
            previous_keys = sample_keys

            # 새로 generate mapping schema
            mapping_schema = {'context': 'context', 'prompt': 'question', 'answer': 'answer key', 'original_category': 'subject', 'reference': None, 'options': ['option 1', 'option 2', 'option 3', 'option 4', 'option 5']}#generate_mapping_schema(sample_data[0], problem_type)
            previous_mapping_schema = mapping_schema
      
            print(f"Detected problem type: {problem_type}")
            print(f"Generated mapping schema: {mapping_schema}")
        import pdb;pdb.set_trace()
        # Step 3~5: reformat + validate + move → reformat_dataset_tool 로 통합
        reformat_result = reformat_dataset_tool(
            saved_path=raw_path,
            mapping_schema=mapping_schema,
            problem_type=problem_type,
            dataset_key=dataset_key,
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

    datasets = ["MBZUAI/ArabicMMLU"]
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
    