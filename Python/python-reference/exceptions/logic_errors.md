# Logic Errors (Programming Mistakes)

This document covers **logic-related exceptions**.

These exceptions are raised when the program is **syntactically valid** but the logic is incorrect or assumptions about data are wrong.

Most bugs in real-world Python applications fall into this category.

---

## Overview

Logic errors usually indicate:
- Incorrect assumptions about data types or values
- Accessing data that does not exist
- Calling methods or attributes incorrectly
- Violating explicit or implicit constraints

These errors inherit from `Exception` and are safe to catch.

---

## `TypeError`

### Description
Raised when an operation or function is applied to an object of **inappropriate type**.

### Common Causes
- Using the wrong data type
- Mixing incompatible types
- Calling non-callable objects

**Example:**
```python
result = "10" + 5
```

**Error:**
```text
TypeError: can only concatenate str (not "int") to str
```

**Rule:**
Validate types before operations or convert explicitly.

---

## `ValueError`

### Description
Raised when a function receives an argument of the **correct type** but with an **invalid value**.

**Common Causes:**
- Invalid string-to-number conversion
- Out-of-range values
- Malformed input

**Example:**
```python
int("abc")
```

**Error:**
```text
ValueError: invalid literal for int()
```

**Rule:**
Type is right. Value is wrong.

---

## `NameError`

### Description
Raised when a variable or name is **not defined**.

**Common Causes:**
- Typos
- Using variables before assignment
- Missing imports

**Example:**
```python
print(total)
```

**Error:**
```text
NameError: name 'total' is not defined
```

**Rule:**
If Python doesn’t know the name, neither should your code.

---

## `UnboundLocalError`

### Description
A subclass of `NameError`.

Raised when a local variable is referenced **before assignment**, even though a variable with the same name exists elsewhere.

**Example:**
```python
x = 10

def func():
    print(x)
    x = 5

func()
```

**Error:**
```text
UnboundLocalError: local variable 'x' referenced before assignment
```

**Rule:**
Assignment inside a function makes the variable local unless declared otherwise.

---

## `AttributeError`

### Description
Raised when an attribute reference or assignment fails.

**Common Causes:**
- Calling non-existent methods
- Typos in attribute names
- Wrong object type

**Example:**
```python
numbers = [1, 2, 3]
numbers.appendd(4)
```

**Error:**
```text
AttributeError: 'list' object has no attribute 'appendd'
```

**Rule:**
Know the object’s API before calling methods.

---

## `IndexError`

### Description
Raised when accessing a sequence index that is **out of range**.

**Common Causes:**
- Invalid list or tuple index
- Off-by-one errors

**Example:**
```python
items = [1, 2, 3]
print(items[5])
```

**Error:**
```text
IndexError: list index out of range
```

**Rule:**
Indexes are zero-based. Length matters.

---

## `KeyError`

### Description
Raised when accessing a dictionary key that does not exist.

**Example:**
```python
data = {"a": 1}
print(data["b"])
```

**Error:**
```text
KeyError: 'b'
```

**Rule:**
Use `.get()` or check key existence when unsure.

**Note:**
Using `.get()` returns `None` instead of raising `KeyError`.

---

## `LookupError`

### Description
Base class for lookup-related errors.

**Child Exceptions:**
- `IndexError`
- `KeyError`

**Notes:**
Mostly useful for catching both `IndexError` and `KeyError` together.

---

## `AssertionError`

### Description
Raised when an `assert` statement fails.

**Example:**
```python
x = -1
assert x > 0, "x must be positive"
```

**Error:**
```text
AssertionError: x must be positive
```

**Notes:**
- Used for debugging, not user-facing validation
- Can be disabled with optimization flags
- Do not use assertions for validating external input

**Rule:**
Assertions document assumptions, not handle errors.

---

## `NotImplementedError`

### Description
Raised to indicate that a method or function is **intentionally not implemented**.

**Example:**
```python
class Shape:
    def area(self):
        raise NotImplementedError
```

**Notes:**
- Common in abstract base classes
- Not a placeholder error

**Rule:**
Use to enforce subclass implementation.

---

## Common Patterns & Mistakes

**❌ Catching Too Broad**
```python
try:
    risky_code()
except Exception:
    pass
```

This hides logic bugs.

**✅ Catch Specific Errors**
```python
try:
    risky_code()
except (TypeError, ValueError) as e:
    handle_error(e)
```

## Summary

- Logic errors indicate mistakes in assumptions or usage
- Most inherit directly from `Exception`
- Catch specific exceptions when possible
- Fix the logic, don’t silence the error

These exceptions usually point to **bugs**, not edge cases.