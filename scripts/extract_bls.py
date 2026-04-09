import requests
import pandas as pd
import os
from config import BLS_API_KEY, RAW_DATA_PATH

def extract_bls(start_year="2022", end_year="2024"):
    print("Extracting BLS data...")

    series_ids = {
    "LNS14000000": "total",
    "LNU04032231": "construction",
    "LNU04032232": "manufacturing",
    "LNU04032234": "wholesale_retail",
    "LNU04032236": "financial_activities",
    "LNU04032238": "professional_services"
    }

    url = "https://api.bls.gov/publicAPI/v2/timeseries/data/"
    payload = {
        "seriesid": list(series_ids.keys()),
        "startyear": start_year,
        "endyear": end_year,
        "registrationkey": BLS_API_KEY
    }

    response = requests.post(url, json=payload)
    data = response.json()
    
    rows = []
    for series in data["Results"]["series"]:
        series_id = series["seriesID"]
        industry = series_ids[series_id]
        for record in series["data"]:
            rows.append({
                "series_id": series_id,
                "industry": industry,
                "year": record["year"],
                "period": record["period"],
                "month": record["periodName"],
                "unemployment_rate": record["value"]
            })

    df = pd.DataFrame(rows)
    output_path = os.path.join(RAW_DATA_PATH, "bls_unemployment.csv")
    df.to_csv(output_path, index=False)
    print(f"BLS data saved — {len(df)} rows")
    return df

if __name__ == "__main__":
    extract_bls()