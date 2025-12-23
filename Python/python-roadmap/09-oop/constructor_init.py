# constructor_init.py
# Using __init__ as a constructor

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user1 = User("Pito", 21)
print(user1.name)
print(user1.age)
