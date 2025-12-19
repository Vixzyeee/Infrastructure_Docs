# Exception Fundamentals (Core Exceptions)

This document covers the **core exception classes** that form the foundation of Python’s exception system.

These exceptions sit at the **root of the exception hierarchy** and behave differently from typical runtime errors.

Understanding this file is mandatory before documenting or handling any other exception.

---

## Exception Hierarchy Overview

All exceptions in Python inherit from `BaseException`.
```text
BaseException
├── Exception
│ └── (Most application-level errors)
├── SystemExit
├── KeyboardInterrupt
└── GeneratorExit
```

---

## `BaseException`

### Description
The **root class of all exceptions** in Python.

You should almost **never catch this directly**.

### Purpose
- Acts as the absolute base for the exception system
- Allows critical exceptions to bypass generic exception handling

**Example:**
```python
try:
    raise BaseException("Something very bad")
except BaseException as e:
    print(e)
```

**Notes:**
- Catching `BaseException` will also catch:
  - `SystemExit`
  - `KeyboardInterrupt`
  - `GeneratorExit`
- This is usually **a bug**, not a feature

**Rule:**
Do NOT use `except BaseException` unless you know exactly why.

---

## `Exception`

### Description
The **base class for all non-system-exiting errors**.

This is the class you usually want to catch.

### Purpose
- Represents application-level and logic errors
- Safe to catch in most programs

**Example:**
```python
try:
    int("abc")
except Exception as e:
    print(type(e).__name__)
```

**Output:**
```text
ValueError
```

**Notes:**
- `except Exception` does NOT catch:
  - `SystemExit`
  - `KeyboardInterrupt`
- This is intentional and correct

**Rule:**
Use `except Exception` for generic error handling, not `BaseException`.

---

## Bare `except:` vs `except Exception`

Avoid using bare `except:`.
```python
try:
    risky_code()
except:
    pass
```

This catches:
- `SystemExit`
- `KeyboardInterrupt`
- `GeneratorExit`

Bare `except:` should only be used in very rare cases such as **top-level crash logging**, where the program is about to terminate anyway.

Correct usage:
```python
try:
    risky_code()
except Exception as e:
    handle_error(e)
```

---

## `SystemExit`

### Description
Raised when the program is instructed to exit.

Usually triggered by:
- `sys.exit()`
- `exit()`
- `quit()`

**Example:**
```python
import sys

sys.exit("Shutting down")
```

**Example:**
```python
try:
    sys.exit(0)
except Exception:
    print("This will not run")
```

**Behavior:**
- Terminates the program immediately
- Can be caught, but **should not be suppressed**

**Example (Bad Practice):**
```python
try:
    sys.exit()
except Exception:
    print("Still running")  # Will NOT execute
```

**Notes:**
- Inherits directly from `BaseException`
- Not meant to be handled like normal errors
- `SystemExit` carries an optional exit code or message

**Rule:**
Let `SystemExit` pass through.

---

## `KeyboardInterrupt`

### Description
Raised when the user interrupts execution manually.

Usually triggered by:
- `Ctrl + C`

**Example:**
```python
try:
    while True:
        pass
except KeyboardInterrupt:
    print("Interrupted by user")
```

**Example:**
```python
try:
    while True:
        pass
except KeyboardInterrupt:
    print("Cleaning up...")
    raise
```

**Behavior:**
- Indicates intentional termination
- Not a program error

**Notes:**
- Inherits from `BaseException`
- Catching it may trap the user in the program

**Rule:**
Only catch if you need to clean up resources, then re-raise or exit.

---

## `GeneratorExit`

### Description
Raised when a generator is closed.

Usually triggered by:
- `generator.close()`
- Garbage collection
- Program termination

**Example:**
```python
def gen():
    try:
        yield 1
    finally:
        print("Generator closed")

g = gen()
next(g)
g.close()
```

**Output:**
```text
Generator closed
```

**Notes:**
- Not an error condition
- Used internally by Python
- Should not be suppressed

**Rule:**
Do not catch `GeneratorExit` unless implementing advanced generator logic.

---

## Common Mistakes

**❌ Catching Everything**
```python
try:
    risky_code()
except BaseException:
    pass
```

This will:
- Ignore Ctrl+C
- Prevent program exit
- Hide critical failures

**✅ Correct Generic Handling**
```python
try:
    risky_code()
except Exception as e:
    handle_error(e)
```

## Summary

- `BaseException` is the root of all exceptions
- `Exception` is the correct base for application errors
- `SystemExit`, `KeyboardInterrupt`, and `GeneratorExit` are **control-flow signals**
- Do not suppress system-level exceptions
- Catch narrowly, not lazily

This file defines **what should and should not be caught** in Python.