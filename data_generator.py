from stream_processor import process_event
import time
import random
from datetime import datetime

stocks = ["RELIANCE", "TCS", "HDFCBANK"]

prices = {
    "RELIANCE": 2500,
    "TCS": 3400,
    "HDFCBANK": 1600
}

while True:
    stock = random.choice(stocks)
    change = random.uniform(-5, 5)
    prices[stock] += change

    data = {
        "timestamp": datetime.now(),
        "stock": stock,
        "price": round(prices[stock], 2)
    }

    print(data)
    process_event(data)
    time.sleep(1)
    
