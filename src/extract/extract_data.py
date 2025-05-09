import pandas as pd

def extract_data(file_path: str) -> pd.DataFrame:
    """
    Extract data from a parquet file and return a pandas DataFrame.
    """
    df = pd.read_parquet(file_path)
    return df

if __name__ == "__main__":
    file_path = "data/yellow_tripdata_2025-01_clean.parquet"
    df = extract_data(file_path)
    print(df.head())


