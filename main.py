from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from data_fetcher import get_stock_list, get_stock_data

app = FastAPI()

# Enable CORS for Frontend Communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Welcome to Stock Market Tracker API"}

@app.get("/stocks")
def fetch_stocks():
    """Returns a list of stock tickers"""
    return {"stocks": get_stock_list()}

@app.get("/stock/{ticker}")
def fetch_stock_data(ticker: str):
    """Returns historical data for a stock"""
    return get_stock_data(ticker)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
