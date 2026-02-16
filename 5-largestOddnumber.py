# Write a program to enter 10 numbers and display largest odd number from the entered number.

odds = []

print("Enter 10 numbers:")
for i in range(10):
    n = int(input())
    if n % 2 == 1:
        odds.append(n)

if odds:
    print("Largest odd number is:", max(odds))
else:
    print("No odd numbers entered")