import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="", database="stu")
cur = con.cursor()

cur.execute("SELECT * FROM student")
rows = cur.fetchall()

for r in rows:
    name = r[1]
    if name.startswith("N") and len(name) == 5:
        print(r)

con.close()