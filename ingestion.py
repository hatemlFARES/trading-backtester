import requests
import pandas as pd
import os
from datetime import datetime

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

        # No more data — stop
        if not data:
            break

        all_data.extend(data)

        # Move startTime to after the last candle we received
        start_ms = data[-1][0] + 1

        # If we got less than 1000 candles we reached the end
        if len(data) < 1000:
            break

    return all_data


# Fetch everything since 2017
raw = fetch_all_candles("BTCUSDT", "1d", datetime(2017, 1, 1))

df = pd.DataFrame(raw, columns=[
    "open_time", "open", "high", "low", "close",
    "volume", "close_time", "quote_volume", "trades",
    "taker_buy_base", "taker_buy_quote", "ignore"
])

df = df[["open_time", "open", "high", "low", "close", "volume"]]
df["open_time"] = pd.to_datetime(df["open_time"], unit="ms")

os.makedirs("data", exist_ok=True)
df.to_csv("data/BTCUSDT_1d.csv", index=False)

print(f"Done! Got {len(df)} candles")
print(df)