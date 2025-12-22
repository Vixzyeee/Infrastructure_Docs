print("=== Number Calculator ===")

first_number = input("Input first number: ")
second_number = input("Input second number: ")

first_number = int(first_number)
second_number = int(second_number)

print()
print("Result:")

addition = first_number + second_number
subtraction = first_number - second_number
multiplication = first_number * second_number

print(f"Addition       : {addition}")
print(f"Subtraction   : {subtraction}")
print(f"Multiplication : {multiplication}")
