# BenchHub Pipeline

This directory contains the core pipeline for preparing and organizing benchmark datasets for use with **BenchHub**. It includes tools for:

* **Reformatting**: Converting raw benchmark datasets into BenchHub-compatible formats.
* **Categorizing**: Automatically assigning skill, subject, and target tags to datasets using both rule-based and LLM-guided methods.

The pipeline is designed to support both large-scale automation and flexible customization, enabling seamless integration of new datasets into the BenchHub framework.

## Reformatting

* **`pipeline/reformat_agent.py`**
  An end-to-end reformatter built on an agent-driven architecture. It automates the process of reformatting datasets for model training and evaluation in a flexible and scalable way.

* **`pipeline/reformat.py`**
  A rule-based and LLM-guided reformatter tailored for datasets from Hugging Face. It applies preprocessing and formatting rules to prepare Hugging Face datasets for downstream tasks.

## Categorizing

* **`pipeline/categorize.py`**
  Code for categorizing datasets using our fine-tuned model [BenchHub-Cat-7b](https://huggingface.co/BenchHub/BenchHub-Cat-7b), based on Qwen-2.5-7B. The script includes the prompts used during inference.
