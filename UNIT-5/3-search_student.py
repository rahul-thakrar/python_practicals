# Definition: Search means finding specific record from table using condition.

import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="", database="stu")
cur = con.cursor()

rno = int(input("Enter Roll No to Search: "))

cur.execute("SELECT * FROM student WHERE rollno=%s", (rno,))
row = cur.fetchone()

if row:
    print("Student Found:", row)
else:
    print("Student Not Found")

con.close()