import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="", database="stu")
cur = con.cursor()

rno = int(input("Enter Roll No to Delete: "))

cur.execute("DELETE FROM student WHERE rollno=%s", (rno,))

con.commit()
print("Record Deleted Successfully")

con.close()