def handle_price(data):
    try:
        symbol = data['s']
        price = data['c']
        print(f"💰 {symbol}: ${price}")
    except KeyError:
        print("Invalid message structure:", data)
