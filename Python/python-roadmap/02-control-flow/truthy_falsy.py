# NOTE:
# This file is intended for reading alongside notes.md
# Running this file executes ALL cases sequentially

# truthy_falsy.py
# Demonstration of truthy and falsy values in Python

# Case 1: Boolean literals
if True:
    print("This runs")

if False:
    print("This does not run")

print("End of Case 1")

# Case 2: Numbers as conditions
if 1:
    print("1 is truthy")

if 0:
    print("0 is truthy")

print("End of Case 2")

# Case 3: Strings as conditions
if "hello":
    print("Non-empty string is truthy")

if "":
    print("Empty string is truthy")

print("End of Case 3")

# Case 4: Lists as conditions
if [1, 2, 3]:
    print("Non-empty list is truthy")

if []:
    print("Empty list is truthy")

print("End of Case 4")

# Case 5: None as condition
value = None

if value:
    print("Value exists")
else:
    print("Value is None or falsy")

print("End of Case 5")

# Case 6: Explicit vs implicit checks
items = []

if items:
    print("Items exist")

if items == []:
    print("Items list is empty")

print("End of Case 6")

# Case 7: Function return truthiness
def get_value():
    return ""

result = get_value()

if result:
    print("Function returned something")

print("End of Case 7")

# Case 8: Using not
data = []

if not data:
    print("Data is empty")

print("End of Case 8")

# Case 9: Different falsy values
values = [0, "", [], None, False]

for v in values:
    if v:
        print(v, "is truthy")
    else:
        print(v, "is falsy")

print("End of Case 9")

# Case 10: Dangerous assumption
user_age = 0

if user_age:
    print("Age provided")
else:
    print("Age missing")

print("End of Case 10")

