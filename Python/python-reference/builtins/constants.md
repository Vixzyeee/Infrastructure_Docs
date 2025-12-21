# Built-in Constants

This file documents **Python’s built-in constant objects**.

These objects:
- exist in the global namespace
- are always available
- represent fixed semantic values in the language

They are **objects**, not keywords, and participate fully in Python’s object model.

---

## Scope

Covered in this file:
- `None`
- `True`
- `False`
- `NotImplemented`
- `Ellipsis`

Not covered:
- literals and syntax rules
- boolean operators
- sentinel objects from libraries

---

## Constants as Objects

All constants documented here:
- have identity
- have a type
- can be passed, compared, and returned

All built-in constants documented here are singleton objects.

They are not compiler directives.
They are runtime objects with defined semantics.

---

## `None`

### Definition
Represents the absence of a value.

### Role
- Default return value for functions
- Sentinel for `“no result”` or `“no value”`
- Explicit placeholder for missing data

**Example:**
```python
def f():
    pass

print(f())
```

**Output:**
```text
None
```

**Notes:**
- There is exactly one `None` object
- Its type is `NoneType`
- Should be compared using `is`, not `==`

---

## `True`

### Definition
Represents the boolean truth value true.

### Role
- Logical truth
- Control-flow condition result
- Numeric value equivalent to `1`

**Example:**
```python
print(True == 1)
print(True + 1)
```

**Output:**
```text
True
2
```

**Notes:**
- Subclass of `int`
- Exists for semantic clarity
- Should not be treated as a generic integer

---

## `False`

### Definition
Represents the boolean truth value false.

### Role
- Logical falsehood
- Control-flow condition result
- Numeric value equivalent to `0`

**Example:**
```python
print(False == 0)
print(False * 10)
```

**Output:**
```text
True
0
```

**Notes:**
- Subclass of `int`
- Exists for readability and intent
- Prefer boolean semantics over numeric ones

---

## `NotImplemented`

### Definition
A special marker used to signal unsupported operations.

### Role
- Returned by binary special methods
- Informs the interpreter to try alternative resolution
- Not an error signal

**Example:**
```python
class A:
    def __eq__(self, other):
        return NotImplemented

print(A() == 1)
```

**Output:**
```text
False
```

**Notes:**
- Must be returned, not raised
- Used internally during operator dispatch
- Misuse leads to incorrect comparison behavior
- The interpreter handles `NotImplemented`; it is not the final comparison result

---

## `Ellipsis`

### Definition
Represents an explicit “not fully specified” value.

### Role
- Placeholder in slicing
- Marker in APIs and data structures
- Structural sentinel

**Example:**
```python
print(...)
```

**Output:**
```text
Ellipsis
```

**Notes:**
- Single shared object
- Commonly used in multidimensional slicing
- Rarely used in application logic
- Its primary purpose is structural, not semantic

---

## Design Notes
- These constants exist to encode language-level meaning
- They are not interchangeable with user-defined sentinels
- Identity matters more than value
- Misuse often leads to subtle bugs

---

## Summary
- Built-in constants are singleton objects
- They represent fixed semantic concepts
- They participate fully in runtime behavior
- Correct usage depends on identity, not equality
- These objects encode meaning that cannot be safely replicated by user-defined sentinels

This file defines **Python’s built-in constant objects**, not syntactic literals.