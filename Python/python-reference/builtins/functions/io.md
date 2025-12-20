# Input and Output Built-in Functions

This file documents **built-in functions related to basic input and output**.

These functions provide **minimal, universal I/O primitives** that are always
available without importing any modules.

They are intentionally simple and opinionated.

---

## Scope

Covered in this file:
- `print`
- `input`
- `open`

Not covered:
- file object methods
- advanced I/O abstractions
- buffering strategies
- networking or async I/O

---

## I/O Context

Python’s built-in I/O functions exist to:
- support interactive usage
- provide a lowest-common-denominator interface
- bootstrap higher-level I/O systems

They are not designed to replace full I/O frameworks.

---

## `print()`

### Definition
Writes textual representations of objects to an output stream.

### Syntax
```python
print(*objects, sep=' ', end='\n', file=None, flush=False)
```

**Behavior:**
- Converts objects using `str()`
- Writes to `sys.stdout` by default
- Appends a newline unless overridden

**Example:**
```python
print("hello", "world")
print(1, 2, 3, sep=",")
```

**Output:**
```text
hello world
1,2,3
```

**Notes:**
- Intended for human-readable output
- Not suitable for structured or machine-oriented output
- Output destination can be redirected

---

## `input()`

### Definition
Reads a line of text from standard input.

### Syntax
```python
input(prompt=None)
```

**Behavior:**
- Displays the prompt if provided
- Reads a single line from `sys.stdin`
- Returns a string without the trailing newline

**Example:**
```python
name = input("Name: ")
print(name)
```

**Output:**
```text
Name: admin
admin
```

**Notes:**
- Always returns a string
- Blocking operation
- Intended for interactive use only
- Not suitable for non-interactive or automated environments

---

## `open()`

### Definition
Opens a file and returns a file object.

### Syntax
```python
open(file, mode='r', buffering=-1, encoding=None,
     errors=None, newline=None, closefd=True, opener=None)
```

**Behavior:**
- Returns a file object bound to a system resource
- Mode controls read/write behavior
- Encoding applies only to text mode

**Example:**
```python
f = open("example.txt", "w")
f.write("data")
f.close()
```

**Output:**
```text
(data written to file)
```

**Notes:**
- File objects must be closed explicitly
- Prefer context managers for safety
- Errors depend on OS and filesystem
- Resource acquisition is immediate; failure raises an exception

---

## Design Notes
- These functions are **foundational**, not flexible
- They favor simplicity over configurability
- Higher-level I/O belongs in the standard library

---

## Summary
- `print` handles basic output
- `input` supports interactive input
- `open` bridges Python and the filesystem

This file defines **Python’s minimal I/O surface**, not full I/O systems.