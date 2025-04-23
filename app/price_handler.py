import logging

def handle_price(symbol, price):
    try:
        formatted_price = f"${float(price):,.2f}"
        logging.info(f"{symbol.upper()}: {formatted_price}")
    except ValueError:
        logging.error("Received invalid price format.")
