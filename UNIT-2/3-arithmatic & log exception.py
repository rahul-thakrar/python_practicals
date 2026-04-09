#  Write a program to generate arithmetic exception and log the exception in system.


try:
    result = 50 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

