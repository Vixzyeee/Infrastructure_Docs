# os_sys.py
# Basic usage of os and sys modules

import os
import sys

print("Current working directory:")
print(os.getcwd())

print("\nList files in current directory:")
print(os.listdir("."))

print("\nPython executable:")
print(sys.executable)

print("\nPython version:")
print(sys.version)
