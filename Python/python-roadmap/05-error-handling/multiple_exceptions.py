# multiple_exceptions.py
# Handling multiple exception types

try:
    numbers = [1, 2, 3]
    index = int(input("Enter index: "))
    print(numbers[index])
except ValueError:
    print("Input must be a number.")
except IndexError:
    print("Index out of range.")
