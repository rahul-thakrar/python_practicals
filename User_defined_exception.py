#Write a program to execute user defined exception in python.

class MyException(Exception):
    pass
num1 = int(input("Enter a number 1: "))
num2 = int(input("Enter a number 2: "))
try:
    if (num2 == 0):
        raise MyException
    else  :
        divison = num1/num2
        print("Answer is : ",divison)
except MyException:
        print("Can not divide with zero")
