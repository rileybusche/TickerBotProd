#! /bin/bash
sudo apt-get update
sudo apt install python3-pip -y
python3 -m pip install -U discord.py
python3 -m pip install apscheduler

# Git clone
mkdir TickerBot
cd TickerBot/
git init
git clone https://github.com/rileybusche/TickerAlert.git
cd TickerPriceBot
touch api_key.txt
touch token.txt