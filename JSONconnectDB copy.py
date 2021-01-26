import json
import sqlite3
from pprint import pprint

#make the connection to the DB
conn = sqlite3.connect('testdb.sqlite')
cur = conn.cursor()

#present data in the console. Not sure where to go from here but want to make this connection first
cur.execute('SELECT * FROM vehgps')
rows = cur.fetchall() #forgot i needed this

#iterate rows from the select statement above
for row in rows:
    #print(row)
    print("id = ", row[0], )

#commit and close the db. I actually do not think i need the commit code.
conn.commit()
conn.close()
