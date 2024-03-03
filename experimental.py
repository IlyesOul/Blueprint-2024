import requests
import json

url = 'https://www.alphavantage.co/query?function=TOP_GAINERS_LOSERS&apikey=2RP8A05B6JJ2RP71'
r = requests.get(url)
data = r.json()

riskiest = []

for entry in data["top_gainers"][:5]:
	riskiest.append(entry["ticker"])

for entry in data["top_losers"][:5]:
	riskiest.append(entry["ticker"])

print(riskiest)

ticker_response = requests.get("https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=tesco&apikey"
                               "=2RP8A05B6JJ2RP71").json()

print(ticker_response)

