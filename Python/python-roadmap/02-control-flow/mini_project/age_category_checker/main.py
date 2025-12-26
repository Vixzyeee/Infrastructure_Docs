print("=== Age Category Checker ===")
print()

name = input("Name: ")
age = input("Age: ")

# convert
age = int(age)

print()
print("=== RESULT ===")

print(f"Name : {name}")
print(f"Age  : {age}")

# age category logic
if age < 0:
    category = "Invalid age"
elif age < 13:
    category = "Child"
elif age < 18:
    category = "Teenager"
elif age < 60:
    category = "Adult"
else:
    category = "Senior"

print(f"Category : {category}")
