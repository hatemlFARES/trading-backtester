import requests
import pandas as pd
import os
from config import SYMBOL, INTERVAL, START_DATE, DATA_PATH

def fetch_all_candles(symbol, interval, start_date):
    url = "https://api.binance.com/api/v3/klines"
    start_ms = int(start_date.timestamp() * 1000)
    all_data = []

    while True:
        params = {
            "symbol": symbol,
            "interval": interval,
            "limit": 1000,
            "startTime": start_ms
        }

        response = requests.get(url=url, params=params)
        data = response.json()

        if not data:
            break

        all_data.extend(data)
        start_ms = data[-1][0] + 1

        if len(data) < 1000:
            break

    return all_data


def load_data():
    if os.path.exists(DATA_PATH):
        print("Loading from CSV...")
        return pd.read_csv(DATA_PATH)
    
    print("Fetching from Binance...")
    raw = fetch_all_candles(SYMBOL, INTERVAL, START_DATE)

    df = pd.DataFrame(raw, columns=[
        "open_time", "open", "high", "low", "close",
        "volume", "close_time", "quote_volume", "trades",
        "taker_buy_base", "taker_buy_quote", "ignore"
    ])

    df = df[["open_time", "open", "high", "low", "close", "volume"]]
    df["open_time"] = pd.to_datetime(df["open_time"], unit="ms")

    os.makedirs("data", exist_ok=True)
    df.to_csv(DATA_PATH, index=False)
    print(f"Done! Got {len(df)} candles")
    
    return df


df = load_data()
print(df)