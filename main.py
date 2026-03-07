from datetime import datetime
start = datetime(2017, 1, 1)
start_ms = int(start.timestamp() * 1000)
print(start_ms)