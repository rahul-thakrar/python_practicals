# Write a program to read file which has marks entry of student and display details with total, percentage and grade (Consider a file which has 
# comma separated data with RollNo, Student Name, Mark1, Mark2, Mark3 and Mark4).


def calculate_grade(percentage):
    if percentage >= 90:
        return 'A'
    elif percentage >= 75:
        return 'B'
    elif percentage >= 60:
        return 'C'
    elif percentage >= 50:
        return 'D'
    else:
        return 'F'

def process_student_file(filename):
    try:
        with open(filename, 'r') as file:
            print("RollNo\tName\t\tTotal\tPercentage\tGrade")
            print("-" * 60)

            for line in file:
                data = line.strip().split(',')

                roll_no = data[0]
                name = data[1]
                marks = list(map(int, data[2:]))

                total = sum(marks)
                percentage = total / len(marks)

                grade = calculate_grade(percentage)

                print(f"{roll_no}\t{name}\t{total}\t{percentage:.2f}\t\t{grade}")

    except FileNotFoundError:
        print("File not found!")

# Call the function
process_student_file("8.1-students.txt")