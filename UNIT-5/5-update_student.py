
import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="", database="stu")
cur = con.cursor()

rno = int(input("Enter Roll No to Update: "))
city = input("Enter New City: ")

cur.execute("UPDATE student SET city=%s WHERE rollno=%s", (city, rno))

con.commit()
print("Record Updated Successfully")

con.close()