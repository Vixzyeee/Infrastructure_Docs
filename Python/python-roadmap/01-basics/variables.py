# variables.py
# This file demonstrates basic variable assignment in Python

# Case 1: Basic binding
a = 10
b = a
a = a + 5

print(b)
print(a)
print(b)

# Case 2: Deleting a name does not delete the object
x = 100
y = x

del x

print(y)

# Case 3: Expression creates a new object, not an in-place update
x = 1
y = x
x = x + 1

print(x)
print(y)
