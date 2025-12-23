# try_except.py
# Basic try-except usage

try:
    number = int(input("Enter a number: "))
    print("You entered:", number)
except ValueError:
    print("Invalid input. Please enter a number.")
