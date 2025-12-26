print("=== NUMBER COMPARISON ===")

first_input = input("Enter the first number: ")
second_input = input("Enter the second number: ")

first_number = int(first_input)
second_number = int(second_input)

if first_number > second_number:
    print("First number is greater")
elif second_number > first_number:
    print("Second number is greater")
else:
    print("Both numbers are equal")
