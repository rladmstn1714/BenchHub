from datasets import load_dataset

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

if __name__ == "__main__":
    df = load_benchhub(
        lang='kor',
        subject=['history', 'math'],
        skill='reasoning',
        target='general',
        save='filtered_dataset.csv'
    )
    print(df.head())