# Definition: This program dynamically creates a table using user-defined column info.

import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="", database="stu")
cur = con.cursor()

n = int(input("How many columns: "))
cols = []

for i in range(n):
    cname = input("Column Name: ")
    dtype = input("Data Type (varchar/int): ")
    size = input("Size: ")
    cols.append(cname + " " + dtype + "(" + size + ")")

table = input("Enter Table Name: ") 

query = "CREATE TABLE " + table + " (" + ",".join(cols) + ")"
cur.execute(query)

print("Table Created Successfully")

con.close()