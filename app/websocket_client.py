import websocket
import json
from .price_handler import handle_price
import logging

def on_open(ws):
    payload = {
        "method": "SUBSCRIBE",
        "params": [f"{ws.symbol}@ticker"],
        "id": 1
    }
    ws.send(json.dumps(payload))
    logging.info(f"✅ Subscribed to {ws.symbol.upper()} ticker")

def on_message(ws, message):
    try:
        data = json.loads(message)
        if "c" in data:  # 'c' is the current price in Binance
            handle_price(ws.symbol, data["c"])
        elif "result" in data:
            return  # Ignore subscription confirmation
        else:
            logging.warning(f"Invalid message structure: {data}")
    except Exception as e:
        logging.error(f"Error processing message: {e}")

def on_error(ws, error):
    logging.error(f"WebSocket error: {error}")

def on_close(ws, close_status_code, close_msg):
    logging.warning("🔌 Connection closed")

def start_websocket(symbol):
    url = "wss://stream.binance.com:9443/ws"
    ws = websocket.WebSocketApp(
        url,
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close
    )
    ws.symbol = symbol
    ws.run_forever()
