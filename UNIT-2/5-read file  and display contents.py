# Write a program to read a file and display its contents. At the end it shall also display no. of words available in file.

filename = input("Enter the file name: ")

try:
    with open(filename, 'r') as file:
        content = file.read()
        
        print("\nFile Contents:\n")
        print(content)
        
        words = content.split()
        word_count = len(words)
        
        print("\nNumber of words in the file:", word_count)

except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print("An error occurred:", e)
