from datasets import load_dataset
from dotenv import load_dotenv
from openai import OpenAI
import os
import sys
import pandas as pd
from src.utils import benchhub_citation_report, uniform_2d_sample
from src.description import SUBJECT_HIERARCHY_WITH_DESCRIPTION 
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)

def load_benchhub(lang='en', subject=None, skill=None, target=None, save=None, sampling=False):
    """
    lang: 'en' or 'ko'
    subject: list of str, filter if any string in subject_type contains any of these
    skill: str, filter if skill is substring in task_type
    target: str, filter if target is substring in target_type
    save: path to save filtered dataframe as CSV
    sampling: bool, if True, will sample uniformly using query embedding
    Returns a filtered pandas DataFrame.
    """
    # Hugging Face repo name
    repo_name = f"BenchHub/BenchHub-{lang}"

    # Load dataset from Hugging Face Hub directly
    dataset = load_dataset(repo_name, split='train')
    df = pd.DataFrame(dataset)
    # Filter by subject: Check if any of the given subjects are contained in subject_type column
    if subject is not None and isinstance(subject, list):
        # Apply filter to subject_type based on user input
        mask_subject = df['subject_type'].apply(lambda x: any(sub.split('/')[-1].lower() in str(x) for sub in subject))
        df = df[mask_subject]

    # Filter by skill: Check if skill is a substring of task_type column
    if skill is not None:
        if isinstance(skill, str):
            skill = [skill]
        mask_skill = df['task_type'].apply(lambda x: any(sk.lower() in str(x).lower() for sk in skill))
        df = df[mask_skill]
    # Filter by target: Check if target is a substring of target_type column
    if target is not None:
        if isinstance(target, str):
            target = [target]
        mask_target = df['target_type'].apply(lambda x: any(tag.lower() in str(x).lower().replace('cultural','local') for tag in target))
        df = df[mask_target]
    # Save the filtered DataFrame to a CSV file
    if save:
        df.to_csv(save, index=False)
        print(f"Filtered dataset saved to {save}")
        print(f"Number of {save} dataset: {len(df)}")
    # Return the filtered DataFrame
    if df.empty:
        print("No data found with the specified filters.")
        return pd.DataFrame()  # Return an empty DataFrame if no data matches the filters
    if sampling:
        # Sample uniformly using query embedding
        from sentence_transformers import SentenceTransformer
        import torch

        device = 'cuda' if torch.cuda.is_available() else 'cpu'
        model = SentenceTransformer('all-mpnet-base-v2', device=device)
        embeddings = model.encode(df['query'].tolist(), show_progress_bar=True)
        df['embedding'] = embeddings.tolist()
        df['embedding'] = df['embedding'].apply(lambda x: json.dumps(x))
        print("Embeddings computed and saved to benchhub_embeddings.pkl")
        # reduce 2-dimensionality using t-SNE 
        from sklearn.manifold import TSNE
        tsne = TSNE(n_components=2, random_state=42)
        reduced_embeddings = tsne.fit_transform(embeddings)
        df['tsne_x'] = reduced_embeddings[:, 0]
        df['tsne_y'] = reduced_embeddings[:, 1]
        df.to_pickle("benchhub_embeddings.pkl")
        # sampling based on tsne_x and tsne_y
        df, n_samples = uniform_2d_sample(df, x_col='tsne_x', y_col='tsne_y', n_samples=len(df))
        print(f"Sampled {n_samples} rows.")
    return df

def extract_subject_labels(classification_result):
    """
    Process subject field from classification result into a standardized list of subject labels.

    Returns:
        List of strings:
        - If fine-grained: ["Coarse/Fine", ...]
        - If only coarse: ["Coarse"]
    """
    subject = classification_result.get("subject")

    if isinstance(subject, dict):  # Only coarse subject
        return [subject["coarse"]]

    elif isinstance(subject, list):  # Fine-grained subjects
        return [f'{s["coarse"]}/{s["fine"]}' for s in subject]

    else:
        raise ValueError("Unexpected subject format")

def classify_intent(intent_text: str) -> dict:
    """
    Classify evaluation intent into skill, target, and subject.
    If the intent is abstract/general, return only the coarse-grained subject.
    If the intent is specific, return fine-grained subject(s) with their coarse category. 
    e.g., ["Culture"] or ["Culture/Food", "Culture/Clothing"]

    """

    # Build subject prompt
    subject_prompt = "\n".join([
        f"{coarse}:\n" + "\n".join(
            f"- {fine}: {desc}" for fine, desc in fine_map.items()
        )
        for coarse, fine_map in SUBJECT_HIERARCHY_WITH_DESCRIPTION.items()
    ])

    system_prompt = f"""
You are an assistant that classifies evaluation intents.

1. Skill (choose ALL applicable):
- Knowledge
- Reasoning
- Value/alignment

2. Target (choose ALL applicable):
- General
- Local

3. Subject:
- If the evaluation intent is **broad** (e.g., "Korean culture", "science"), return ONLY the **coarse-grained subject**, like:
  "subject": {{ "coarse": "Culture" }}
- If the intent is **specific**, return all applicable **fine-grained subjects with their coarse category**, like:
  "subject": [{{ "coarse": "Culture", "fine": "Food" }}, ...]

Subjects list:
{subject_prompt}

Return your response in strict JSON:
{{
  "skill": ["..."],
  "target": ["..."],
  "subject": {{
    "coarse": "..." 
  }}
}} 
OR
{{
  "skill": ["..."],
  "target": ["..."],
  "subject": [
    {{ "coarse": "...", "fine": "..." }},
    ...
  ]
}}
"""

    user_prompt = f"Evaluation intent: \"{intent_text}\""

    response = client.chat.completions.create(model="gpt-4",
    messages=[
        {"role": "system", "content": system_prompt.strip()},
        {"role": "user", "content": user_prompt.strip()}
    ],
    temperature=0.0)

    response_dict = eval(response.choices[0].message.content)
    subject_formatted = []
    subject_formatted = extract_subject_labels(response_dict)  # Ensure subject is processed
    response_dict['subject'] = subject_formatted
    return response_dict

if __name__ == "__main__":
    # Assume classify_intent() and SUBJECT_HIERARCHY_WITH_DESCRIPTION are already defined

    # Example evaluation intent (in Korean)
    intent = "I want to evaluate Korean culture."

    # Step 1: Use LLM to classify the intent
    classification = {'skill': ['Knowledge'], 'target': ['General'], 'subject': ['Culture']}#classify_intent(intent)

    # Step 2: Extract arguments for load_benchhub
    skills = classification["skill"]                # e.g., ['Knowledge']
    targets = classification["target"]          # e.g., ['Local']
    subjects = classification["subject"]  # e.g., ['food', 'clothing']

    # Step 3: Load benchmark data filtered using classified info
    df = load_benchhub(
        lang='Ko',
        subject=subjects,
        skill=skills,
        target=targets,
        save='filtered_dataset.csv'
    )
    print(df.head())

    # Step 4: Download citation report
    benchhub_citation_report(df,"citation.txt") 
    #benchhub_citation_report(df,"citation.tex") 
    