from smolagents import CodeAgent, LiteLLMModel
from custom_tools import (
    dataset_download_tool, 
    check_hf_dataset_subset, 
    reformat_dataset_tool, 
    validate_dataset_tool, 
    save_dataset_tool, 
    detect_problem_type_tool, 
    map_row_tool,
    load_dataset_tool 
)
import os
from dotenv import load_dotenv
import openai
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Build Agent
model = LiteLLMModel("gpt-4o")

agent = CodeAgent(
    tools=[
        check_hf_dataset_subset,
        dataset_download_tool,
        detect_problem_type_tool,
        map_row_tool,
        reformat_dataset_tool,
        validate_dataset_tool,
        save_dataset_tool,
        load_dataset_tool  # ✅ 여기에도 추가
    ],
    model=model,
    max_steps=30,
)

# Run Full Pipeline
output = agent.run("""
Download and save the dataset "HAERAE-HUB/KMMLU".
Then open and use the saved file path.
Then detect the problem_type and reformat the dataset.
Then validate the reformatted dataset.
Finally save the reformatted dataset.
""")

print("Pipeline complete.")
print(output)
