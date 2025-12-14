# truthy_falsy.py
# Demonstration of truthy and falsy values

values = [0, 1, "", "text", [], [1, 2], None, True, False]

for value in values:
    if value:
        print(value, "is truthy")
    else:
        print(value, "is falsy")
