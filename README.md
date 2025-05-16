# BenchHub

**BenchHub** is a tool designed to help researchers and developers easily load, filter, and process various benchmark datasets. It allows efficient handling of datasets for model training and evaluation, with functionality for filtering based on specific criteria such as subject, skill, and target. This makes it easier to experiment with and analyze datasets tailored to particular needs.

### Agents

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

This function helps you load datasets, apply necessary filters, and optionally save the processed data for further analysis or training.
