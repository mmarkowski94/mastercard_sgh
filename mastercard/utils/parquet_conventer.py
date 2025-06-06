from pathlib import Path

import pandas as pd

RAW_DIR = Path(__file__).resolve().parent.parent.parent / "data" / "raw"
PROCESSED_DIR = Path(__file__).resolve().parent.parent.parent / "data" / "processed"


def convert_json_to_parquet(filename: Path, output_name: str | None = None) -> None:
	"""Load line-delimited JSON file and save as Parquet."""
	df = pd.read_json(filename, lines=True)

	if output_name is None:
		output_name = filename.name.replace(".json", ".parquet")
	df.to_parquet(PROCESSED_DIR / output_name, index=False)


def convert_csv_to_parquet(filename: Path, output_name: str | None = None) -> None:
	"""Load CSV file and save as Parquet."""
	df = pd.read_csv(filename)

	if output_name is None:
		output_name = filename.name.replace(".csv", ".parquet")
	df.to_parquet(PROCESSED_DIR / output_name, index=False)


if __name__ == "__main__":
	convert_json_to_parquet(RAW_DIR / "transactions.json")
	convert_csv_to_parquet(RAW_DIR / "users.csv")
	convert_csv_to_parquet(RAW_DIR / "merchants.csv")
