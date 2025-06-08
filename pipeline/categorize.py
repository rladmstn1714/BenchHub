import os
import json
from tqdm import tqdm
from multiprocessing import Process
import time

from vllm import LLM, SamplingParams

def PromptGenerator_query2rationale_qwen(query):
    prompt = f'''Your task is to generate a detailed description of the given query metadata based on the following three categories:

Subject Type: Explain what the query is about (e.g., the main topic or subject of the question). Consider the query itself, its answer, and its original category to determine the subject accurately.
Task Type: Identify the type of ability or skill required to solve the query (e.g., reasoning, background knowledge, critical thinking, calculation, etc.). Base your analysis on the nature of the query and the reasoning process needed to reach the answer.
Target Type: Determine whether the query pertains to a specific culture, domain, or context, or if it is more general and universally applicable. Use all available metadata (query, answer, category) to make this judgment.

Provide a comprehensive and well-reasoned explanation for each category to clearly describe the nature of the query.

Query Metadata:
{query}

Your Explanation: 
'''
    return prompt

def process_file(input_csv_path, output_jsonl_path):
    MODEL_NAME = "BenchHub/BenchHub-Cat-7b"
    llm = LLM(model=MODEL_NAME)
    sampling_params = SamplingParams(temperature=0.7, top_p=0.9, max_tokens=512, logprobs=1)

    df = pd.read_csv(input_csv_path)
    
    with open(output_jsonl_path, 'w') as outfile:
        for _, row in tqdm(df.iterrows(), total=len(df), desc="Generating rationales"):
            sample = row.to_dict()
            if sample.get('split', '') == 'train':
                continue
            query = str(PromptGenerator_query2rationale_qwen(sample))
            outputs = llm.generate(query, sampling_params)
            generated_text = outputs[0].outputs[0].text.strip()
            sample['generated'] = generated_text
            outfile.write(json.dumps(sample, ensure_ascii=False) + '\n')

    print(f"✅ Finished processing: {input_csv_path}")


if __name__ == "__main__":
    input_csv_path = "/path/to/your/input.csv"
    output_jsonl_path = "/path/to/output/generated_output.jsonl"
    
    process_file(input_csv_path, output_jsonl_path)