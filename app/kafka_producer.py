import websocket
import json
from kafka import KafkaProducer
from datetime import datetime

# Kafka config
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)
KAFKA_TOPIC = "crypto-prices"

def send_to_kafka(symbol, price):
    try:
        data = {
            "symbol": symbol,
            "price": round(float(price), 2),
            "timestamp": datetime.utcnow().isoformat()
        }
        print(f"📤 Sending to Kafka: {data}")
        producer.send(KAFKA_TOPIC, value=data)
    except Exception as e:
        print(f"❌ Kafka Send Error: {e}")

def on_message(ws, message):
    try:
        msg = json.loads(message)
        if msg.get("e") == "trade":
            symbol = msg.get("s")
            price = msg.get("p")
            if symbol and price:
                send_to_kafka(symbol, price)
    except Exception as e:
        print("❌ WebSocket Parse Error:", e)

def start_producer():
    print("🚀 Starting Binance WebSocket → Kafka Producer...")
    socket = "wss://stream.binance.com:9443/ws/btcusdt@trade"  # direct stream
    ws = websocket.WebSocketApp(
        socket,
        on_message=on_message
    )
    ws.run_forever()

if __name__ == "__main__":
    start_producer()
