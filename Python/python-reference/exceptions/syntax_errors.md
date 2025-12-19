# Syntax Errors (Code Structure Failures)

This document covers **syntax-related exceptions**.

These errors occur when Python **cannot parse the source code**.  
The program does not start. No execution happens.

Syntax errors are detected **before runtime**.

---

## Overview

Syntax errors usually indicate:
- Invalid Python syntax
- Incorrect indentation
- Mixing tabs and spaces
- Malformed statements or blocks

These errors must be **fixed**, not handled.

They cannot be caught using `try/except`.

---

## `SyntaxError`

### Description
Raised when Python encounters **invalid syntax**.

**Common Causes:**
- Missing colons
- Unmatched parentheses or quotes
- Invalid keywords or expressions
- Incorrect statement structure

**Example:**
```python
if x > 5
    print(x)
```

**Error:**
```text
SyntaxError: expected ':'
```

**Notes:**
- Occurs before code execution
- Line number and position are usually provided
- Cannot be caught with `try/except`
- Error messages may vary depending on Python version

**Rule:**
If you see `SyntaxError`, the code is simply **not valid Python**.

---

## `IndentationError`

### Description
Raised when indentation is **incorrect or inconsistent**.

Python uses indentation to define code blocks.  
If indentation is wrong, the program cannot be parsed.

**Common Causes:**
- Missing indentation
- Unexpected indentation
- Misaligned code blocks

**Example:**
```python
def func():
print("hello")
```

**Error:**
```text
IndentationError: expected an indented block
```

**Notes:**
- A subclass of `SyntaxError`
- Very common for beginners
- Fatal until fixed

**Rule:**
Indentation defines structure. Python does not guess.

---

## `TabError`

### Description
Raised when **tabs and spaces are mixed inconsistently**.

**Example:**
(Note: The ⇥ symbol represents a tab character)

```python
def func():
⇥print("hello")
    print("world")
```

**Error:**
```text
TabError: inconsistent use of tabs and spaces in indentation
```

**Notes:**
- A subclass of `IndentationError`
- Usually caused by editor configuration
- Invisible characters cause visible pain

**Rule:**
Use spaces consistently. Configure your editor properly.

---

## Important Limitations

**❌ Cannot Be Caught**
```python
try:
    if True
        print("hi")
except SyntaxError:
    pass
```

This will **never run**.

Syntax errors occur **before** the interpreter executes code.

---

## Common Mistakes

**❌ Treating Syntax Errors Like Runtime Errors**
Syntax errors are not bugs in logic.  
They are violations of the language grammar.

**✅ Fix the Code**
The only solution is to **correct the source code**.

---

## Summary
- Syntax errors prevent the program from starting
- They are detected before runtime
- They cannot be handled with `try/except`
- `IndentationError` and `TabError` are specialized syntax errors
- Fix the structure, not the behavior

If this file appears often in your workflow, the editor setup is probably the real problem.
