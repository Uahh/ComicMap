import json
import sqlite3
from pprint import pprint

conn = sqlite3.connect(r'../data/comic_database.db')

c = conn.cursor()

# c.execute('''CREATE TABLE city_points (
#              [index]   INTEGER PRIMARY KEY,
#              value     INTEGER NOT NULL,
#              city      STRING  NOT NULL,
#              province  STRING  NOT NULL,
#              longitude DOUBLE  NOT NULL,
#              latitude  DOUBLE  NOT NULL
#          );''')
#

# c.execute('''CREATE TABLE province (
#     name  STRING  PRIMARY KEY,
#     value INTEGER NOT NULL
# );
# ''')
# conn.commit()

# with open(r'../data/city_table.json', encoding='utf-8') as json_file:
#     table = json.load(json_file)
#     json_file.close()
#
# for i in range(len(table['cities'])):
#     # print("INSERT INTO city (\"index\", value, city, province, longitude, latitude) \
#     #       VALUES (" + str(i) + ", 0, \"" + table['cities'][i][0] + "\", \"" + str(table['cities'][i][5]) + "\", " +
#     #           str(table['cities'][i][1]) + ", " + str(table['cities'][i][2]) + ")")
#     c.execute("INSERT INTO city (\"index\", value, city, province, longitude, latitude) \
#           VALUES (" + str(i) + ", 0, \"" + table['cities'][i][0] + "\", \"" + str(table['cities'][i][5]) + "\", " +
#               str(table['cities'][i][1]) + ", " + str(table['cities'][i][2]) + ")")

with open(r'../data/province_table.json', encoding='utf-8') as json_file:
    table = json.load(json_file)
    json_file.close()

for i in range(len(table['provinces'])):
    print("INSERT INTO province (name, value) \
          VALUES (\"" + table['provinces'][i]['name'] + "\", 0)")
    c.execute("INSERT INTO province (name, value) \
              VALUES (\"" + table['provinces'][i]['name'] + "\", 0)")

conn.commit()
conn.close()
