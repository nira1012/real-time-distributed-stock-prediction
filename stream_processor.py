from collections import deque
import numpy as np
import pickle
import os


WINDOW_SIZE = 10
price_window = {}

def process_event(event):
    stock = event["stock"]
    price = event["price"]

    if stock not in price_window:
        price_window[stock] = deque(maxlen=WINDOW_SIZE)

    price_window[stock].append(price)

    if len(price_window[stock]) == WINDOW_SIZE:
        avg = np.mean(price_window[stock])
        std = np.std(price_window[stock])

        if abs(price - avg) > 2 * std:
            print(f"🚨 ANOMALY DETECTED → {stock} | Price: {price:.2f}")

CHECKPOINT_FILE = "checkpoint.pkl"

def save_checkpoint():
    with open(CHECKPOINT_FILE, "wb") as f:
        pickle.dump(price_window, f)

def load_checkpoint():
    global price_window
    if os.path.exists(CHECKPOINT_FILE):
        with open(CHECKPOINT_FILE, "rb") as f:
            price_window = pickle.load(f)

load_checkpoint()
save_checkpoint()
