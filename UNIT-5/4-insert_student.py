
import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="", database="stu")
cur = con.cursor()

rollno = int(input("Roll No: "))
name = input("Name: ")
gender = input("Gender: ")
age = int(input("Age: "))
email = input("Email: ")
mobile = input("Mobile: ")
city = input("City: ")

cur.execute("INSERT INTO student VALUES(%s,%s,%s,%s,%s,%s,%s)",
            (rollno, name, gender, age, email, mobile, city))

con.commit()
print("Record Inserted Successfully")

con.close()