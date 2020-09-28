"""In this file - preliminary information is added to the databases
so they are not fully empty and it would be possible to work with them
straight out of the box and then subsequently add more data through the
created api functions"""

import sqlite3
import json
conn = sqlite3.connect("backend/database/recommendations.db")
c = conn.cursor()

# Load the initial data not to polute the .py file all together
with open("backend/database/preliminary_data.json") as json_file:
    data = json.load(json_file)

# Inser few games and movies into our databases. To make it more simple, organize first the information
for entry in data:
    c.execute(f"INSERT INTO {entry['database']} VALUES (:name, :description, :year, :img, :consumed)", 
    {'name': entry['name'], 'description': entry['description'], 'year': entry['year'], 'img': entry['img'], 'consumed': entry['consumed']})
    conn.commit()

conn.close()