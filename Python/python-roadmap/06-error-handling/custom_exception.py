# custom_exception.py
# Defining and raising custom exceptions

class AgeTooLowError(Exception):
    pass

age = int(input("Enter your age: "))

if age < 18:
    raise AgeTooLowError("Age must be at least 18")

print("Access granted")
