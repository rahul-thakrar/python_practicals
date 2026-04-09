import mysql.connector
import re

con = mysql.connector.connect(host="localhost", user="root", password="", database="stu")
cur = con.cursor()

cur.execute("SELECT * FROM student")
rows = cur.fetchall()

pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

for r in rows:
    email = r[4]
    if re.match(pattern, email):
        print(r)

con.close()