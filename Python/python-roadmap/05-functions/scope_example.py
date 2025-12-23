# scope_example.py
# Demonstration of variable scope

x = 10

def show_value():
    x = 5
    print("Inside function:", x)

show_value()
print("Outside function:", x)
