
import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="", database="stu")
cur = con.cursor()

cur.execute("SELECT * FROM student")
rows = cur.fetchall()

for r in rows:
    print(r)

con.close()