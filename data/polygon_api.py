import requests
import pandas as pd
import os

def fetch_polygon_data(symbol, from_date="2023-01-01", to_date="2024-12-31", interval="day"):
    api_key = os.getenv("POLYGON_API_KEY", "demo")
    url = f"https://api.polygon.io/v2/aggs/ticker/{symbol}/range/1/{interval}/{from_date}/{to_date}?adjusted=true&sort=asc&apiKey={api_key}"

    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError(f"Polygon API Error: {response.status_code} - {response.text}")

    data = response.json().get("results", [])
    if not data:
        raise ValueError("No data returned from Polygon API")

    df = pd.DataFrame(data)
    df["timestamp"] = pd.to_datetime(df["t"], unit="ms")
    df.set_index("timestamp", inplace=True)
    df.rename(columns={"o": "Open", "h": "High", "l": "Low", "c": "Close", "v": "Volume"}, inplace=True)
    return df[["Open", "High", "Low", "Close", "Volume"]]