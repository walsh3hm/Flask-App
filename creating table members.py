import sqlite3
conn = sqlite3.connect("celebrities.db")
cursor = conn.cursor()
sql = "create table members(memberID integer PRIMARY KEY, firstname text, lastname text, age int, email text, bio text)"
cursor.execute(sql)
conn.commit()
conn.close()
