'''
Write a program to create abstract class with one method.
'''

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Square(Shape):
    def area(self):
        side = 4
        print("Area of Square:", side * side)

obj = Square()
obj.area()
