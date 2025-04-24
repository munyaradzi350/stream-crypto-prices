# 🪙 Crypto Pulse - Live Crypto Price Tracker

Tracks real-time cryptocurrency prices using Binance WebSocket API.


             Binance WebSocket
                    │
                    ▼
          [Kafka Producer (Python)]
                    │
                    ▼
        ┌───── Kafka Topic: crypto-prices ─────┐
        ▼                                      ▼
[Kafka Consumer → MongoDB]              [Future ML Model / Alerting]
        │
        ▼
[MongoDB: crypto.prices]
        │
        ▼
[Streamlit UI]
    - Current Price
    - Historical Chart
    - Timestamp




## Features
- 🌐 Live streaming prices
- ⚙️ Configurable crypto symbol via `.env`
- 🧠 Formatted logging with timestamps
- 📡 Real-time data for Mining Live Streaming Data project

## Setup

```bash
pip install -r requirements.txt
python3 main.py
