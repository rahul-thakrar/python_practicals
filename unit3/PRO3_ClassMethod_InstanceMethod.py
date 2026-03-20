#Write a program to make use of class method and instance method.

class Demo:
    def instance_method(self):
        print("This is Instance Method")

    @classmethod
    def class_method(cls):
        print("This is Class Method")

obj = Demo()
obj.instance_method()   
Demo.class_method()     
