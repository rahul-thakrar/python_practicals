# Use appropriate functions for each classWrite a program to display \. Multiple inheritance can be done as per your choice.

class A:
    def showA(self):
        print("Class A")

class B:
    def showB(self):
        print("Class B")

class C(A, B):   
    def showC(self):
        print("Class C")

obj = C()

obj.showA()
obj.showB()
obj.showC()


print("MRO:", C.mro())