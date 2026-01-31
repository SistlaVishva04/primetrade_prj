def validate_symbol(symbol):
    if not symbol.endswith("USDT"):
        raise ValueError("Symbol must end with USDT")

def validate_side(side):
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

def validate_quantity(qty):
    qty = float(qty)
    if qty <= 0:
        raise ValueError("Quantity must be > 0")
    return qty

def validate_price(price):
    price = float(price)
    if price <= 0:
        raise ValueError("Price must be > 0")
    return price
