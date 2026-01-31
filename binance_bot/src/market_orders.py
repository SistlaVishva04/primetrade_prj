import sys
from binance.client import Client
from logger import get_logger
from validators import validate_symbol, validate_side, validate_quantity
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY =os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")


if not API_KEY or not API_SECRET:
    raise Exception("API keys not found. Check .env file.")

logger = get_logger()


def main():
    if len(sys.argv) != 4:
        print("Usage: python market_orders.py SYMBOL BUY/SELL QUANTITY")
        sys.exit(1)

    symbol = sys.argv[1]
    side = sys.argv[2].upper()
    quantity = sys.argv[3]

    try:
        validate_symbol(symbol)
        validate_side(side)
        quantity = validate_quantity(quantity)

        client = Client(API_KEY, API_SECRET)
        client.FUTURES_URL = "https://testnet.binancefuture.com"

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

        logger.info(f"MARKET ORDER PLACED | {order}")
        print("Order placed successfully")

    except Exception as e:
        logger.error(f"ERROR | {str(e)}")
        print("Error:", e)

if __name__ == "__main__":
    main()
