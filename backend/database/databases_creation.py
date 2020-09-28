"""The database with all of the information is a static file
Ran with sqlite"""
import sqlite3

# Connect to the database and create navigation cursor
conn = sqlite3.connect("backend/database/recommendations.db")
c = conn.cursor()

# Generate tables (games, movies) for information storing
"""
name - name of the product
description - description of the product
year - year when the product was released
img - url link to the image of the product
consumed - 1 or 0 state of whether the product has been already enjoyed by the user or not
"""
c.execute("""CREATE TABLE Games (
            name text PRIMARY KEY,
            description text,
            year integer,
            img text,
            consumed integer   
        )""")

c.execute("""CREATE TABLE Movies (
            name text PRIMARY KEY,
            description text,
            year integer,
            img text,
            consumed integer
)""")

# Commit the current transaction that creates tables and close the connection
conn.commit()
conn.close()