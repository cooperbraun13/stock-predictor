import yfinance as yf

# Download historical data for Apple (AAPL)
apple = yf.Ticker("AAPL")
# History over last 5 years
historical_data = apple.history(period="5y")

print(historical_data)

historical_data.to_csv("aapl.csv")