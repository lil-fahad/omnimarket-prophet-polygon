logging.basicConfig(level=logging.INFO)
import logging
import requests
import pandas as pd
import os

def fetch_polygon_data(symbol, from_date="2022-01-01", to_date="2024-12-31", interval="day"):
    """
    وظيفة: fetch_polygon_data
    """
    api_key = os.getenv("POLYGON_API_KEY", "demo")
    url = f"https://api.polygon.io/v2/aggs/ticker/{symbol}/range/1/{interval}/{from_date}/{to_date}?adjusted=true&sort=asc&apiKey={api_key}"
    response = requests.get(url)
    data = response.json().get("results", [])
    df = pd.DataFrame(data)
    df["Date"] = pd.to_datetime(df["t"], unit="ms")
    df.set_index("Date", inplace=True)
    df.rename(columns={"o": "Open", "h": "High", "l": "Low", "c": "Close", "v": "Volume"}, inplace=True)
    return df[["Open", "High", "Low", "Close", "Volume"]]