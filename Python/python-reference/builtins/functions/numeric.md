# Numeric Built-in Functions

This file documents **numeric-related built-in functions** provided by Python.

These functions perform **basic numeric operations** that are fundamental to the language runtime.
They are available globally and operate across Python’s numeric types.

This file focuses on:
- semantic behavior
- return values
- interaction with numeric types

It does **not** document numeric methods or operators.

---

## Scope

Covered in this file:
- `abs`
- `round`
- `pow`
- `divmod`

Not covered:
- arithmetic operators (`+`, `-`, `*`, `/`)
- numeric methods (`int.bit_length`, `float.is_integer`, etc.)
- math-heavy operations (`math` module)

---

## `abs()`

### Definition
Returns the **absolute value** of a number.

### Syntax
```python
abs(x)
```

**Behavior:**
- Removes the sign of a numeric value
- Works with integers, floats, and complex numbers
- For complex numbers, returns the magnitude

**Example:**
```python
print(abs(-10))
print(abs(-3.5))
print(abs(3 + 4j))
```

**Output:**
```text
10
3.5
5.0
```

**Notes:**
- For `complex`, this is equivalent to Euclidean length
- Does not mutate the input
- Delegates to the object’s numeric protocol

---

## `round()`

### Definition
Rounds a number to a given number of decimal digits.

### Syntax
```python
round(number, ndigits=None)
```

**Behavior:**
- Returns an integer when ndigits is omitted, otherwise returns a value of the same numeric category
- Uses **banker’s rounding** (round to even)

**Example:**
```python
print(round(3.5))
print(round(2.5))
print(round(3.14159, 2))
```

**Output:**
```text
4
2
3.14
```

**Notes:**
- This is not traditional “round half up”
- Behavior is intentional for numeric stability
- Floating-point precision affects results

---

## `pow()`

### Definition
Raises a number to a power, with optional modulo support.

### Syntax
```python
pow(base, exp[, mod])
```

**Behavior:**
- Equivalent to `base ** exp`
- With `mod`, computes modular exponentiation efficiently
- Supports integers, floats, and complex numbers

**Example:**
```python
print(pow(2, 3))
print(pow(2, 3, 5))
```

**Output:**
```text
8
3
```

**Notes:**
- The 3-argument form is **not optional sugar**
- Modular exponentiation avoids large intermediate values
- Commonly used in cryptography and number theory
- The modular form only supports integers

---

## `divmod()`

### Definition
Returns both the quotient and remainder of a division.

### Syntax
```python
divmod(a, b)
```

**Behavior:**
- Equivalent to `(a // b, a % b)`
- Guarantees mathematical consistency between results
- Works with integers and floats

**Example:**
```python
print(divmod(10, 3))
print(divmod(7.5, 2))
```

**Output:**
```text
(3, 1)
(3.0, 1.5)
```

**Notes:**
- Useful when both results are needed
- Avoids duplicate division operations
- Respects Python’s floor-division rules
- Negative operands follow floor division behavior

---

## Design Notes
- These functions exist because they are fundamental numeric primitives
- They operate across multiple numeric types
- They integrate directly with Python’s numeric model
- More specialized math is intentionally excluded and delegated to the standard library

---

## Summary
- Numeric built-ins provide core arithmetic behavior
- They are type-aware and protocol-driven
- Precision and rounding behavior are deliberate
- These functions prioritize correctness over intuition

This file defines **Python’s numeric built-in function surface**, not numeric theory.