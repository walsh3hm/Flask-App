import sqlite3
conn = sqlite3.connect("celebrities.db")
cursor = conn.cursor()
sql = "insert into members values (?,?,?,?,?,?)"
data = ( (1, "Hannah", "Walsh", 21, "walsh3hm@dukes.jmu.edu", "She was born in Boston, MA and was raised in Midlothian, VA. She currently is a junior at JMU. Her major is ISAT and concentration is IKM."), (2, "Kiva", "Gayle", 20, "gaylekn@dukes.jmu.edu", "She lives in Northern Virginia, in Centreville. She is junior at JMU. Her major is ISAT and concentration is Telecom and IKM. She enjoys building drones in her free time.") )
cursor.executemany(sql, data)
conn.commit()
conn.close()
