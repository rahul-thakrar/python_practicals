'''
Write a program to do student operations using menu as follows
a) Add Student
b) Search Student
c) List All Students
d) Update Student
e) Delete Student
f) Exit
'''
students = {}

while True:
    print("1 Add")
    print("2 Search")
    print("3 List")
    print("4 Update")
    print("5 Delete")
    print("6 Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        r = input("Roll: ")
        n = input("Name: ")
        students[r] = n

    elif ch == 2:
        r = input("Roll: ")
        print(students.get(r,"Not found"))

    elif ch == 3:
        for i in students:
            print(i,students[i])

    elif ch == 4:
        r = input("Roll: ")
        n = input("New Name: ")
        students[r] = n

    elif ch == 5:
        r = input("Roll: ")
        students.pop(r,None)

    elif ch == 6:
        break
