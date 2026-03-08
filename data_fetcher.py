import yfinance as yf
import pandas as pd

def get_stock_list():
    """Returns a list of available stock tickers"""
    return ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA", "NFLX", "META", "NVDA"]

def get_stock_data(ticker):
    """Fetches historical stock data"""
    stock = yf.Ticker(ticker)
    history = stock.history(period="1mo")
    
    return {
        "ticker": ticker,
        "history": history.reset_index().to_dict(orient="records")
    }
