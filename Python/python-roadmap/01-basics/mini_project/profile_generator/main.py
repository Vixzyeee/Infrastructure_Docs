print("=== Profile Generator ===")
print()

name = input("Name: ")
age = input("Age: ")
height = input("Height (cm): ")

age = int(age)
height = float(height)

print()
print("=== PROFILE SUMMARY ===")

print(f"Name          : {name}")
print(f"Current Age   : {age}")
print(f"Age Next Year : {age + 1}")
print(f"Height        : {height} cm")
