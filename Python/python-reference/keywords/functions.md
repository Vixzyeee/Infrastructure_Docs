# Function Keywords

## What is this?
Function keywords are used to define, control, and manage functions
in Python.

---

## def
**Purpose:** Define a function.

```python
def greet():
    print("hello")
```

**Output:**

```text
hello
```

**Notes:**

- Used to create a function definition
- Function body is defined by indentation

---

## return
**Purpose:** Return a value from a function and exit it.

```python
def add(a, b):
    return a + b

result = add(2, 3)
print(result)
```

**Output:**

```text
5
```

**Notes:**

- Ends function execution immediately
- Can return a value or nothing (None)

---

## lambda
**Purpose:** Create a small anonymous function.

```python
add = lambda a, b: a + b
print(add(2, 3))
```

**Output:**

```text
5
```

**Notes:**

- Limited to a single expression
- Often used for short, simple functions

---

## yield
**Purpose:** Produce a value from a generator function.

```python
def count_up():
    yield 1
    yield 2
    yield 3

for i in count_up():
    print(i)
```

**Output:**

```text
1
2
3
```

**Notes:**

- Turns a function into a generator
- Execution resumes after each yield

---
