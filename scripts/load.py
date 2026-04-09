import pandas as pd
from sqlalchemy import create_engine
import os

PROCESSED_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "processed")

def get_engine():
    return create_engine("postgresql://postgres:guillaume@localhost:5432/labor_pipeline")

def load_combined():
    print("Loading combined labor data into PostgreSQL...")
    df = pd.read_csv(os.path.join(PROCESSED_PATH, "combined_labor_data.csv"))
    engine = get_engine()
    df.to_sql("combined_labor", engine, if_exists="replace", index=False)
    print(f"Loaded {len(df)} rows into combined_labor table")

def load_oews():
    print("Loading OEWS data into PostgreSQL...")
    df = pd.read_csv(os.path.join(PROCESSED_PATH, "oews_processed.csv"))
    engine = get_engine()
    df.to_sql("occupational_wages", engine, if_exists="replace", index=False)
    print(f"Loaded {len(df)} rows into occupational_wages table")

if __name__ == "__main__":
    load_combined()
    load_oews()