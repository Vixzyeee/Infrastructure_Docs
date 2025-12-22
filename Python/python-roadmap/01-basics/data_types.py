# NOTE:
# This file is intended for reading alongside notes.md
# Running this file executes ALL cases sequentially

# data_types.py
# Demonstration of basic Python data types

# Case 1: Type belongs to the object, not the name
x = 10
print(type(x))

x = "10"
print(type(x))

# Case 2: Immutable objects cannot be modified in place
x = 10
print(id(x))

x = x + 1
print(id(x))

# Case 3: Mutable objects can be modified in place
x = [1, 2, 3]
print(id(x))

x.append(4)
print(id(x))

print(x)

# Case 4: Shared reference to a mutable object
a = [1, 2]
b = a

print(id(a))
print(id(b))

b.append(3)

print(a)
print(b)

