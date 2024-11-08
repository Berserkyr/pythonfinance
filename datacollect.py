import yfinance as yf

data =yf.download('AAPL', start='2022-01-01', end='2024-29-07')
print(data.head())


import requests

url ='https://api.stlouisfed.org/fred/series/observations?series_id=DGS10&api_key=YOUR_API_KEY&file_type=json'
response = requests.get(url)
interest_data = response.json()
print(interest_data)


data['volatility'] = data['close'].pct_change().rolling(window=252).std() * (252**0.5)
print(data[['close','volatility']].head())
