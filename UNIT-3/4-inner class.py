#Write a program to make use of inner class.

class Outer:
    def __init__(self):
        print("Outer class constructor")

    class Inner:
        def __init__(self):
            print("Inner class constructor")

        def display(self):
            print("This is a method inside the Inner class")

outer_obj = Outer()
inner_obj = outer_obj.Inner()
inner_obj.display()