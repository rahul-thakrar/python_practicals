# Write a program to input 2 numbers and one arithmetic operator. Perform operations as per arithmetic operator which is given as input.

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
op = input("Enter arithmetic operator (+, -, *, /): ")

if op == '+':
    print("Sum is:", num1 + num2)

elif op == '-':
    print("Subtraction is:", num1 - num2)

elif op == '*':
    print("Multiplication is:", num1 * num2)

elif op == '/':
    if num2 != 0:
        print("Division is:", num1 / num2)
    else:
        print("Error: Division by zero")

else:
    print("Invalid operator")