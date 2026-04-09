# Write a program to do student operations using menu as follows
# a) Add Student
# b) Search Student
# c) List All Students
# e) Delete Student
# f) Exit


students = []

def add_student():
    roll_no = input("Enter Roll No: ")
    name = input("Enter Name: ")
    marks = []

    for i in range(1, 5):
        mark = int(input(f"Enter Mark {i}: "))
        marks.append(mark)

    student = {
        "roll_no": roll_no,
        "name": name,
        "marks": marks
    }

    students.append(student)
    print("Student added successfully!\n")


def search_student():
    roll_no = input("Enter Roll No to search: ")

    for student in students:
        if student["roll_no"] == roll_no:
            print("\nStudent Found:")
            print(f"Roll No: {student['roll_no']}")
            print(f"Name: {student['name']}")
            print(f"Marks: {student['marks']}\n")
            return

    print("Student not found!\n")


def list_students():
    if not students:
        print("No students available!\n")
        return

    print("\nList of Students:")
    print("-" * 40)
    for student in students:
        print(f"Roll No: {student['roll_no']}, Name: {student['name']}, Marks: {student['marks']}")
    print()


def delete_student():
    roll_no = input("Enter Roll No to delete: ")

    for student in students:
        if student["roll_no"] == roll_no:
            students.remove(student)
            print("Student deleted successfully!\n")
            return

    print("Student not found!\n")
while True:
    print("STUDENT MENU")
    print("a) Add Student")
    print("b) Search Student")
    print("c) List All Students")
    print("d) Delete Student")
    print("e) Exit")

    choice = input("Enter your choice: ").lower()

    if choice == 'a':
        add_student()
    elif choice == 'b':
        search_student()
    elif choice == 'c':
        list_students()
    elif choice == 'd':
        delete_student()
    elif choice == 'e':
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.\n")