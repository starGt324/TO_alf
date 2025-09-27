import sqlite3
#only fetch data
conn=sqlite3.connect("prix.db")
corsor=conn.cursor()

corsor.execute("select * from px order by price")
list_of_prices=corsor.fetchall()

print(list_of_prices)


conn.commit()
conn.close()
