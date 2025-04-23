import websocket
import json
from app.price_handler import handle_price

def on_message(ws, message):
    data = json.loads(message)
    handle_price(data)

def on_error(ws, error):
    print("❌ Error:", error)

def on_close(ws, close_status_code, close_msg):
    print("🔌 Connection closed")

def on_open(ws):

    symbol = "btcusdt"
    payload = {
        "method": "SUBSCRIBE",
        "params": [f"{symbol}@ticker"],
        "id": 1
    }
    ws.send(json.dumps(payload))
    print(f"✅ Subscribed to {symbol} ticker")

def start_websocket():
    socket = "wss://stream.binance.com:9443/ws"
    ws = websocket.WebSocketApp(socket,
                                 on_open=on_open,
                                 on_message=on_message,
                                 on_error=on_error,
                                 on_close=on_close)
    print("📡 Starting Crypto Price Tracker...")
    ws.run_forever()
