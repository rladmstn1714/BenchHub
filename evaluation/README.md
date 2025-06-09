# 📘 Evaluation Module

This directory contains the core utilities for filtering, evaluating, and citing benchmark datasets using the BenchHub taxonomy. It is the main entry point for users who want to perform systematic evaluation of LLMs.

---

## 📦 Components

### 1. `dataset_loader.py`

#### 🔹 Function: `load_benchhub()`

Load and filter evaluation subsets from BenchHub using structured metadata. This module also includes intent classification utilities for converting natural language queries into structured filters.

```python
from evaluation.dataset_loader import load_benchhub, classify_intent

# Option 1: Load using structured filters
df = load_benchhub(
    lang='kor',
    subject=['Science/Mathematics'],
    skill='reasoning',
    target='general',
    save='math_eval.csv'
)

# Option 2: Load using natural language intent
intent = "I want to evaluate understanding of Korean traditional food and clothing."
parsed = classify_intent(intent)
df = load_benchhub(
    lang='kor',
    subject=parsed['subject_labels'],
    skill=parsed['skill'],
    target=parsed['target']
)
```

**Parameters:**

* `lang`: Language filter (`'kor'` or `'en'`)
* `subject`: List of subjects (fine or coarse/fine, e.g. `'Science/Mathematics'`)
* `skill`: Task type (`'knowledge'`, `'reasoning'`, `'value/alignment'`)
* `target`: Target type (`'general'` or `'local'`)
* `save`: Optional filename to save the filtered DataFrame

---

### 2. `evaluation.py`

#### 🔹 Function: `run_benchhub_evaluation()`

Run full evaluation pipeline via HRET, including filtering, model execution, and citation. Citation generation is handled internally within this module.

```python
from evaluation.evaluate import run_benchhub_evaluation

results = run_benchhub_evaluation(
    skill_type=['knowledge'],
    target_type=['local'],
    subject_type=['Culture/Food', 'Culture/Clothing'],
    problem_type=['MCQA'],
    citation_path='report.tex'
)
```

**Arguments:**

* `skill_type`, `target_type`, `subject_type`, `problem_type`: Filtering parameters
* `benchmark_names`: Optional list of specific benchmarks to include
* `language`: Language of the dataset (`'kor'` or `'en'`)
* `dataset`: Dataset name (default: `'benchhub'`)
* `citation_path`: Optional LaTeX file path to export citation report
* `model_name`, `api_base`, etc.: Model execution configuration

---

## 🧪 Backend Evaluation

This module is fully integrated with [HRET (Haerae Evaluation Toolkit)](https://github.com/HAE-RAE/haerae-evaluation-toolkit/), supporting evaluation methods including:

* `string_match`
* `llm_judge`
* `custom` scoring functions

---

## 📂 Directory Overview

```
evaluation/
├── evaluation.py            # Main pipeline and citation generator
├── dataset_loader.py        # Dataset loader and intent classifier
├── analyze.py               # TBA
└── README.md                # You're here :)
```

---

For questions or contributions, please open an issue or contact the maintainers.
