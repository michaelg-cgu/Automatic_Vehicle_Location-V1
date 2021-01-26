#This program takes data a json file and inserts specific content into a sqlite DB. As of 9/4, running the code more than once produces duplicate data. The goal is to have the data eventually update every 15 minutes. This should fix this 'issue' of duplicate data but I should still enter code to perform sanitation test. Perhaps on the time
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
conn = sqlite3.connect('testdb.sqlite')
cur = conn.cursor()

#currently set up so that each test, needs to physically delete DB in the value holder
cur.execute('''
            CREATE TABLE IF NOT EXISTS vehgps (id text,
            latitude INTEGER, longitude INTEGER)''')

with open('vehiclepositions.json') as f:
    #load the json and store in a variable called data
    data = json.load(f)

pprint(data)

#identify the structure. This may not be necessary for future as JSON is in a nice format. But for my own understanding of the JSON, this was pivotal
the_id = data['entity'][0]['id']
v_lat = data['entity'][0]['vehicle']['position']['latitude']
print(the_id)
print(v_lat)
print(type(data))
print(type(data['entity']))

#new test codes. This grabes each element from the json data. If the element has more than one value, the type is dict. This means that position - vehicle/position is a dictionary class.
for vehicle in data['entity']:
    print(vehicle['id'])

    #print(vehicle['vehicle'])
    # print(vehicle['vehicle']['position'])
    # print(vehicle['vehicle']['timestamp'])
    # print(vehicle['vehicle']['trip'])
    # print(vehicle['vehicle']['vehicle'])
    #x = vehicle['id']
    cur.execute('INSERT INTO vehgps (id, latitude, longitude) VALUES (?, ?, ?)', (vehicle['id'], vehicle['vehicle']['position']['latitude'], vehicle['vehicle']['position']['longitude']))
print(type(vehicle['id']))



#TEST of DUMP INTO A NEW FILE. This works:
# for the_alert in data['entity']:
#     del the_alert['alert']
# with open('sometesting.json', 'w') as d:
#     json.dump(data, d)


conn.commit()
conn.close()
