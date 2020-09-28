import sqlite3
conn = sqlite3.connect("backend/database/recommendations.db")
c = conn.cursor()

c.execute("SELECT * FROM Movies")
print(c.fetchone())
conn.commit()
conn.close()