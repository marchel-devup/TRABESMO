#!/bin/python3
import requests
import sqlite3
import json
import config


curs = requests.post('https://api.exmo.me/v1/ticker/')
if(curs.status_code != 200):
	print("Error! Code :" + str(curs.status_code))
for pair in config.pairs:
	res = json.loads(curs.text)[pair]
	conn = sqlite3.connect(config.db_file)
	c = conn.cursor()
	string = "INSERT INTO TICKER VALUES('%s',%s,%s,%s)"%(pair,
	res['buy_price'] ,res['sell_price'], res['updated'])
	c.execute(string)
	conn.commit()
	conn.close()
