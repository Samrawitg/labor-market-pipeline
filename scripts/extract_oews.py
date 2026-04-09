import pandas as pd
import os
from config import RAW_DATA_PATH

def extract_oews():
    print("Extracting OEWS data...")

    input_path = os.path.join(RAW_DATA_PATH, "oews_national.xlsx")
    df = pd.read_excel(input_path)

    columns_needed = [
        "OCC_CODE", "OCC_TITLE", "O_GROUP",
        "TOT_EMP", "H_MEDIAN", "A_MEDIAN"
    ]
    df = df[columns_needed]
    
    output_path = os.path.join(RAW_DATA_PATH, "oews_wages.csv")
    df.to_csv(output_path, index=False)
    print(f"OEWS data saved — {len(df)} rows")
    return df

if __name__ == "__main__":
    extract_oews()