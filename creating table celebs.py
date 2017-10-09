import sqlite3
conn = sqlite3.connect("celebrities.db")
cursor = conn.cursor()
sql = "create table celebs(celebID integer PRIMARY KEY, firstname text, lastname text, age int, email text, photo text, bio text)"
cursor.execute(sql)
conn.commit()
conn.close()
