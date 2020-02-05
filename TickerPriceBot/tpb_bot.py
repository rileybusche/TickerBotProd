#!/usr/bin/env python3

from discord.ext import commands
from apscheduler.schedulers.blocking import BlockingScheduler
import discord
import json
import os
import asyncio

import helpers.api_helper as api_helper
import helpers.discord_logging as log
import helpers.graph as graph

# client = discord.Client()
bot = commands.Bot(command_prefix='!')
# token = open("token.txt", "r").read().strip()
frequency = '5min'

with open('/home/ec2-user/creds/creds.json') as file:
    creds = json.load(file)

token = creds['Credentials']['Ticker Bot']['Token']

# Scheduler for output of ticker info
sched = BlockingScheduler()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def stock(ctx, ticker: str):
    json_response = api_helper.stock_price(ticker, frequency)
    # log.write_log(json_response, bot)

    for time in json_response:
        price = float(json_response[time]['4. close'])
        print(price)
        break
    
    file_path = graph.create_graph(json_response, ticker, frequency)
    await ctx.send(file=discord.File(file_path))

    os.system('rm image.jpg')

    try:
        if price < 0.01:
            message = f'```fix\n{ticker}: ${price}```'
        else:
            message = f'```fix\n{ticker}: ${price:.2f}```'
    except:
        message = '```\nCould not get a value. Please check the ticker and try again shortly.```'

    await ctx.send(message)

