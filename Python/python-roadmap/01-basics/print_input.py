# NOTE:
# This file is intended for reading alongside notes.md
# Running this file executes ALL cases sequentially
# Some cases expect user input.

# print_input.py
# Basic input and output example

## Case 1: input() always returns str
age = input("Enter your age: ")

print(type(age))
print(age + "1")

# Case 2: Explicit conversion and failure
age = input("Enter your age: ")

age_int = int(age)

print(age_int + 1)

