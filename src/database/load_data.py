import pandas as pd 
from connection import get_engine

engine = get_engine()

file = "data/yellow_tripdata_2025-01_clean.parquet"

def load_data():
    df = pd.read_parquet(file)
    df.to_sql("transformed_taxi_data", engine, if_exists="append", index=False, chunksize=5000)
    print("Data loaded successfully")

if __name__ == "__main__":
    load_data()

