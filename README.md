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



## 🔧 Features

- 🧩 Modular loading of diverse benchmark datasets
- 🔍 Fine-grained filtering by metadata
- 📊 Ready-to-use evaluation interface
- 💻 Integration with Hugging Face Hub for ease of use



### Agent-Based Reformatter

* **`agents/run.py`**: An end-to-end reformatter based on an agent-driven architecture. It automates the process of reformatting datasets for model training and evaluation in a flexible, scalable manner.
* **`agents/run_determ_github.py`**: A rule-based, LLM-guided reformatter designed specifically for datasets from GitHub. It leverages rule-based logic to process and format the data for easier analysis.
* **`agents/run_determ.py`**: A rule-based, LLM-guided reformatter focused on datasets from Hugging Face. It applies rule-based techniques to preprocess and format Hugging Face datasets for downstream tasks.

### Example: `load_dataset` Function

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
```

## 📝 Citation

If you use BenchHub in your research, please cite:

```bibtex
@misc{kim2025benchhub,
      title={BenchHub: A Unified Benchmark Suite for Holistic and Customizable LLM Evaluation}, 
      author={Eunsu Kim and Haneul Yoo and Guijin Son and Hitesh Patel and Amit Agarwal and Alice Oh},
      year={2025},
      eprint={2506.00482},
      archivePrefix={arXiv},
      primaryClass={cs.LG},
      url={https://arxiv.org/abs/2506.00482}, 
}
```

## 📫 Contact

For questions or suggestions, please open an [issue](https://github.com/rladmstn1714/BenchHub/issues) or contact the authors at [kes0317@kaist.ac.kr](mailto:kes0317@kaist.ac.kr).

