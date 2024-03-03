import requests
import yfinance as yf
import numpy as np

# url = 'https://www.alphavantage.co/query?function=TOP_GAINERS_LOSERS&apikey=GN93EPRI42VAHGHX'
# r = requests.get(url)
# data = r.json()
# riskiest = []
#
# for entry in data["top_gainers"][:7]:
# 	riskiest.append(entry["ticker"])
#
# for entry in data["top_losers"][:7]:
# 	riskiest.append(entry["ticker"])
#
#
# risky_companies = []
#
# for ticker in riskiest:
# 	url = f"https://api.polygon.io/v3/reference/tickers?ticker={ticker}&active=true&apiKey=VFSwKNWbH7pv7Yp98ayguccA6KVAJYjr"
# 	print(requests.get(url).status_code)
# 	if requests.get(url).status_code == 200:
# 		ticker_response = requests.get(url).json()
# 		risky_companies.append(ticker_response["results"][0]["name"])
#
# print(risky_companies)

#tick = yf.Ticker("AAPL")

risky_companies = ["AAPL", "GOOGL", "MSFT", "RTX"]
ticks_with_prices = {}

for ticker in risky_companies:
	tick = yf.Ticker(ticker)
	ticks_with_prices[ticker] = np.average(np.array(tick.history(period="1mo")["High"]))

keys = list(ticks_with_prices.keys())
values = list(ticks_with_prices.values())
sorted_value_index = reversed(np.argsort(values))
sorted_dict = {keys[i]: values[i] for i in sorted_value_index}

print(sorted_dict)
