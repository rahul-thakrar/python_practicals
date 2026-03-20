'''
Use appropriate functions for each classWrite a program to display MRO using
multiple inheritance. Multiple inheritance can be done as per your choice.
'''

class A:
    def show(self):
        print("Class A")
class B(A):
    def show(self):
        print("Class B")
class C(A):
    def show(self):
        print("Class C")
class D(B, C):
    pass
obj = D()
print("MRO of class D:")
for i in D.mro():
    print(i)
