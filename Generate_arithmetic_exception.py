#Write a program to generate Arithmetic exception and log the exception in system.

num1 = int(input("Enter a number 1: "))
num2 = int(input("Enter a number 2: "))
try:
      num3 = num1 / num2
    print("Result:", num3)
except ZeroDivisionError:
    print("Arithmetic Exception: Cannot divide by zero")

  
