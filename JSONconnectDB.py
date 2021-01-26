import json
import sqlite3
from gmplot import *
from pprint import pprint

#make the connection to the DB
conn = sqlite3.connect('testdb.sqlite')
cur = conn.cursor()

#present data in the console. Not sure where to go from here but want to make this connection first
cur.execute('SELECT * FROM vehgps')
rows = cur.fetchall() #forgot i needed this

#Create empty lists to be used in mapping
list1 = []
lat_list = []
long_list = []
#iterate rows from the select statement above
for row in rows:
    #print(row)
    #print("id = ", row[0], )
    the_id = row[0]
    the_lat = row[1]
    the_long = row[2]
    #New try: Set variables to empty list
    list1.append(the_id)
    lat_list.append(the_lat)
    long_list.append(the_long)
#print(list1)

#Create a list from the DB and store in a variable
#this was done within connection. should be necessary
# latitude_list = ('SELECT latitude FROM vehgps')
# longitude_list = ('SELECT longitude FROM vehgps')
#the above needs to be appended to a list

#commit and close the db. I actually do not think i need the commit code.
conn.commit()
conn.close()

#create the Standard Map. Try #2
gmap = gmplot.GoogleMapPlotter(41.765800, -72.673400, 18)
gmap.apikey = "AIzaSyCe-LrwagwKSHcX2MxVTjCFqopOBI8ifIY"
gmap.scatter(lat_list, long_list)
gmap.draw("/Users/michaelgarcia/Desktop/py4e/Vehicle_map/maptest.html")
