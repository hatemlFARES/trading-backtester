# Trading Backtester - Full Session Summary

## What we are building

A trading backtesting engine in Python - a serious resume project.
It fetches historical price data, runs trading strategies on it,
simulates trades, and shows performance results.

## Architecture - 5 Layers

1. Ingestion → fetch data from yfinance, validate, save as CSV
2. Strategy → BaseStrategy class, children for each strategy (OOP/inheritance)
3. Backtester → simulation loop, tracks balance, trades, fees
4. Analytics → calculates metrics from trade history
5. Dashboard → Streamlit web UI to show results visually

## Folder Structure

trading-backtester/
├── data/ → saved CSV files
├── ingestion/ → fetch, validate, cache data
├── strategy/ → BaseStrategy + RSI, MA strategies etc
├── backtester/ → simulation loop + order tracking
├── analytics/ → performance metrics
├── dashboard/ → Streamlit UI
├── tests/ → unit tests
├── main.py → entry point
├── config.py → all settings
└── requirements.txt → list of libraries

## config.py will contain

- symbol (e.g. "AAPL")
- start_date / end_date
- timeframe (e.g. "1d", "15min")
- initial_balance
- commission fee

## Key decisions made

- No heavy database needed, CSV or SQLite is enough
- Fees deducted after every trade (win or lose)
- Buy signal executes on NEXT candle open (realistic)
- BaseStrategy has generate_signal(data) method
- data = full OHLCV dataframe

## Analytics receives

- Initial balance
- Trade history (entry, exit, P&L)
- Win/loss count
- R:R per trade

## Analytics outputs

- Total return %
- Win rate
- Average R:R
- Max drawdown
- Sharpe ratio

## Tech Stack

Python, pandas, numpy, yfinance, pandas-ta,
plotly, Streamlit, SQLite, pytest

## GitHub

- Repo is set up and working
- Daily workflow: git add . → git commit -m "message" → git push
- On new computer: git clone <repo-url>

## Next Session

- Start coding ingestion/ module
- Fetch data with yfinance
- Save it as CSV
