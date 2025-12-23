# generator_yield.py
# Basic generator and yield example

def count_up_to(limit):
    current = 1
    while current <= limit:
        yield current
        current += 1

gen = count_up_to(5)

print("Generator output:")
for number in gen:
    print(number)
