from llm_eval.evaluator import Evaluator
import pandas as pd
# ----------------------------
# Evaluation runner
# ----------------------------
def run_benchhub_evaluation(
    skill_type: list[str],
    target_type: list[str],
    subject_type: list[str],
    problem_type: list[str],
    benchmark_names: list[str] = None,
    language: str = "ko",
    model_name: str = "gpt-4",
    api_base: str = "http://0.0.0.0:8000/v1/chat/completions",
    batch_size: int = 3,
    split: str = "test",
    evaluation_method: str = "string_match",
    citation_path: str = None,
):
    """
    Run evaluation using HRET and user-defined filtering options.
    """
    dataset_params = {
        "language": language,
        "split": None,
        "problem_type": problem_type,
        "benchmark_names": benchmark_names,
        "task_types": [s.lower() for s in skill],
        "target_types": [t.capitalize() for t in target],
        "subject_types": subject
    }

    evaluator = Evaluator()
    results = evaluator.run(
        model="openai",
        model_params={
            "api_base": api_base,
            "model_name": model_name,
            "batch_size": batch_size
        },
        dataset="benchhub",
        dataset_params=dataset_params,
        evaluation_method=evaluation_method
    )

    if citation_path:
        try:
            results.benchhub_citation_report(output_path=citation_path)
            print(f"Citation report saved to: {citation_path}")
        except ValueError as e:
            print(f"Citation report generation failed: {e}")

    return results


# ----------------------------
# Example usage
# ----------------------------
if __name__ == "__main__":
    # Manual filtering inputs
    skill = ["knowledge"]
    target = ["local"]
    subject = ["Culture/Food", "Culture/Clothing"]

    # Run evaluation
    results = run_benchhub_evaluation(
        skill=skill,
        target=target,
        subject=subject,
        citation_path="benchhub_eval_report.tex",
    )

    print("Metrics:")
    print(results.metrics)
    print("\nPreview:")
    print(results.to_dataframe().head())