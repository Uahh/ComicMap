import json
import sqlite3
from pprint import pprint

conn = sqlite3.connect(r'../data/comic_database.db')

c = conn.cursor()

c.execute('''CREATE TABLE city_points (
             [index]   INTEGER PRIMARY KEY,
             city      STRING  NOT NULL,
             longitude DOUBLE  NOT NULL,
             latitude  DOUBLE  NOT NULL
         );''')

conn.commit()

with open(r'../data/city_point_test_table.json', encoding='utf-8') as json_file:
    table = json.load(json_file)
    json_file.close()
# pprint(table)
for i in range(len(table['cities'])):
    c.execute("INSERT INTO city_points (\"index\",city,longitude,latitude) \
          VALUES (" + str(i) + ", \"" + table['cities'][i][0] + "\", "
              + str(table['cities'][i][1]) + ", " + str(table['cities'][i][2]) + ")")

conn.commit()
conn.close()
