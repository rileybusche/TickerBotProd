# Calculates Percentage Change of Ticker for the day
import datetime

def ticker_delta(price_data):
    date = datetime.datetime.now()

    hour = date.hour + 1
    day = date.day
    month = date.month

    if hour < 10:
        hour = f'0{str(hour)}'
    if day < 10:
        day = f'0{str(day)}'
    if month < 10:
        month = f'0{str(month)}'

    
    market_time_open = f'{date.year}-{month}-{day} 09:31:00'
    market_time_now = f'{date.year}-{month}-{day} {hour}:{date.minute}:00'

    market_price_open = float(price_data[market_time_open]['1. open'])
    market_price_now = float(price_data[market_time_now]['4. close'])

    delta = market_price_now - market_price_open

    print(delta)

    return str(delta)