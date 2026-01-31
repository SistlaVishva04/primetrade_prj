# Binance Futures CLI Trading Bot

## 📌 Project Overview

This project is a **CLI-based trading bot** built for **Binance USDT-M Futures**.  
It allows users to place futures orders directly from the command line using the **official Binance Futures API**.

The bot is designed for **educational and evaluation purposes** and runs entirely on the **Binance Futures Testnet**, meaning **no real money is used**.

---

## 🎯 Objectives

- Build a command-line (CLI) trading bot (no UI / no web app)
- Support core and advanced futures order types
- Implement proper input validation and structured logging
- Follow clean project structure and secure API handling

---

## ✅ Features Implemented

### Core Orders (Mandatory)
- **Market Orders**
  - Instant BUY or SELL at current market price
- **Limit Orders**
  - BUY or SELL at a specified price (GTC – Good Till Cancelled)

### Advanced Orders
- **TWAP (Time-Weighted Average Price)**
  - Splits a large order into smaller market orders
  - Executes them at fixed time intervals to reduce market impact

### Other Capabilities
- CLI-based execution
- Input validation (symbol, side, quantity, price)
- Structured logging to `bot.log`
- Secure API key management using environment variables

---

## 🛠 Tech Stack

- **Language:** Python 3.9+
- **Library:** python-binance
- **API:** Binance USDT-M Futures Testnet
- **Logging:** Python logging module
- **Security:** Environment variables (`.env`)

---

## 📁 Project Structure
```
binance_bot/
│
├── src/
│ ├── market_orders.py # Market order CLI
│ ├── limit_orders.py # Limit order CLI
│ ├── logger.py # Logging configuration
│ ├── validators.py # Input validation
│ │
│ └── advanced/
│ └── twap.py # TWAP strategy
│
├── bot.log # Execution & error logs
├── README.md # Project documentation
├── report.pdf # Analysis & screenshots
└── .env # API keys (ignored in git)
```

---

## 🔐 API & Environment Setup

### 1️⃣ Create Binance Futures Testnet Account
- Visit: https://testnet.binancefuture.com
- Generate **API Key** and **Secret**

### 2️⃣ Create `.env` file (project root)

```env
BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_api_secret
```

**⚠️ The project uses testnet only**.
No real funds or real trades are involved.

## 📦 Installation

Install dependencies:
```
pip install python-binance python-dotenv
```
## ▶️ How to Run (CLI Commands)

Run all commands from the project root directory.

### 🔹 **Market Order**

Places an instant BUY or SELL order at market price.
```
python src/market_orders.py BTCUSDT BUY 0.01
```

**What it does**:

- Opens a futures position at current market price

- Executes immediately

- Logs the order result

### 🔹 **Limit Order**

Places an order at a specific price.
```
python src/limit_orders.py BTCUSDT SELL 0.01 90000
```

**What it does**:

- Places a SELL limit order at 90,000 USDT

- Order stays open until price is reached or canceled

- Logs order placement

### 🔹 TWAP Order (Advanced)

Splits a large order into smaller orders over time.
```
python src/advanced/twap.py BTCUSDT BUY 0.05 5 10
```

**Meaning**:
```
- Total quantity: 0.05 BTC

- Split into: 5 orders

- Delay between orders: 10 seconds
```
**What it does**:

- Places 5 market orders of 0.01 BTC each

- Executes them sequentially

- Logs each execution

## 📝 Logging

**All actions, executions, and errors are logged to**:
```
bot.log
```

Each log entry includes:

- Timestamp

- Order type

- Execution details or errors

### ⚠️ Important Notes

- This project uses Binance USDT-M Futures Testnet only

- No real cryptocurrency is bought or sold

- TWAP is implemented as a strategy, not a native Binance feature

- API keys are securely loaded via environment variables

## 📄 Report

The report.pdf contains:

- Project explanation

- Architecture overview

- Screenshots of successful order executions

- Sample log outputs

## 🏁 Conclusion

This project demonstrates:

- Practical use of Binance Futures APIs

- CLI-based system design

- Secure credential handling

- Clean logging and validation

- Implementation of an advanced trading strategy (TWAP)

- It is designed to be reproducible, safe, and easy to evaluate.

---
## 👤 Author
Vishnu Vamsi

Email: vishnuvamsi04@gmail.com

