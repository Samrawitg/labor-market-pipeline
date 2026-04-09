import pandas as pd
import os
from config import RAW_DATA_PATH

PROCESSED_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "processed")

def transform_combined():
    print("Transforming BLS + FRED data...")

    bls = pd.read_csv(os.path.join(RAW_DATA_PATH, "bls_unemployment.csv"))
    fred = pd.read_csv(os.path.join(RAW_DATA_PATH, "fred_indicators.csv"))
    
    # Fix BLS date
    bls["date"] = pd.to_datetime(
        bls["year"].astype(str) + "-" + bls["month"] + "-01",
        format="%Y-%B-%d"
    )
    bls = bls.drop(columns=["year", "period", "month"])
 
    # Pivot FRED
    fred["date"] = pd.to_datetime(fred["date"])
    fred["value"] = pd.to_numeric(fred["value"], errors="coerce")
    fred_pivot = fred.pivot_table(
        index="date",
        columns="series_name",
        values="value"
    ).reset_index()
    fred_pivot.columns.name = None

    # Merge
    combined = pd.merge(bls, fred_pivot, on="date", how="left")
    
    # Handle duplicate unemployment_rate columns from merge
    if "unemployment_rate_x" in combined.columns:
        combined = combined.drop(columns=["unemployment_rate_y"])
        combined = combined.rename(columns={"unemployment_rate_x": "unemployment_rate_bls"})
    elif "unemployment_rate" in combined.columns:
        combined = combined.rename(columns={"unemployment_rate": "unemployment_rate_bls"})

    # Feature engineering
    combined = combined.sort_values(["industry", "date"])
    combined["unemployment_yoy_change"] = combined.groupby("industry")[
        "unemployment_rate_bls"
    ].pct_change(periods=12) * 100
    combined["unemployment_3m_avg"] = combined.groupby("industry")[
            "unemployment_rate_bls"
    ].transform(lambda x: x.rolling(3).mean())
    combined["wage_vs_inflation"] = combined["avg_hourly_earnings"] / combined["cpi"]
 
    output_path = os.path.join(PROCESSED_PATH, "combined_labor_data.csv")
    combined.to_csv(output_path, index=False)
    print(f"Combined data saved — {combined.shape[0]} rows, {combined.shape[1]} columns")
    return combined

def transform_oews():
    print("Transforming OEWS data...")

    oews = pd.read_csv(os.path.join(RAW_DATA_PATH, "oews_wages.csv"))

    # Clean column names to lowercase
    oews.columns = oews.columns.str.lower()

    # Keep only detailed occupations, drop summary rows
    oews = oews[oews["o_group"] == "detailed"]

    # Convert wage columns to numeric
    oews["a_median"] = pd.to_numeric(oews["a_median"], errors="coerce")
    oews["h_median"] = pd.to_numeric(oews["h_median"], errors="coerce")
    oews["tot_emp"] = pd.to_numeric(oews["tot_emp"], errors="coerce")

    # Drop rows with no wage data
    oews = oews.dropna(subset=["a_median"])

    output_path = os.path.join(PROCESSED_PATH, "oews_processed.csv")
    oews.to_csv(output_path, index=False)
    print(f"OEWS data saved — {oews.shape[0]} occupations")
    return oews

if __name__ == "__main__":
    transform_combined()
    transform_oews()