@bot.command()
async def crypto(ctx, ticker: str):
    json_respons = api_helper.crypto_price(ticker, frequency)
    # log.write_log(json_response, bot)
    try:
        price = float(json_respons["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
        if price < 0.01:
            message = f'```fix\n{ticker}: ${price}```'
        else:
            message = f'```fix\n{ticker}: ${price:.2f}```'
        
    except:
        message = '```\nCould not get a value. Please check the ticker and try again shortly.```'
    
    await ctx.send(message)

@bot.command()
async def bot_quit(ctx):
    await bot.close()

# client.run(token)
bot.run(token)


# # Outputs price of ticker
# @bot.command()
# async def Price_Stock(ctx, ticker: str):
#     await ctx.send("```fix\n" + ticker_alert.callStockAPI(ticker, "single") + "```")

# # Outputs price of ticker
# @bot.command()
# async def Price_Crypto(ctx, crypto: str):
#     await ctx.send("```fix\n" + ticker_alert.callCryptoAPI(crypto, "single") + "```")

# # Lists price for all tracked tickers
# @bot.command()
# async def All_Stocks(ctx):
#     await ctx.send(f"```fix\nAll Tracked Tickers:\n" + ticker_alert.callStockAPI("null", "all") + "```")

# # Lists price for all tracked cryptos
# @bot.command()
# async def All_Cryptos(ctx):
#     await ctx.send(f"```fix\nAll Tracked Cryptos:\n" + ticker_alert.callCryptoAPI("null", "all") + "```" )

# # Add to list of tracked tickers (tickers.txt)
# @bot.command()
# async def Add_Stock(ctx, ticker):
#     # API call to try and receive a price, if error, not a valid ticker.
#     try:
#         crypto_price = ticker_alert.callCryptoAPI(ticker, "single")
#     except:
#         await ctx.send(f"{ticker} is not a valid crypto ticker.")
#         return

#     # Checking if File Exists
#     if os.path.exists("tickers.txt"):
#         ticker_list_contents = ticker_list = [line.rstrip('\n') for line in open('tickers.txt')]
#         for check_ticker in ticker_list_contents:
#             if ticker.lower() == check_ticker.lower():
#                 # Ticker already in list
#                 await ctx.send(f"```fix\n{ticker} already tracked. \n" + ticker_alert.callStockAPI(ticker, "single") + "```")
#                 return
#             else:
#                 # Ticker not in list
#                 ticker_file = open('tickers.txt', 'a')
#                 ticker_file.write(ticker + "\n")
#                 await ctx.send(f"```fix\nCheckingcle {ticker} \n" + ticker_alert.callStockAPI(ticker, "single") + "```")
#                 return

#     else:
#         ticker_file = open('tickers.txt', 'w')
#         ticker_file.write(ticker + "\n")
#         await ctx.send(f"```fix\nChecking {ticker} \n" + ticker_alert.callStockAPI(ticker, "single") + "```")
        

# # Add to list of tracked cryptos (cryptos.txt)
# @bot.command()
# async def Add_Crypto(ctx, crypto):
#     # API call to try and receive a price, if error, not a valid crypto.
#     try:
#         crypto_price = ticker_alert.callCryptoAPI(crypto, "single")
#     except:
#         await ctx.send(f"{crypto} is not a valid crypto currency.")
#         return

#     # Make a "doesExist()"
#     if os.path.exists("cryptos.txt"):
#         crypto_list_contents = crypto_list = [line.rstrip('\n') for line in open('cryptos.txt')]
#         for check_crypto in crypto_list_contents:
#             if crypto.lower() == check_crypto.lower():
#                 # Crypto already in list
#                 await ctx.send(f"```fix\n{crypto} already tracked. \n" + ticker_alert.callCryptoAPI(crypto, "single") + "```")
#                 return
#             else:
#                 # Crypto not in list
#                 crypto_file = open('cryptos.txt', 'a')
#                 crypto_file.write(crypto + "\n")
#                 await ctx.send(f"```fix\nAdding {crypto} \n" + ticker_alert.callCryptoAPI(crypto, "single") + "```")

#     else:
#         # Crypto not in list
#         crypto_file = open('cryptos.txt', 'w')
#         crypto_file.write(crypto + "\n")
#         await ctx.send(f"```fix\nAdding {crypto} \n" + ticker_alert.callCryptoAPI(crypto, "single") + "```")

# # Remove 
# @bot.command()
# async def Remove(ctx, ticker):
#     await ctx.send("This command isn't implemented yet.")

# # Clears all tickers
# @bot.command()
# async def Clear_All(ctx):
#     await ctx.send("This command isn't implemented yet.")

# # Lists all tracked tickers (tickers.txt)
# @bot.command()
# async def List_Stocks(ctx):
#     ticker_list_contents = ticker_list = [line.rstrip('\n') for line in open('tickers.txt')]
#     message = ""
#     for ticker in ticker_list:
#         message += (str(ticker) + "\n")
#     await ctx.send(f"```fix\nTracked tickers: \n{message}```")

# # Lists all tracked cryptos (cryptos.txt)
# @bot.command()
# async def List_Cryptos(ctx):
#     crypto_list_contents = crypto_list = [line.rstrip('\n') for line in open('cryptos.txt')]
#     message = ""
#     for crypto in crypto_list:
#         message += (str(crypto) + "\n")
#     await ctx.send(f"```fix\nTracked cryptos: \n{message}```")

# # Setting frequency for All() to be run
# @bot.command()
# async def Set_Timer(ctx, time):
#     if time == "1":
#         await ctx.send(f"Listing info for ticker(s) every minute.")
#         await sched.add_job(All(), 'cron', minute = '*')
#     elif time == "5":
#         await ctx.send(f"Listing info for ticker(s) every {time} minutes.")
#         await sched.add_job(All(), 'cron', minute = '*/5')
#     elif time == "10":
#         await ctx.send(f"Listing info for ticker(s) every {time} minutes.")
#         await sched.add_job(All(), 'cron', minute = '*/10')
#     elif time == "15":
#         await ctx.send(f"Listing info for ticker(s) every {time} minutes.")
#         await sched.add_job(All(), 'cron', minute = '*/15')
#     elif time == "30":
#         await ctx.send(f"Listing info for ticker(s) every {time} minutes.")
#         await sched.add_job(All(), 'cron', minute = '*/30')
#     elif time == "60":
#         await ctx.send(f"Listing info for ticker(s) every hour.")
#         await sched.add_job(All(), 'cron', hour = '*')
#     else:
#         await ctx.send(f"{time} is not a valid input.")

# @bot.command()
# async def Graph(ctx):
#     await ctx.send("This command isn't implemented yet")

