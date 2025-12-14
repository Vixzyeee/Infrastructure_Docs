# pathlib_basic.py
# Basic usage of pathlib module

from pathlib import Path

current_path = Path.cwd()

print("Current path:")
print(current_path)

print("\nList files using pathlib:")
for item in current_path.iterdir():
    print(item.name)

example_file = current_path / "example.txt"
print("\nExample file path:")
print(example_file)
