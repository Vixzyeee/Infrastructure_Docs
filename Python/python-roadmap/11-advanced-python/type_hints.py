# type_hints.py
# Basic type hints example

from typing import List, Dict

def add(a: int, b: int) -> int:
    return a + b

def greet(name: str) -> str:
    return f"Hello, {name}"

def sum_numbers(numbers: List[int]) -> int:
    return sum(numbers)

def build_user(name: str, age: int) -> Dict[str, int | str]:
    return {"name": name, "age": age}

print(add(3, 4))
print(greet("Pito"))
print(sum_numbers([1, 2, 3]))
print(build_user("Pito", 21))
