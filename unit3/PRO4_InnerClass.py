# Write a program to make use of inner class

class Bhogayata:
    def __init__(self):
        print("This is the Outer Class: Bhogayata")
    
    class Akshay:
        def greet(self):
            print("Hello from the Inner Class: Akshay")

outer_obj = Bhogayata()
inner_obj = outer_obj.Akshay()
inner_obj.greet()
