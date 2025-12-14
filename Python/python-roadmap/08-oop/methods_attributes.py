# methods_attributes.py
# Class methods and attributes

class User:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}")

user1 = User("Pito")
user2 = User("Alex")

user1.greet()
user2.greet()
