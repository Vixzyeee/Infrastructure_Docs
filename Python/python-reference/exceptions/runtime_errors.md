# Runtime Errors (Execution-Time Failures)

This document covers **runtime-related exceptions**.

These exceptions occur **during program execution** when Python encounters conditions it cannot safely continue from.

They usually indicate:
- Deep logic flaws
- Resource exhaustion
- Internal interpreter issues

All exceptions in this file inherit from `Exception`.

---

## Overview

Runtime errors are different from:
- Syntax errors (code cannot start)
- Logic errors (wrong assumptions)

Runtime errors indicate that the program **started correctly** but failed due to execution conditions.

They are often severe and should not be ignored.

---

## `RuntimeError`

### Description
Raised when an error occurs that **does not fall into a more specific category**.

**Example:**
```python
raise RuntimeError("Unexpected runtime condition")
```

**Error:**
```text
RuntimeError: Unexpected runtime condition
```

**Notes:**
- Acts as a generic fallback error
- Often signals a bug in program flow
- Often used intentionally by developers to signal unrecoverable states

**Rule:**
Do not silence `RuntimeError`. Investigate the cause.

---

## `RecursionError`

### Description
Raised when the maximum recursion depth is exceeded.

**Example:**
```python
def recurse():
    return recurse()

recurse()
```

**Error:**
```text
RecursionError: maximum recursion depth exceeded
```

**Notes:**
- Prevents stack overflow
- Common in poorly designed recursive algorithms

**Rule:**
Use iteration or limit recursion depth.

---

## `MemoryError`

### Description
Raised when the program runs **out of memory**.

**Example:**
```python
data = []
while True:
    data.append("x" * 10**6)
```

**Error:**
```text
MemoryError
```

**Notes:**
- Rare on small programs
- Common in data-heavy or infinite allocation scenarios
- May terminate the process abruptly
- In some cases, the process may terminate before this exception can be handled

**Rule:**
Memory exhaustion is a design failure. Reduce memory usage.

---

## `ReferenceError`

### Description
Raised when accessing a **weak reference** that no longer exists.

**Example:**
```python
import weakref

class Obj:
    pass

o = Obj()
r = weakref.ref(o)
del o
r()
```

**Error:**
```text
ReferenceError: weakly-referenced object no longer exists
```

**Notes:**
- Rarely encountered
- Mostly appears in advanced memory management

**Rule:**
Avoid weak references unless you understand their lifecycle.

---

## `SystemError`

### Description
Raised when the Python interpreter detects an **internal error**.

**Example:**
```python
raise SystemError("Internal interpreter error")
```

**Error:**
```text
SystemError: Internal interpreter error
```

**Notes:**
- Indicates a bug in Python or C extensions
- Not caused by normal user code

**Rule:**
Do not catch `SystemError`. Report it.

---

## Common Patterns & Mistakes

**❌ Ignoring Runtime Errors**
```python
try:
    risky_code()
except Exception:
    pass
```

This hides severe bugs.

---

**✅ Fail Fast**
```python
try:
    risky_code()
except RuntimeError as e:
    log_and_abort(e)
```

---

## Summary
- Runtime errors occur during execution
- They often indicate serious problems
- Catch them only when you can recover safely
- Most runtime errors should terminate the program

If your program reaches this file often, the design needs rethinking.