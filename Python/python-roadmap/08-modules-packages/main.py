# main.py
# Entry point of the program

from math_utils import add, subtract
from helpers.string_utils import to_upper

result = add(10, 5)
print("Add result:", result)

text = to_upper("python modules")
print("Upper text:", text)
