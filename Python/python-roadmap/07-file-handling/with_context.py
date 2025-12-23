# with_context.py
# Using context manager for file handling

with open("sample.txt", "r") as file:
    for line in file:
        print(line.strip())
