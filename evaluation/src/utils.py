import json
import pandas as pd
from typing import Any, Dict, List, Callable, Any, Union
from collections import Counter 
import importlib
import os
import sys
# sys.path.append(os.path.join(os.path.dirname(__file__)))

sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
from dataset.benchmark_info import DATASETS

def to_dataframe(self) -> pd.DataFrame:
    """
    Return a DataFrame where each row is a sample, with columns:
        - "input", "reference", "prediction"
        - Possibly flattened fields like "evaluation.is_correct"
        - Additional fields if they exist
    """
    df = pd.DataFrame(self.samples)
    if "evaluation" in df.columns:
        # Flatten 'evaluation' dict into separate columns 
        eval_df = df["evaluation"].apply(pd.Series)
        df = pd.concat([df.drop(columns=["evaluation"]), eval_df.add_prefix("eval_")], axis=1)
    return df

def save_json(path: str):
    """
    Save the entire result (metrics, samples, info) to a JSON file.
    """
    with open(path, "w", encoding="utf-8") as f:
        json.dump(self.to_dict(), f, ensure_ascii=False, indent=2)

def benchhub_citation_report(df,output_path: str) -> None:
    """
    Generates a LaTeX citation report for evaluations run with the BenchHub dataset.
    
    This method creates a LaTeX table summarizing the datasets included in the evaluation
    and provides the necessary BibTeX entries for citation. The report is saved to the
    specified output path.

    Args:
        output_path (str): The file path where the LaTeX report will be saved.
    
    Raises:
        ValueError: If this method is called on an EvaluationResult that was not
                    generated from a BenchHub dataset run (i.e., 'benchmark_details' missing in info).
    """
    # if "benchmark_details" not in self.info:
    #     raise ValueError(
    #         "This report can only be generated for results from a BenchHub dataset run, "
    #         "as it requires 'benchmark_details' in the 'info' dictionary."
    #     )
    
    # 1. Count samples for each benchmark
    benchmark_names = [
        sample
        for sample in df['benchmark_name']
    ]
    sample_counts = Counter(benchmark_names)

    # 2. Build the LaTeX table rows
    table_rows = []
    references = ""
    for benchmark_info in DATASETS:
        benchmark_name = benchmark_info.dataset_key
        count = sample_counts.get(benchmark_name, 0)
        citation_key = benchmark_info.citation_key
        if count != 0:
            table_rows.append(f"\\cite{{{citation_key}}} & {count} \\\\")
            citation = benchmark_info.citation
            references += f"\n{citation}\n"
    table_content = "\n".join(table_rows)

    # 3. HRET Citation (from README.md)
    hret_citation = """@article{lee2025hret,
title={HRET: A Self-Evolving LLM Evaluation Toolkit for Korean},
author={Lee, Hanwool and Kim, Soo Yong and Choi, Dasol and Baek, SangWon and Hong, Seunghyeok and Jeong, Ilgyun and Hwang, Inseon and Lee, Naeun and Son, Guijin},
journal={arXiv preprint arXiv:2503.22968},
year={2025}
}"""

    # 4. BenchHub Citation (provided by user)
    benchhub_citation = """@misc{kim2025benchhub,
    title={BenchHub: A Unified Benchmark Suite for Holistic and Customizable LLM Evaluation}, 
    author={Eunsu Kim and Haneul Yoo and Guijin Son and Hitesh Patel and Amit Agarwal and Alice Oh},
    year={2025},
    eprint={2506.00482},
    archivePrefix={arXiv},
    primaryClass={cs.LG},
    url={https://arxiv.org/abs/2506.00482}, 
}"""

    # 5. Build the full LaTeX report string
    report_template = f"""
The evaluation dataset are sampled using BenchHub~\\cite{{kim2025benchhub}}. 
%If you use hret for the evaluation, please add the following text: The evaluation is conducted using hret~\cite{{lee2025hret}}.
The individual datasets include in the evaluation set, along with their statistics, are summarized in Table~\\ref{{tab:eval-dataset}}.

% Please add the following required packages to your document preamble:
% \\usepackage{{booktabs}}
\\begin{{table}}[h]
\\centering
\\begin{{tabular}}{{@{{}}ll@{{}}}}
\\toprule
\\textbf{{Dataset}} & \\textbf{{Number of Samples}} \\\\ \\midrule
{table_content}
\\bottomrule
\\end{{tabular}}
\\caption{{Breakdown of datasets included in the evaluation set.}}
\\label{{tab:eval-dataset}}
\\end{{table}}

% --- BibTeX Entries ---

{hret_citation}

{benchhub_citation}
"""
    report_template += references
    # Add citations for each individual benchmark

    # 6. Write to file
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(report_template.strip())
            print(f"BenchHub citation report successfully saved to '{output_path}'.")
    except IOError as e:
        print(f"Failed to write citation report to '{output_path}': {e}", exc_info=True)
        raise
