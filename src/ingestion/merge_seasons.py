import pandas as pd
import logging
from pathlib import Path

RAW_DATA_DIR = Path("data/raw")
OUTPUT_DIR = Path("data/interim")
OUTPUT_FILE = OUTPUT_DIR / "epl_master.csv"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def extract_season(file_name: str) -> str:
    season = file_name.replace("EPL_", "").replace(".csv", "")
    start, end = season.split("_")
    return f"{start}/{end}"

def load_csv(file_path: Path) -> pd.DataFrame:
    logging.info(f"Loading {file_path.name}")

    data = pd.read_csv(file_path)

    season = extract_season(file_path.name)
    data["Season"] = season

    return data

def merge_seasons():
    csv_files = sorted(RAW_DATA_DIR.glob("*.csv"))

    if not csv_files:
        raise FileNotFoundError(
            f"No csv file found in {RAW_DATA_DIR}"
        )
    logging.info(f"Found {len(csv_files)} CSV files")

    dataframes = []

    for file in csv_files:
        data = load_csv(file)
        dataframes.append(data)

    logging.info("Concatenating datasets...")

    master_data = pd.concat(dataframes, ignore_index=True)

    if "Date" in master_data.columns:
        try:
            master_data["Date"] = pd.to_datetime(master_data['Date'], dayfirst=True, errors="coerce")

            master_data = master_data.sort_values("Date")

        except Exception as e:
            logging.warning(f"Date conversion failed: {e}")


    OUTPUT_DIR.mkdir(
        parents=True, exist_ok=True
        )
    
    master_data.to_csv(
        OUTPUT_FILE, index=False
    )

    logging.info("=" * 50)
    logging.info("MERGE COMPLETE")
    logging.info(f"Rows: {master_data.shape[0]}")
    logging.info(f"Columns: {master_data.shape[1]}")
    logging.info(f"Saved to: {OUTPUT_FILE}")
    logging.info("=" * 50)

    return master_data


if __name__ == "__main__":
    data = merge_seasons()
    print("\nDataset Preview:")
    print(data.head())

    print("\nDataset Shape:")
    print(data.shape)
    print(data.info())
    print(data.head())
    print(data.tail())
    print(data["Date"].dtype)
    print(data["Season"].value_counts())
    print(data["Date"].min())
    print(data["Date"].max())