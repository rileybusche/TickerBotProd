#!/usr/bin/env python3
import requests
import json

api_key = open('api_key.txt', 'r').read().strip()

def crypto_price(ticker):
    try:
        response = requests.get(f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={ticker}&apikey={api_key}')
        json_response = response.json()