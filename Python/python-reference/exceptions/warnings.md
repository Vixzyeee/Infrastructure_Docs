# Warnings (Non-Fatal Runtime Signals)

This document covers **Python warnings**.

Warnings are **non-fatal signals** emitted by Python to indicate potential problems, deprecated behavior, or risky patterns.

Unlike exceptions:
- Warnings do NOT stop program execution
- Warnings are meant to be noticed, not ignored

Warnings are part of Python’s **early warning system**.

---

## Overview

Warnings usually indicate:
- Deprecated features
- Risky or ambiguous behavior
- Potential bugs that may break in the future
- Backward compatibility issues

Ignoring warnings does not crash your program today,  
but it often guarantees problems tomorrow.

---

## `Warning`

### Description
Base class for all warning categories.

**Notes:**
- Rarely used directly
- Most warnings are emitted as subclasses
- Usually not emitted directly
- Subclasses are used in practice

**Rule:**
Do not filter all warnings blindly.

---

## `DeprecationWarning`

### Description
Indicates that a feature is **deprecated** and may be removed in future versions.

**Example:**
```python
import warnings
warnings.warn("This feature is deprecated", DeprecationWarning)
```

**Output:**
```text
DeprecationWarning: This feature is deprecated
```

**Notes:**
- Often hidden by default
- Common in libraries transitioning APIs

**Rule:**
Fix deprecated usage early.

---

## `PendingDeprecationWarning`

### Description
Signals features that will be deprecated in the future, but are not yet officially deprecated.

**Example:**
```python
import warnings
warnings.warn("This will be deprecated soon", PendingDeprecationWarning)
```

**Output:**
```text
PendingDeprecationWarning: This will be deprecated soon
```

**Notes:**
- Mostly useful for library authors
- Rare in application code

**Rule:**
Treat as early technical debt.

---

## `FutureWarning`

### Description
Indicates that behavior will change in a future Python version.

**Example:**
```python
import warnings
warnings.warn("Behavior will change", FutureWarning)
```

**Output:**
```text
FutureWarning: Behavior will change
```

**Notes:**
- Often visible by default
- Common in numerical and data libraries

**Rule:**
Future warnings are not optional. Address them.

---

## `RuntimeWarning`

### Description
Signals suspicious runtime behavior.

**Example:**
```python
import warnings
warnings.warn("Suspicious runtime behavior", RuntimeWarning)
```

**Output:**
```text
RuntimeWarning: Suspicious runtime behavior
```

**Notes:**
- Indicates logic that may be incorrect
- Often emitted by math or numeric code

**Rule:**
Investigate immediately.

---

## `SyntaxWarning`

### Description
Warns about questionable syntax that is technically valid but risky.

**Example:**
```python
import warnings
warnings.warn("Suspicious syntax", SyntaxWarning)
```

**Output:**
```text
SyntaxWarning: Suspicious syntax
```

**Notes:**
- May indicate bugs caused by operator precedence
- Not a syntax error

**Rule:**
Clean it up before it becomes an error.

---

## `UserWarning`

### Description
Generic warning category for application-level warnings.

**Example:**
```python
import warnings
warnings.warn("Custom warning", UserWarning)
```

**Output:**
```text
UserWarning: Custom warning
```

**Notes:**
- Default warning type when none is specified
- Intended for developers, not end users

**Rule:**
Use sparingly and meaningfully.

---

## `ResourceWarning`

### Description
Indicates potential resource leaks.

**Example:**
```python
import warnings
warnings.warn("Unclosed resource", ResourceWarning)
```

**Output:**
```text
ResourceWarning: Unclosed resource
```

**Notes:**
- Often related to unclosed files or sockets
- Usually hidden by default

**Rule:**
Close what you open.

---

## `BytesWarning`

### Description
Warns about implicit mixing of bytes and strings.

**Example:**
```python
import warnings
warnings.warn("Bytes/str confusion", BytesWarning)
```

**Output:**
```text
BytesWarning: Bytes/str confusion
```

**Notes:**
- Useful during Python 2 → 3 transitions
- Still relevant in low-level code

**Rule:**
Be explicit about text vs bytes.

---

## `UnicodeWarning`

### Description
Signals suspicious Unicode operations.

**Example:**
```python
import warnings
warnings.warn("Unicode issue detected", UnicodeWarning)
```

**Output:**
```text
UnicodeWarning: Unicode issue detected
```

**Notes:**
- Rare in modern Python
- Appears in encoding edge cases

**Rule:**
Unicode bugs are never harmless.

---

## Warning Control (`warnings` module)

**Showing all warnings**
```python
import warnings
warnings.simplefilter("default")
```

**Treat warnings as errors**
```python
warnings.simplefilter("error")
```

This converts warnings into exceptions.

---

## Common Mistakes

**❌ Ignoring All Warnings**
```python
import warnings
warnings.filterwarnings("ignore")
```

This hides real problems.

**✅ Controlled Filtering**
```python
warnings.filterwarnings("ignore", category=DeprecationWarning)
```

Filter narrowly, not globally.

## Summary
- Warnings are non-fatal but important
- They signal future failures and risky behavior
- Ignoring warnings accumulates technical debt
- Treat warnings seriously, especially in production
- Convert warnings to errors during development when possible

Warnings are Python telling you “this still works… but don’t get comfortable.”