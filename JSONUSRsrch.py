import json
import sqlite3
from gmplot import *
from pprint import pprint

#make the connection to the DB
conn = sqlite3.connect('testdb.sqlite')
cur = conn.cursor()

#Not sure if needed below- Failb v
# cur.execute('SELECT id FROM vehgps')
# rows = cur.fetchall() #forgot i needed this

while True:
    #grab user input :
    user_input = input("Please Enter Bus ID or quit: ")
    if (user_input == 'quit') or len(user_input)<1 : break

    #create the execution of the user ID. Also, this has a break at the else statement fow now. Will probably need to update where that happs, but for now this is where it is
    cur.execute("""SELECT id FROM vehgps WHERE id = ?""", (user_input,))
    user_input = cur.fetchone()
    if user_input is None:
        print('invalid data, please enter vehicle. Invalid Long/Lat')
    else:
        #change the user_input to a string for user's sake
        display_id = str(user_input[0])

        #Create empty list for the mapping needs
        yourlat_list = []
        yourlong_list =[]

        #Display the coordinates from the derived User Input
        print('success')
        cur.execute("""SELECT * FROM vehgps WHERE id = ?""", (display_id,))
        for row in cur.fetchall():
            print(row)
            your_vehid = row[0]
            your_lat = row[1]
            your_long = row[2]

            #appending to the lists
            yourlat_list.append(your_lat)
            yourlong_list.append(your_long)

        print('Your ID: ',your_vehid, '\n', 'your last coordinates are: ',your_lat, your_long)

    #map build now. This would be cooler to feed via a list. I will figure that out in my next project
        print('Would you to see your vehicle(s) on a map? y/n?')
        yn_input = input("enter: ")
        if yn_input == 'y':
            print('YAY')
            print('Creating map...')
            gmap = gmplot.GoogleMapPlotter(41.765800, -72.673400, 18)
            gmap.apikey = "AIzaSyCe-LrwagwKSHcX2MxVTjCFqopOBI8ifIY"
            gmap.scatter(yourlat_list, yourlong_list)
            gmap.draw("/Users/michaelgarcia/Desktop/py4e/Vehicle_map/oneveh.html")
            print('map created. view oneveh.html to view map')
            break
        else:
            print('boo')
            break
