import yfinance as yf

def get_stock_data_yahoo(symbol):
    stock = yf.Ticker(symbol)
    data = stock.history(period="1mo")
    return data

# Example usage
symbol = 'AAPL'
data = get_stock_data_yahoo(symbol)
print(data)
