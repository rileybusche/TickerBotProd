#! /bin/bash
sudo apt-get update
sudo apt install python3-pip -y
python3 -m pip install -U discord.py
python3 -m pip install apscheduler

# Git clone
mkdir TickerBot
git clone https://github.com/rileybusche/TickerBotProd.git
cd TickerBotProd/TickerPriceBot/
touch api_key.txt
touch token.txt