# Portfolio Optimization Project

## Overview
This is a simple portfolio optimization project I built in Python.
It finds the best mix of stocks based on return and risk and displays the results in a basic dashboard.

## What it Does
- Pulls historical stock data using yfinance
- Calculates daily returnsdoes
- Generates different portfolio weight combinations
- Evaluates each portfolio using:
  - Return
  - Risk (volatility)
  - Sharpe ratio
- Identifies:
  - Best portfolio (max Sharpe)
  - Safest portfolio (lowest risk)
- Runs a CAPM regression to calculate:
  - Alpha
  - Beta
- Displays results in a simple HTML dashboard

## Tools Used
- Python
- pandas
- numpy
- matplotlib
- statsmodels
- yfinance
- HTML

## How to Run

1. Run the model:
python main.py

2. Start the dashboard:
cd web
python -m http.server 8080

3. Open in your browser:
http://localhost:8080