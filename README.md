<div align="center">
  <h1>📚 BenchHub: A Unified Benchmark Suite for Holistic and Customizable LLM Evaluation </h1>
  <p>
    <a href="https://arxiv.org/abs/2506.00482">
      <img src="https://img.shields.io/badge/ArXiv-BenchHub-<COLOR>" alt="Paper">
    </a>
    <a href="https://github.com/rladmstn1714/BenchHub">
      <img src="https://img.shields.io/badge/GitHub-Code-blue" alt="GitHub">
    </a>
    <a href="https://huggingface.co/BenchHub">
      <img src="https://img.shields.io/badge/HuggingFace-Dataset&Demo-yellow" alt="Hugging Face">
    </a>
  </p>
</div>


**Official repository for [BenchHub: A Unified Benchmark Suite for Holistic and Customizable LLM Evaluation](https://arxiv.org/abs/2506.00482).**




## 📌 Overview

**BenchHub** is a unified benchmark suite designed to help researchers and developers **easily load, filter, and process various LLM benchmark datasets**.

It enables efficient dataset handling for **training and evaluation**, providing flexible filtering capabilities by:
- **Subject**
- **Skill**
- **Target**

This allows users to build **custom benchmarks** tailored to specific needs and conduct **holistic evaluations** of language models.
![Overview](assets/benchhub_overview.png)

## 🔧 Features

The evaluation system in `BenchHub` provides key utilities for conducting standardized LLM evaluation. 

We currently support three main function for evaluation:

1. **Flexible Benchmark Loader (`load_benchhub`,`classify_intent` )**  
  - The primary interface for filtering and loading evaluation datasets.  
   Users can directly specify `skill`, `target`, and `subject` filters to construct customized evaluation subsets.
  - 🧠 Additionally, BenchHub offers an **intent classification** module that maps free-form evaluation goals (e.g., *"Evaluate understanding of Korean culture"*) to structured filters based on BenchHub's taxonomy.
  <!-- ### Example: `load_dataset` Function

  You can load and filter datasets using the `load_benchhub` function. Here's how to use it:

  ```python
  from src import load_benchhub

  df = load_benchhub(
      lang='kor',                # Specify language (e.g., 'kor' for Korean)
      subject=['history', 'math'],  # Filter based on subjects
      skill='reasoning',         # Filter based on skill type
      target='general',          # Filter based on target type
      save='filtered_dataset.csv' # Optionally save the filtered dataset to a CSV file
  )
  ``` -->


2. **Evaluation Execution (via HRET)**  
  - BenchHub works in conjunction with the [HRET (Haerae Evaluation Toolkit)](https://github.com/HAE-RAE/haerae-evaluation-toolkit/) evaluation toolkit to support evaluations using string-matching, LLM inference, or external scoring. This collaboration ensures compatibility with broader evaluation pipelines.

3. **Citation Report Generator**  
  - As BenchHub serves mixture of benchmarks, we provide automated LaTeX + BibTeX reports that document the dataset sources included in your evaluation. This supports transparent reporting in research papers.

4. **Category-Wise Performance Analysis (TBA)**
  - A future module will support category-wise accuracy analysis, allowing users to break down evaluation results by skill type, subject area, or benchmark source.

> 📂 For full usage and code examples, see [`evaluation/README.md`](evaluation/README.md)

## Submit Your Dataset
If you would like your dataset to be included in BenchHub, please submit a pull request via the "Submit your dataset" section at the following link:
👉 https://huggingface.co/spaces/BenchHub/BenchHub

## Implementation of BenchHub 

BenchHub is designed to transform raw benchmarks into BenchHub-compatible formats and to automatically categorize datasets by skill, subject, and target using both rule-based and LLM-guided methods. The code for reformatting and categorization is located in the /pipeline directory, with more details available in [`pipeline/README.md`](pipeline/README.md)
<!-- * **`agents/run.py`**: An end-to-end reformatter based on an agent-driven architecture. It automates the process of reformatting datasets for model training and evaluation in a flexible, scalable manner.
* **`agents/run_determ_github.py`**: A rule-based, LLM-guided reformatter designed specifically for datasets from GitHub. It leverages rule-based logic to process and format the data for easier analysis.
* **`agents/run_determ.py`**: A rule-based, LLM-guided reformatter focused on datasets from Hugging Face. It applies rule-based techniques to preprocess and format Hugging Face datasets for downstream tasks. -->



