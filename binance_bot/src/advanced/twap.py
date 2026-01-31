import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import time
from binance.client import Client
from logger import get_logger
from validators import validate_symbol, validate_side, validate_quantity

from dotenv import load_dotenv
load_dotenv()
API_KEY =os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

if not API_KEY or not API_SECRET:
    raise Exception("API keys not found. Check .env file.")


logger = get_logger()



def main():
    if len(sys.argv) != 6:
        print("Usage: python twap.py SYMBOL BUY/SELL TOTAL_QTY PARTS DELAY_SEC")
        sys.exit(1)

    symbol = sys.argv[1]
    side = sys.argv[2].upper()
    total_qty = sys.argv[3]
    parts = int(sys.argv[4])
    delay = int(sys.argv[5])

    try:
        validate_symbol(symbol)
        validate_side(side)
        total_qty = validate_quantity(total_qty)

        chunk_qty = round(total_qty / parts, 6)

        client = Client(API_KEY, API_SECRET)
        client.FUTURES_URL = "https://testnet.binancefuture.com"

        for i in range(parts):
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=chunk_qty
            )

            logger.info(
                f"TWAP ORDER {i+1}/{parts} | {order}"
            )
            print(f"TWAP order {i+1}/{parts} placed")

            time.sleep(delay)

    except Exception as e:
        logger.error(f"TWAP ERROR | {str(e)}")
        print("Error:", e)

if __name__ == "__main__":
    main()
