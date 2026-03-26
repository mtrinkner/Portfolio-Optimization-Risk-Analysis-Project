import pandas as pd
import yfinance as yf

def get_data():
    
    tickers = ['META', 'AMD', 'MSFT', 'SPY']
    data = yf.download(tickers, start='2020-01-01')['Close']
    returns = data.pct_change().dropna()
    asset_returns = returns[['META', 'AMD', 'MSFT']]
    market_returns = returns['SPY']

    return asset_returns, market_returns