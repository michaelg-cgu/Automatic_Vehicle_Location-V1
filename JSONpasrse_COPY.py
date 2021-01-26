import json
import sqlite3
from pprint import pprint
from io import StringIO

#Public API:
#import requests
#trans_data = requests.get('url of jSON')
#set a variable to trans data to load:
#veh_position = trans_data.json()[1]

#creating the SQL connection
# conn = sqlite3.connect('testdb.sqlite')
# cur = conn.cursor()

#currently set up so that each test, needs to physically delete DB in the value holder
# cur.execute('''
#             CREATE TABLE IF NOT EXISTS vehgps (id text,
#             trip_update text,
#             vehicle text
#              )''')

with open('vehiclepositions.json') as f:
    #load the json and store in a variable called data
    data = json.load(f)
    pprint(data)

    #identify the structure. This may not be necessary for future as JSON is in a nice format. But for my own understanding of the JSON, this was pivotal
    the_id = data['entity'][0]['id']
    v_lat = data['entity'][0]['vehicle']['position']['latitude']
    print(the_id)
    print(v_lat)

    the_data = json.dumps(f)
    print(the_data)


    #TEST test loop, create a for loop on top branch id, and attempt to insert into DB.
#     for vehid in data:
#         cur.execute('INSERT INTO vehgps VALUES (?, ?, ?)', [vehid['id'], vehid['trip_update'], vehid['vehicle']])
#         conn.commit()
#
# conn.close()
