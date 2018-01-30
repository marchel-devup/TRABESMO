#!/bin/python3
import requests
import sqlite3
import json
PAIRS = ["BTC_USD", "ETH_USD"]
DB_FILE = 'trade.db'
curs = requests.post('https://api.exmo.me/v1/ticker/')
if(curs.status_code != 200):
	print("Error! Code :" + str(curs.status_code))
for pair in PAIRS:
	res = json.loads(curs.text)[pair]
	conn = sqlite3.connect(DB_FILE)
	c = conn.cursor()
	string = "INSERT INTO TICKER VALUES('%s',%s,%s,%s)"%(pair,
	res['buy_price'] ,res['sell_price'], res['updated'])
	c.execute(string)
	conn.commit()
	#results = c.fetchall()
	print(results)
	conn.close()
