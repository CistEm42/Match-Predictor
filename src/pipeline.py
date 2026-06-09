import pandas as pd
from pathlib import Path

from preprocessing.cleaning import remove_high_missing_columns


DATA_PATH = "data/interim/epl_master.csv"
OUTPUT_DIR = Path("data/processed")
OUTPUT_FILE = OUTPUT_DIR / "cleaned.csv"


def run_pipeline():
    # 1. Load data
    data = pd.read_csv(DATA_PATH)

    # 2. Clean data
    data = remove_high_missing_columns(data)
    data["AHh"] = data["AHh"].fillna(data["AHh"].median())
    data["MaxCAHH"] = data["MaxCAHH"].fillna(data["MaxCAHH"].median())
    data["MaxCAHA"] = data["MaxCAHA"].fillna(data["MaxCAHA"].median())


    # 3. (next steps will come later)
    print("After cleaning:", data.shape)

    OUTPUT_DIR.mkdir(
        parents=True, exist_ok=True
        )
    
    data.to_csv(
        OUTPUT_FILE, index=False
    )

    return data


if __name__ == "__main__":
    run_pipeline()