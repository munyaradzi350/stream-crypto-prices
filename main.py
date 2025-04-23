# main.py
from app.websocket_client import start_websocket
from dotenv import load_dotenv
import os
import logging

# Load env variables
load_dotenv()
symbol = os.getenv("CRYPTO_SYMBOL", "btcusdt").lower()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="📅 %(asctime)s | 🔔 %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def main():
    logging.info("📡 Starting Crypto Price Tracker...")
    start_websocket(symbol)

if __name__ == "__main__":
    main()
