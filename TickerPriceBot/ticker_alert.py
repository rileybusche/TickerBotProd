#!/usr/bin/env python3
import requests
import json

api_key = open("api_key.txt", "r").read()
hook_url = open("hook_url.txt", "r").read()

# Posts to Discord
def postToDiscord(message):
    params = {
        "content" : message,
        "username" : "Ticker Alert"
    }

    post = requests.post(hook_url, params)    

    print(post)

# Make API Call For Stock Ticker
def callStockAPI(ticker, mode):
    results = ""
    ticker_list = []

    if mode == "single":
        ticker_list.append(ticker)
        try:
            response = requests.get(f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={ticker}&apikey={api_key}')
            response_json = response.json()
            print(response)
            print(response_json)
            price = float(response_json["Global Quote"]["05. price"])
            results += f"The Price of {ticker} is: ${price:.2f}"
        except:
            results += f"There was no price information for {ticker}."

    elif mode == "all":
        ticker_list = [line.rstrip('\n') for line in open('tickers.txt')]
    
        # Alphavantage
        for ticker in ticker_list:    
            try:
                response = requests.get(f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={ticker}&apikey={api_key}')
                response_json = response.json()
                print(response)
                print(response_json)
                price = float(response_json["Global Quote"]["05. price"])
                results += f"The Price of {ticker} is: ${price:.2f}.\nNow tracking {ticker}"
            except:
                results += f"There was no price information for {ticker}.\nDid not add {ticker}."

    print(results)
    
    return results

# Make API Call For Crypto Ticker
def callCryptoAPI(crypto, mode):
    results = ""
    crypto_list = []

    if mode == "single":
        crypto_list.append(crypto)
        try:
            print(crypto_list)
            response = requests.get(f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={crypto}&to_currency=USD&apikey={api_key}")
            response_json = response.json()
            print(response)
            print(response_json)
            price = float(response_json["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
            results += f"The Price of {crypto} is: ${price:.2f}"
        except:
            results += f"There was no price information for {crypto}.\nDid not add {crypto}."

    elif mode == "all":
        crypto_list = [line.rstrip('\n') for line in open('cryptos.txt')]
    
        # Alphavantage
        for crypto in crypto_list:    
            try:
                response = requests.get(f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={crypto}&to_currency=USD&apikey={api_key}")
                response_json = response.json()
                print(response)
                print(response_json)
                price = float(response_json["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
                results += f"The Price of {crypto} is: ${price:.2f}\n"
            except:
                results += f"There was no price information for {crypto}."

    # Converting List to Single stream for output
    
    print(results)
    
    return results



