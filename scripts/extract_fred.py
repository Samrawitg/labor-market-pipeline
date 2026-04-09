import requests
import pandas as pd
import os
from config import FRED_API_KEY, RAW_DATA_PATH

def extract_fred(start_date="2022-01-01", end_date="2024-12-31"):
    print("Extracting FRED data...")

    series = {
        "unemployment_rate": "UNRATE",
        "cpi": "CPIAUCSL",
        "avg_hourly_earnings": "CES0500000003",
        "JOLTS_openings": "JTSJOL"
    }

    rows = []
    for name, series_id in series.items():
        url = "https://api.stlouisfed.org/fred/series/observations"
        params = {
            "series_id": series_id,
            "api_key": FRED_API_KEY,
            "file_type": "json",
            "observation_start": start_date,
            "observation_end": end_date
        }
        try:
            response = requests.get(url, params=params, timeout=10)
            data = response.json()
            if "observations" not in data:
                print(f"ERROR on {name}:", data)
                continue
            for obs in data["observations"]:
                rows.append({
                    "series_name": name,
                    "date": obs["date"],
                    "value": obs["value"]
                })
            print(f"{name} pulled — {len(data['observations'])} records")
        except Exception as e:
            print(f"Failed on {name}: {e}")

    df = pd.DataFrame(rows)
    output_path = os.path.join(RAW_DATA_PATH, "fred_indicators.csv")
    df.to_csv(output_path, index=False)
    print(f"FRED data saved — {len(df)} rows total")
    return df

if __name__ == "__main__":
    extract_fred()