# NOTE:
# This file is intended for reading alongside notes.md
# Running this file executes ALL cases sequentially
# Variable names are intentionally reused across cases
# to emphasize independent execution and rebinding

# if_else.py
# Demonstration of basic conditional control flow in Python

# Case 1: Basic if statement
x = 10

if x > 5:
    print("x is greater than 5")

print("End of Case 1")

# Case 2: if–else branching
x = 3

if x > 5:
    print("x is greater than 5")
else:
    print("x is less than or equal to 5")

print("End of Case 2")

# Case 3: if–elif–else chain
score = 75

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
else:
    print("Grade D")

print("End of Case 3")

# Case 4: Order matters in conditions
value = 10

if value > 0:
    print("Positive number")
# The elif branch is never reached due to condition order
elif value > 5:
    print("Greater than 5")

print("End of Case 4")

# Case 5: Nested if statements
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Allowed to enter")
    else:
        print("ID required")
else:
    print("Underage")

print("End of Case 5")

# Case 6: Boolean expressions
age = 25
is_member = True

if age >= 18 and is_member:
    print("Adult member")
else:
    print("Access denied")

print("End of Case 6")

# Case 7: Comparison operators
a = 5
b = 10

if a == b:
    print("a equals b")
else:
    print("a does not equal b")

if a != b:
    print("a is not equal to b")

print("End of Case 7")

# Case 8: Chained comparisons
x = 7

if 5 < x < 10:
    print("x is between 5 and 10")

print("End of Case 8")

# Case 9: Using not
is_logged_in = False

if not is_logged_in:
    print("User is not logged in")

print("End of Case 9")

# Case 10: Implicit else (no else block)
temperature = 30

if temperature > 25:
    print("Hot day")

print("End of Case 10")

# Case 11: Multiple independent if statements
number = 15

if number > 0:
    print("Positive")

if number % 3 == 0:
    print("Divisible by 3")

print("End of Case 11")

# Case 12: if–elif vs multiple if
value = 10

print("if–elif result:")
if value > 5:
    print("Greater than 5")
elif value > 8:
    print("Greater than 8")

print("multiple if result:")
if value > 5:
    print("Also greater than 5")
if value > 8:
    print("Also greater than 8")

print("End of Case 12")

# Case 13: Membership test
role = "admin"

if role in ("admin", "moderator"):
    print("Access granted")
else:
    print("Access denied")

print("End of Case 13")

# Case 14: Identity vs equality
a = None

if a is None:
    print("a is None")

print("End of Case 14")
