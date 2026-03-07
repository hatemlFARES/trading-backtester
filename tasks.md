# Trading Backtester - tasks

## tasks for the next time

Task 1 — Fix data types
The open, high, low, close, volume columns are currently strings. Convert them to numbers so you can do math on them.
Hint: look up pd.to_numeric() or astype(float)

Task 2 — Make load_data() flexible
Right now load_data() only works for BTCUSDT. Change it so it accepts symbol, interval, start_date as parameters so tomorrow you could call it with any coin.
Hint: think about how fetch_all_candles() receives parameters.

Task 3 — Add error handling
What if Binance is down or your internet cuts out? Wrap the Binance request in a try/except so instead of crashing it prints a friendly error message.
Hint: look up try/except requests.exceptions.RequestException
