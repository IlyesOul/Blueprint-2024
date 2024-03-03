import requests

response_json = requests.get("https://financialmodelingprep.com/api/v3/stock_market/gainers?apikey=660b686a5741c3a14db31b0f2dc9ce41").json()

top_7_winners = response_json[:7]
print(top_7_winners)

response_json = requests.get("https://financialmodelingprep.com/api/v3/stock_market/losers?apikey=660b686a5741c3a14db31b0f2dc9ce41").json()

top_7_losers = response_json[len(response_json)-7:]
print(top_7_losers)

print(top_7_losers[0]["name"])
