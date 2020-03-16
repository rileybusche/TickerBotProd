#!/usr/bin/env python3
import requests
import json
import pprint

import delta

pp = pprint.PrettyPrinter(indent=4)

# api_key = open('api_key.txt', 'r').read().strip()

with open('/home/ec2-user/creds/creds.json') as file:
    creds = json.load(file)

api_key = creds['Credentials']['Ticker Bot']['API Key']

def stock_price(ticker, frequency, output_size):
    # call = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={ticker}&apikey={api_key}'
    # Intraday
    call = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&interval={frequency}&outputsize={output_size}&apikey={api_key}'
    response = requests.get(call)

    json_response = response.json()
    time_series = json_response[f'Time Series ({frequency})']

    ticker_delta = delta.ticker_delta(time_series)

    return json_response[f'Time Series ({frequency})']

def crypto_price(ticker, frequency):
    call = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={ticker}&to_currency=USD&apikey={api_key}'
    response = requests.get(call)
    
    json_response = response.json()
    print(json_response)

    return json_response