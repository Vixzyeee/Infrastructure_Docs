# Numeric Types

This file documents **Python’s built-in numeric types**.

These types define how numbers are:
- represented
- compared
- combined
- interpreted as truth values

They form Python’s **numeric model**, not just containers for values.

---

## Scope

Covered in this file:
- `int`
- `float`
- `complex`
- `bool`

Not covered:
- numeric operators
- numeric methods
- mathematical libraries

---

## Numeric Model Overview

Python’s numeric types are:
- immutable
- interoperable
- ordered by a well-defined coercion hierarchy
- This hierarchy applies to type promotion, not value ordering

Operations between numeric types follow predictable promotion rules.

---

## `int`

### Definition
Represents arbitrary-precision integers.

### Role
- Exact numeric representation
- No fixed size limit
- Primary integer type in Python

**Example:**
```python
x = 10
y = 10**100
print(x)
print(y)
```

**Output:**
```text
10
10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
```

**Notes:**
- Precision limited only by available memory
- No integer overflow
- Used implicitly in most numeric operations

---

## `float`

### Definition
Represents double-precision floating-point numbers.

### Role
- Approximate real numbers
- Hardware-backed numeric type
- Optimized for performance

**Example:**
```python
x = 0.1 + 0.2
print(x)
```

**Output:**
```text
0.30000000000000004
```

**Notes:**
- Based on IEEE 754
- Precision is finite
- Equality comparisons require care

---

## `complex`

### Definition
Represents complex numbers with real and imaginary parts.

### Role
- Mathematical completeness
- Supports complex arithmetic natively
- No ordering defined

**Example:**
```python
z = 1 + 2j
print(z)
print(z.real, z.imag)
```

**Output:**
```text
(1+2j)
1.0 2.0
```

**Notes:**
- Components are floats
- Cannot be ordered (`<`, `>`)
- Fully supported by numeric operators

---

## `bool`

### Definition
Represents truth values.

### Role
- Logical state representation
- Subtype of `int`
- Integrates with control flow

**Example:**
```python
print(True + True)
print(False * 10)
```

**Output:**
```text
2
0
```

**Notes:**
- `True` equals `1`, `False` equals `0`
- Exists for semantic clarity, not numeric power
- Implicitly used in conditionals
- Truthiness is a language-level concept, not a numeric feature

## Numeric Type Interactions
Python promotes numeric types automatically.

General promotion order:
```text
bool → int → float → complex
```

**Example:**
```python
print(1 + 2.5)
print(1 + 2j)
```

**Output:**
```text
3.5
(1+2j)
```

## Design Notes
- Numeric types are immutable
- Precision and correctness are explicit trade-offs
- Promotion favors generality over strictness
- Exactness (`int`) and approximation (`float`) coexist deliberately

---

## Summary
- `int` provides exact arithmetic
- `float` provides fast approximate arithmetic
- `complex` completes the numeric model
- `bool` integrates truth into numeric operations

This file defines **Python’s numeric type system**, not mathematical theory.