# Calculates Percentage Change of Ticker for the day
import datetime

def ticker_delta(price_data):
    date = datetime.datetime.now()

    market_time_open = f'{date.year}-{date.month}-{date.day} 09:31:00'

    hour = date.hour + 1
    if hour < 10:
        hour = f'0{str(hour)}'

    market_time_now = f'{date.year}-{date.month}-{date.day} {hour}:{date.minute}:00'

    market_price_open = float([market_time_open]['1. open'])
    market_price_now = float([market_time_now]['4. close'])

    delta = market_price_now - market_price_open

    print(delta)

    return str(delta)