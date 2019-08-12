import requests
import json

api_key = open('api_key.txt', 'r').read()
hook_url = open('hook_url.txt', 'r').read()

# Posts to Discord
def postToDiscord(message):
    params = {
        "content" : message,
        "username" : "Ticker Alert"
    }

    post = requests.post(hook_url, params)    


def callCryptoAPI():
    # BTC
    response = requests.get(f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey={api_key}")
    response_json = response.json()
    price_BTC = float(response_json["Realtime Currency Exchange Rate"]["5. Exchange Rate"])

    # ETH
    response = requests.get(f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=ETH&to_currency=USD&apikey={api_key}")
    response_json = response.json()
    price_ETH = float(response_json["Realtime Currency Exchange Rate"]["5. Exchange Rate"])

    message = f"```fix\nBTC: {price_BTC}\nETH: {price_ETH}```"

callCryptoAPI()