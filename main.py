import random
import time
from datetime import datetime
import sqlite3
#int var in memory
time_now=datetime.now()
gen_int=random.randint(0,999999999)
alf=20
print("hello---")
#catch eror:
try:
    price_mad=float(input("price by MAD : "))
except ValueError:
    print("---pease input a float price value  not string or anything else...")
    price_mad=200.5

calcul=price_mad*20

print("**MAD TRANSFORM TO ALF == ",calcul)
print()
#save and fetch data from db

conn=sqlite3.connect("prix.db")

corsor=conn.cursor()
corsor.execute(f"INSERT INTO px VALUES('{gen_int}','{calcul}','{time_now}')")
print("***save data complete to prix.db")
print()



conn.commit()
conn.close()

print("***all data in db:")
print()
print(">>>by id-price-date")
print()
from fetch import list_of_prices
print(list_of_prices)
