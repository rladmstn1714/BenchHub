import json
import pandas as pd
from typing import Any, Dict, List, Callable, Any, Union
from collections import Counter 
import importlib
import os
import sys
from dataset.benchmark_info import DATASETS
import numpy as np
import ast
# sys.path.append(os.path.join(os.path.dirname(__file__)))

sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))


def uniform_2d_sample(df, x_col='tsne_0', y_col='tsne_1', n_samples=100, seed=42):
    np.random.seed(seed)

    # 1. 전체 범위
    x_min, x_max = df[x_col].min(), df[x_col].max()
    y_min, y_max = df[y_col].min(), df[y_col].max()

    # 2. 격자 크기 (ceil로 해서 최대한 N개 채우도록)
    grid_size = int(np.ceil(np.sqrt(n_samples)))
    x_bins = np.linspace(x_min, x_max, grid_size + 1)
    y_bins = np.linspace(y_min, y_max, grid_size + 1)

    sampled_indices = []

    # 3. 각 셀에 대해 샘플 1개
    for i in range(grid_size):
        for j in range(grid_size):
            x_mask = (df[x_col] >= x_bins[i]) & (df[x_col] < x_bins[i + 1])
            y_mask = (df[y_col] >= y_bins[j]) & (df[y_col] < y_bins[j + 1])
            cell_df = df[x_mask & y_mask]

            if not cell_df.empty:
                sampled_indices.append(cell_df.sample(1).index[0])
    print(f"real N :{len(sampled_indices)}")
    return df.loc[sampled_indices].reset_index(drop=True), len(sampled_indices)

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
        license_ = benchmark_info.license
        if count != 0:
            table_rows.append(f"\\cite{{{citation_key}}} & {count} & {license_}\\\\")
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
\\begin{{tabular}}{{@{{}}lll@{{}}}}
\\toprule
\\textbf{{Dataset}} & \\textbf{{Number of Samples}} & \\textbf{{License}} \\\\ \\midrule
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

