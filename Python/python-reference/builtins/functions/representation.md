# Representation and Conversion Built-in Functions

This file documents **built-in functions related to object representation and value conversion**.

These functions control how values are:
- represented as strings
- converted between numeric bases
- transformed between character and code point forms

They are foundational for debugging, logging, and serialization.

---

## Scope

Covered in this file:
- `repr`
- `ascii`
- `bin`
- `oct`
- `hex`
- `chr`
- `ord`
- `format`

Not covered:
- string formatting syntax
- f-strings
- type-specific formatting methods

---

## `repr()`

### Definition
Returns the **official string representation** of an object.

### Syntax
```python
repr(obj)
```

**Behavior:**
- Aims to be unambiguous
- Often suitable for debugging
- Delegates to `obj.__repr__()`

**Example:**
```python
text = "hello"
print(repr(text))
```

**Output:**
```text
'hello'
```

**Notes:**
- Not intended for end users
- Should uniquely identify the object state by convention, when possible

---

## `ascii()`

### Definition
Returns a string with non-ASCII characters escaped.

### Syntax
```python
ascii(obj)
```

**Behavior:**
- Similar to `repr()`
- Escapes non-ASCII characters using backslash notation

**Example:**
```python
text = "café"
print(ascii(text))
```

**Output:**
```text
'caf\\xe9'
```

**Notes:**
- Useful for logs and ASCII-only environments
- Output is always ASCII-safe

---

## `bin()`

### Definition
Converts an integer to its binary string representation.

### Syntax
```python
bin(x)
```

**Behavior:**
- Prefixes result with `0b`
- Accepts only integers

**Example:**
```python
print(bin(10))
```

**Output:**
```text
0b1010
```

**Notes:**
- Output is a string, not a numeric value
- Intended for inspection and representation, not computation
- Negative values preserve the sign prefix

---

## `oct()`

### Definition
Converts an integer to its octal string representation.

### Syntax
```python
oct(x)
```

**Behavior:**
- Prefixes result with `0o`
- Accepts only integers

**Example:**
```python
print(oct(10))
```

**Output:**
```text
0o12
```

**Notes:**
- Output is a string, not a numeric value
- Primarily used for inspection and legacy or low-level contexts
- Rarely used in modern application logic

---

## `hex()`

### Definition
Converts an integer to its hexadecimal string representation.

### Syntax
```python
hex(x)
```

**Behavior:**
- Prefixes result with `0x`
- Accepts only integers

**Example:**
```python
print(hex(255))
```

**Output:**
```text
0xff
```

**Notes:**
- Output is a string, not a numeric value
- Mainly used for debugging and low-level inspection
- Rarely used in application-level logic

---

## `chr()`

### Definition
Returns the Unicode character for a given code point.

### Syntax
```python
chr(i)
```

**Behavior:**
- Accepts a valid Unicode code point
- Returns a single-character string

**Example:**
```python
print(chr(65))
```

**Output:**
```text
A
```

**Notes:**
- Valid range is `0` to `0x10FFFF`
- Raises `ValueError` for invalid code points

---

## `ord()`

### Definition
Returns the Unicode code point of a character.

### Syntax
```python
ord(c)
```

**Behavior:**
- Accepts a single character string
- Returns an integer

**Example:**
```python
print(ord("A"))
```

**Output:**
```text
65
```

**Notes:**
- Inverse operation of `chr()`
- Raises `TypeError` for strings longer than one character

---

## `format()`

### Definition
Formats a value using a format specification.

### Syntax
```python
format(value, format_spec="")
```

**Behavior:**
- Delegates to `value.__format__()`
- Produces a formatted string representation

**Example:**
```python
print(format(3.14159, ".2f"))
```

**Output:**
```text
3.14
```

**Notes:**
- Formatting rules are type-specific
- This function exposes the formatting protocol, not formatting syntax
- Complex formatting logic belongs to higher-level APIs

---

## Design Notes
- Representation functions separate **debugging output** from **user-facing display**
- Conversion functions expose explicit base transformations
- Formatting is protocol-driven and type-aware

---

## Summary
- `repr` and `ascii` control representation semantics
- `bin`, `oct`, and `hex` expose numeric base conversion
- `chr` and `ord` bridge characters and code points
- `format` provides standardized formatting hooks

This file defines **Python’s representation and conversion primitives**, not string formatting syntax.