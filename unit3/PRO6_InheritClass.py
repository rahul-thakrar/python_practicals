'''
Write a Python Program that creates a class and inherit into another class (Base
Class : Student with rollno, name, gender, age) (Derived Class : Course with
coursename, duration, fee)
'''

class Student:
    def __init__(self, rollno, name, gender, age):
        self.rollno = rollno
        self.name = name
        self.gender = gender
        self.age = age

class Course(Student):
    def __init__(self, rollno, name, gender, age, coursename, duration, fee):
        super().__init__(rollno, name, gender, age)
        self.coursename = coursename
        self.duration = duration
        self.fee = fee

    def display(self):
        print(f"Roll No: {self.rollno}")
        print(f"Name: {self.name}")
        print(f"Gender: {self.gender}")
        print(f"Age: {self.age}")
        print(f"Course Name: {self.coursename}")
        print(f"Duration: {self.duration}")
        print(f"Fee: {self.fee}")

# Example usage
student_course = Course(1, "Akshay", "Male", 21, "Python Programming", "3 months", 1500)
student_course.display()
