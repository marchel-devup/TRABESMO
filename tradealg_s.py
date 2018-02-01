#!/bin/python3
import sqlite3
import time
import json
DBconf = 'db.conf'
DBname = open(DBconf).readline().strip()


HISTORY = 1800#30 min epoch
wall = 'wallet'

def getCurrency(pair, act, period=0):
	if period == 0:string = "select  %s_price,updated from TICKER where pair='%s' limit 1"%(act,pair)
	else: string = "select sell_price,updated from TICKER where pair='BTC_USD' AND updated>%s;"%(time.time()-period*60)
	conn = sqlite3.connect(DBname)
	c = conn.cursor()
	c.execute(string)
	res = c.fetchall()
	conn.commit()
	conn.close()
	return res
def wallet(pair, act, wall):
	fwall = open(wall)
	json.loads(fwall)
	fwall.close()
result = getCurrency("BTC_USD","buy",30)
first = float(result[0][0])
last = float(result[-1][0])
deff = last-first
if deff >= 0:print ("%s -> %s GROWS UP TO %s USD or %s perc."%(first,last,deff,(deff/last*100)))
else: print ("%s -> %s FALL DOWN TO %s USD or %s perc."%(first,last,deff,(deff/last*-100)))