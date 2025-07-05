import pandas as pd
from dataclasses import dataclass, asdict
from typing import List, Optional
import pprint


@dataclass
class DatasetEntry:
    dataset: str
    dataset_key: str
    citation_key: str
    citation: str
    anthology: Optional[str]
    languages: List[str]
    license: str

def convert_row_to_entry(row) -> DatasetEntry:
    return DatasetEntry(
        dataset=row['dataset'],
        dataset_key=row['dataset_key'],
        citation_key=row['citation_key'],
        citation=row['citation'],
        anthology=row['anthology'] if pd.notna(row['anthology']) and row['anthology'].strip() else None,
        languages=[lang.strip() for lang in row['languages'].split(',')],
        license=row['license']
    )


df = pd.read_csv('dataset/dataset_info.csv')


entries = [convert_row_to_entry(row) for _, row in df.iterrows()]


with open('dataset/dataset_entries_temp.py', 'w', encoding='utf-8') as f:
    f.write("from dataclasses import dataclass\n")
    f.write("from typing import List, Optional\n\n\n")
    f.write("@dataclass\n")
    f.write("class DatasetEntry:\n")
    f.write("    dataset: str\n")
    f.write("    dataset_key: str\n")
    f.write("    citation_key: str\n")
    f.write("    citation: str\n")
    f.write("    anthology: Optional[str]\n")
    f.write("    languages: List[str]\n")
    f.write("    license: str\n\n\n")
    f.write("DATASETS: List[DatasetEntry] =[\n")
    for entry in entries:
        f.write("    DatasetEntry(\n")
        f.write(f"        dataset={entry.dataset!r},\n")
        f.write(f"        dataset_key={entry.dataset_key!r},\n")
        f.write(f"        citation_key={entry.citation_key!r},\n")
        f.write(f"        citation={entry.citation!r},\n")
        f.write(f"        anthology={entry.anthology!r},\n")
        f.write(f"        languages={entry.languages!r},\n")
        f.write(f"        license={entry.license!r}\n")
        f.write("    ),\n")
    f.write("]\n")
