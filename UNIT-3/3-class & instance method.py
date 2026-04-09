# Write a program to make use of class method and instance method.

class Student:
    school_name = "ABC School"   # Class variable

    def __init__(self, name, marks):
        self.name = name        # Instance variable
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

    @classmethod
    def show_school(cls):
        print("School Name:", cls.school_name)


s1 = Student("Keval", 85)
s2 = Student("Rahul", 92)

s1.display()
s2.display()

Student.show_school()