# Arithmetic Errors (Numeric Failures)

This document covers **arithmetic-related exceptions**.

These exceptions occur when a numeric operation is **mathematically invalid**, exceeds limits, or violates numeric constraints.

They are runtime errors and inherit from `Exception`.

---

## Overview

Arithmetic errors usually indicate:
- Invalid mathematical operations
- Division by zero
- Numeric overflow
- Floating-point limitations

These errors must be **handled or avoided**, depending on context.

---

## `ArithmeticError`

### Description
Base class for arithmetic-related runtime exceptions.

### Child Exceptions
- `ZeroDivisionError`
- `OverflowError`
- `FloatingPointError`

**Notes:**
- Rarely raised directly
- Mostly useful for grouping numeric failures

**Rule:**
Catch specific arithmetic errors when possible.

---

## `ZeroDivisionError`

### Description
Raised when attempting to divide by zero.

**Example:**
```python
result = 10 / 0
```

**Error:**
```text
ZeroDivisionError: division by zero
```

**Notes:**
- Applies to both integer and floating-point division
- Always a runtime error
- Integer division (`//`) also raises `ZeroDivisionError`

**Rule:**
Never assume a divisor is non-zero. Validate inputs.

---

## `OverflowError`

### Description
Raised when the result of a numeric operation is **too large to be represented**.

**Example:**
```python
import math

math.exp(1000)
```

**Error:**
```text
OverflowError: math range error
```

**Notes:**
- More common in math libraries (`math`, `decimal`)
- Less common with Python integers (they auto-expand)

**Rule:**
Know the numeric limits of the operation you are performing.

---

## `FloatingPointError`

### Description
Raised when a floating-point operation fails.

**Example:**
```python
# FloatingPointError is not raised by default
import math
math.sqrt(-1)
```

**Error:**
```text
ValueError: math domain error
```

(Note: `FloatingPointError` is rarely raised by default.)

**Notes:**
- Floating-point errors are usually **silently handled**
- Requires explicit configuration via `numpy` or `decimal`
- In the standard library, floating-point domain errors usually raise `ValueError` instead of `FloatingPointError`

**Rule:**
Do not rely on `FloatingPointError` unless explicitly enabled.

---

## Common Patterns & Mistakes

**❌ Assuming Math Always Works**
```python
result = total / count
```
If **count** is zero, the program crashes.

---

**✅ Validate Before Calculating**
```python
if count == 0:
    raise ValueError("count must not be zero")

result = total / count
```

---

## Summary
- Arithmetic errors occur during numeric operations
- `ArithmeticError` is the base class
- `ZeroDivisionError` is the most common
- `OverflowError` depends on numeric limits
- `FloatingPointError` is rarely raised by default
- Validate numeric inputs before calculation

Arithmetic errors are predictable.  
If they surprise you, the assumptions were wrong.