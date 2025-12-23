# comprehension.py
# List, dict, and set comprehension examples

numbers = [1, 2, 3, 4, 5]

squares = [n * n for n in numbers]
print("Squares:", squares)

even_numbers = [n for n in numbers if n % 2 == 0]
print("Even numbers:", even_numbers)

square_map = {n: n * n for n in numbers}
print("Square map:", square_map)

unique_lengths = {len(word) for word in ["python", "java", "go", "python"]}
print("Unique lengths:", unique_lengths)
