#!/usr/bin/env python3
import requests
import json

# api_key = open('api_key.txt', 'r').read().strip()

with open('/home/ec2-user/creds/creds.json') as file:
    creds = json.load(file)

api_key = creds['Credentials']['Ticker Bot']['API Key']

def stock_price(ticker):
    call = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={ticker}&apikey={api_key}'
    response = requests.get(call)
    json_response = response.json()
    print(json_response)

    return json_response

def crypto_price(ticker):
    call = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={ticker}&to_currency=USD&apikey={api_key}'
    response = requests.get(call)
    
    json_response = response.json()
    print(json_response)

    return json_response