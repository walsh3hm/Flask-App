import sqlite3
conn = sqlite3.connect("celebrities.db")
cursor = conn.cursor()
sql = "select * from members"
cursor.execute(sql)
rows = cursor.fetchall()
for row in rows:
    print (row)
conn.close()
