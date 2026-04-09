# Definition: Menu program is used to perform multiple database operations in one program.

import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="", database="stu")
cur = con.cursor()

while True:
    print("\n1.Insert  2.Update  3.Search  4.Delete  5.List  6.Exit")
    ch = int(input("Enter Choice: "))

    if ch == 1:
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
        print("Inserted Successfully")

    elif ch == 2:
        rno = int(input("Roll No: "))
        city = input("New City: ")
        cur.execute("UPDATE student SET city=%s WHERE rollno=%s", (city, rno))
        con.commit()
        print("Updated Successfully")

    elif ch == 3:
        rno = int(input("Roll No: "))
        cur.execute("SELECT * FROM student WHERE rollno=%s", (rno,))
        row = cur.fetchone()
        if row:
            print(row)
        else:
            print("Not Found")

    elif ch == 4:
        rno = int(input("Roll No: "))
        cur.execute("DELETE FROM student WHERE rollno=%s", (rno,))
        con.commit()
        print("Deleted Successfully")

    elif ch == 5:
        cur.execute("SELECT * FROM student")
        rows = cur.fetchall()
        for r in rows:
            print(r)

    elif ch == 6:
        break

    else:
        print("Invalid Choice")

con.close()