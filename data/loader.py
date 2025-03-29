import logging
logging.basicConfig(level=logging.INFO)
from data.polygon_api import fetch_polygon_data

def load_data(symbol="AAPL", from_date="2022-01-01", to_date="2024-12-31"):
    """
    وظيفة: load_data
    """
    return fetch_polygon_data(symbol, from_date, to_date)
