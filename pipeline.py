import json
import torch
from datasets import load_dataset
import random

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

# 1️⃣ Hugging Face에서 데이터 가져오기
def download_dataset(hf_key: str, split: str = "train"):
    dataset = load_dataset(hf_key, split=split)
    return dataset

# 2️⃣ JSON 리스트 변환
def dataset_to_json(dataset, output_file="data.json"):
    data_list = [dict(sample) for sample in dataset]
    
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data_list, f, ensure_ascii=False, indent=4)

    return output_file

# 3️⃣ 간단한 카테고리화 (랜덤)
def categorize_data_simple(data_list):
    categories = ["A", "B", "C"]
    for sample in data_list:
        sample["category"] = random.choice(categories)
    return data_list

# 4️⃣ 데이터 병합
def merge_to_repo(new_data_file, repo_path="merged_data.json"):
    if os.path.exists(repo_path):
        with open(repo_path, "r", encoding="utf-8") as f:
            existing_data = json.load(f)
    else:
        existing_data = []

    with open(new_data_file, "r", encoding="utf-8") as f:
        new_data = json.load(f)

    merged_data = existing_data + new_data
    
    with open(repo_path, "w", encoding="utf-8") as f:
        json.dump(merged_data, f, ensure_ascii=False, indent=4)

# 5️⃣ 실행
def main():
    HF_KEY = "ag_news"
    dataset = download_dataset(HF_KEY)
    json_file = dataset_to_json(dataset)

    with open(json_file, "r", encoding="utf-8") as f:
        data_list = json.load(f)

    categorized_data = categorize_data_simple(data_list)
    with open("test_data.json", "w", encoding="utf-8") as f:
        json.dump(categorized_data, f, ensure_ascii=False, indent=4)

    merge_to_repo("test_data.json")

if __name__ == "__main__":
    main()
