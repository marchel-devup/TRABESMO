#!/bin/python3
import sqlite3
import time
import config

HISTORY = 1800#30 min epoch

conn = sqlite3.connect(config.db_file)
c = conn.cursor()
delta = time.time()-HISTORY
string = "select sell_price from TICKER where pair='BTC_USD' AND updated>%s;"%delta
c.execute(string)
result = c.fetchall()
for line in result: print (line)
deff = float(result[0][0])-float(result[-1][0]) 
if deff >= 0:print ("GROWS UP TO %s USD"%deff)
else: print ("FALL DOWN TO %s USD"%deff)
#print (int(result))
conn.commit()
conn.close()

