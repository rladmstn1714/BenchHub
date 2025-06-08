from datasets import load_dataset
import openai
from src.descriptions import SUBJECT_HIERARCHY_WITH_DESCRIPTION
from dotenv import load_dotenv
import openai
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

openai.api_key = openai_api_key
def load_benchhub(lang='en', subject=None, skill=None, target=None, save=None):
    """
    lang: 'en' or 'ko'
    subject: list of str, filter if any string in subject_type contains any of these
    skill: str, filter if skill is substring in task_type
    target: str, filter if target is substring in target_type
    save: path to save filtered dataframe as CSV
    
    Returns a filtered pandas DataFrame.
    """
    # Hugging Face repo name
    repo_name = f"EunsuKim/BenchHub-{lang}"
    
    # Load dataset from Hugging Face Hub directly
    dataset = load_dataset(repo_name, split='train')
    df = pd.DataFrame(dataset)
    
    # Filter by subject: Check if any of the given subjects are contained in subject_type column
    if subject is not None and isinstance(subject, list):
        # Apply filter to subject_type based on user input
        mask_subject = df['subject_type'].apply(
            lambda x: any(sub in x for sub in subject)
        )
        df = df[mask_subject]
    
    # Filter by skill: Check if skill is a substring of task_type column
    if skill is not None:
        df = df[df['task_type'].str.contains(skill, na=False)]
    
    # Filter by target: Check if target is a substring of target_type column
    if target is not None:
        df = df[df['target_type'].str.contains(target, na=False)]
    
    # Save the filtered DataFrame to a CSV file
    if save:
        df.to_csv(save, index=False)
    
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

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt.strip()},
            {"role": "user", "content": user_prompt.strip()}
        ],
        temperature=0.0
    )

    return eval(response['choices'][0]['message']['content'])

if __name__ == "__main__":
    # Assume classify_intent_multi() and SUBJECT_HIERARCHY_WITH_DESCRIPTION are already defined

    # Example evaluation intent (in Korean)
    intent = "I want to evaluate Korean culture."

    # Step 1: Use LLM to classify the intent
    classification = classify_intent_multi(intent)

    # Step 2: Extract arguments for load_benchhub
    skills = classification["skill"]                # e.g., ['Knowledge']
    targets = classification["target"]              # e.g., ['Local']
    subjects = [s["fine"].lower() for s in classification["subject"]]  # e.g., ['food', 'clothing']

    # Step 3: Load benchmark data filtered using classified info
    df = load_benchhub(
        lang='kor',
        subject=subjects,
        skill=skills,
        target=targets,
        save='filtered_dataset.csv'
    )
    print(df.head())