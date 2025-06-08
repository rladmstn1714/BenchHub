import os
import argparse
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from langchain_openai import AzureChatOpenAI
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_together import ChatTogether
import google.generativeai as genai
from langchain_community.chat_models import ChatClovaX
from langchain.schema import SystemMessage, HumanMessage, AIMessage
# from vllm import LLM, SamplingParams
from vllm import LLM, SamplingParams
import pandas as pd
from dotmap import DotMap

from tokenizers.pre_tokenizers import Whitespace
import sys
sys.path.append('..')

import getpass
import os

OPENAI_API_KEY= os.getenv("OPENAI_API_KEY")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT =     os.getenv("AZURE_OPENAI_ENDPOINT")
GEMINI15_API_KEY = os.getenv("GEMINI15_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)
HF_TOKEN = ""

load_dotenv('./.env')

agents_model = {
    "gemini-1.5-pro": "gemini-1.5-pro",
    "gemini-2.0-flash": "gemini-2.0-flash",
    "gpt-4o": "gpt-4o-2024-08-06",
    "gpt-4-turbo" : "gpt-4-turbo-2024-04-09",
    "gpt-4o-mini": "gpt-4o-mini-2024-07-18",
    "phi-3-mini-4k-instruct": "microsoft/Phi-3-mini-4k-instruct",
    "llama-3.1-70b": "meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo",
    "llama-2-7b-chat-hf" : "meta-llama/Llama-2-7b-chat-hf",
    "hcx-003":"HCX-003",
    "hc-seed-15b" : "naver-hyperclovax/HyperCLOVAX-SEED-Text-Instruct-1.5B",
    "exaone-32b":"LGAI-EXAONE/EXAONE-3.5-32B-Instruct",
    "exaone-8b":"LGAI-EXAONE/EXAONE-3.5-7.8B-Instruct",
    "llama-3.1-8b-chat" : "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
    "mixtral-8x7B-Instruct-v0.1" : "mistralai/Mixtral-8x7B-Instruct-v0.1",
    "mistral-7B-Instruct-v0.1" : "mistralai/Mistral-7B-Instruct-v0.1",
    "deepseek-math-7b-instruct" : "deepseek-ai/deepseek-math-7b-instruct",
    "deepseek-coder-7b-instruct-v1.5" : "deepseek-ai/deepseek-coder-7b-instruct-v1.5",
    "qwen2.5-7b-instruct" : "Qwen/Qwen2.5-7B-Instruct-Turbo",
    "qwen2.5-72b-instruct" : "Qwen/Qwen2.5-72B-Instruct-Turbo",
    "llama-3.1-8b" : "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
    "llama-3.1-70b" : "meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo",
    "gemma-9b" : "google/gemma-2-9b-it",
    "gemma-27b" : "google/gemma-2-27b-it",
    #olmoe-math
    "olmoe" : "allenai/OLMoE-1B-7B-0924",
    "claude-3-5-sonnet" : "anthropic/claude-3-5-sonnet-20241022",
    "qwen3-8b" : "Qwen/Qwen3-8B"

    # add other models as needed
}

api_version = {
    "gpt-4o": "2025-02-01-preview",
    "gpt-4-turbo": "2025-02-01-preview",
    "gpt-4o-mini": "2025-02-01-preview",
}
class Testmodel:
    def invoke(prompt):
        return "test"
from langchain.schema import HumanMessage, AIMessage, SystemMessage

def format_vllm_prompt(messages):
    """
    Converts a list of messages (which could be HumanMessage, AIMessage, or SystemMessage)
    into a formatted string for vLLM processing.
    
    - HumanMessage → "user"
    - SystemMessage → "system"
    - AIMessage → "assistant"
    """
    formatted_prompt = ""

    for msg in messages:
        if isinstance(msg, HumanMessage):
            role = "user"
        elif isinstance(msg, SystemMessage):
            role = "system"
        elif isinstance(msg, AIMessage):
            role = "assistant"
        else:
            raise ValueError(f"Unknown message type: {type(msg)}")


        formatted_prompt += f"{role}: {msg.content}\n"


    return formatted_prompt.strip()  # Remove trailing newline





class HuggModel():
    def __init__(self,name,max_tokens=512):
        self.name = name
        self.model = LLM(self.name)  
        self.max_tokens = max_tokens
    def invoke(self,prompt):
          
        sampling_params = SamplingParams(temperature=0.7, top_p=0.9, max_tokens=self.max_tokens)
        try:
            # formatted_prompt = format_vllm_prompt(prompt)
            outputs = self.model.generate([prompt], sampling_params)
            message = outputs[0].outputs[0].text.strip()
            message = AIMessage(content = message)
        except:
            print("error")
            import pdb;pdb.set_trace()
            message = AIMessage(content = message)
            return message
        return message
class GeminiModel():
    def __init__(self,name,temperature=0.7,max_tokens=512):
        self.name = name
        self.model = genai.GenerativeModel(self.name)
        self.generation_config=genai.types.GenerationConfig(
        temperature=temperature,       # 창의성 조절
        max_output_tokens=max_tokens,  # 최대 토큰
        top_p=0.95,            # nucleus sampling
        top_k=40               # top-k sampling
    )

    def invoke(self,prompt):
        try:

            # formatted_prompt = format_vllm_prompt(prompt)
            outputs = self.model.generate_content(prompt)
            message = outputs.candidates[0].content.parts[0].text
            message = AIMessage(content = message)
        except:
            print("error")
            import pdb;pdb.set_trace()
            message = AIMessage(content = message)
            return message
        return message
class ChatModel:

    def create_model(name,temp=0.7,max_tokens=512):
        model_name = name.lower()
        assert model_name in agents_model.keys(), f"{model_name} is not supported"
        if 'test' in model_name:
            model = Testmodel
        elif "hcx" in model_name:
 
            model = ChatClovaX( model="HCX-003",ncp_clovastudio_api_key = os.getenv("CLOVA_API_KEY"),max_tokens=max_tokens,temperature=temp)
        elif "gpt-4o" in model_name:
            model = ChatOpenAI(
                model=agents_model[model_name],
                temperature=temp,
                max_tokens=max_tokens,
                timeout=None,
                max_retries=2,
                # other params...
            )
        elif "gpt" in model_name:
            model = AzureChatOpenAI(
                azure_deployment=agents_model[model_name],
                api_version=api_version[model_name],
                azure_endpoint=azure_endpoint,
                api_key=AZURE_OPENAI_API_KEY,
                temperature=temp,
                max_tokens=max_tokens,
                timeout=None,
                max_retries=2,
                # other params...
            )
        elif "claude" in model_name:
            model = ChatAnthropic(
                model= model_name,
                temperature=0,
                max_tokens=max_tokens, 
                api_key= ANTHROPIC_API_KEY
            )
        elif "gemini" in model_name:
            if "1.5" in model_name:
                api_key = os.getenv("GEMINI15_API_KEY")
            else:
                api_key = os.getenv("GEMINI15_API_KEY")

            model = GeminiModel(agents_model[model_name],temperature=temp,max_tokens=max_tokens)

        elif "exaone" in model_name:
            model = HuggModel(agents_model[model_name],max_tokens=max_tokens)
        elif "seed" in model_name:
            model = HuggModel(agents_model[model_name],max_tokens=max_tokens)
        elif "qwen3-8b" in model_name:
            model = HuggModel(agents_model[model_name],max_tokens=max_tokens)
        else :

            try:
                model = ChatTogether(together_api_key=os.getenv("TOGETHER_API_KEY"),temperature=temp, model=agents_model[model_name],max_tokens = max_tokens)
            except:
                model = HuggModel(agents_model[model_name],max_tokens=max_tokens)
   

        return model
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, default="")
    args = parser.parse_args()

    llama = ChatModel.create_model('gemini-2.0-flash')
    messag = llama.invoke("Hi")

