# Text and Binary Types

This file documents **Python’s built-in text and binary data types**.

These types define how Python represents:
- human-readable text
- raw binary data
- views over existing memory

Clear separation between text and binary data is a core design principle.

---

## Scope

Covered in this file:
- `str`
- `bytes`
- `bytearray`
- `memoryview`

Not covered:
- encoding libraries
- file I/O behavior
- networking protocols

---

## Text vs Binary Model

Python enforces a strict separation:
- **Text** represents characters
- **Binary** represents bytes

Mixing the two implicitly is not allowed.
Conversion requires explicit encoding or decoding.

---

## `str`

### Definition
Represents immutable sequences of Unicode characters.

### Role
- Primary text type
- Human-readable data
- Language-level string representation

**Example:**
```python
text = "hello"
print(text)
```

**Output:**
```text
hello
```

**Notes:**
- Immutable
- Stores Unicode code points
- Encoding is not part of `str` itself

---

## `bytes`

### Definition
Represents immutable sequences of bytes.

### Role
- Raw binary data
- File and network payloads
- Explicitly encoded data

**Example:**
```python
data = b"hello"
print(data)
```

**Output:**
```text
b'hello'
```

**Notes:**
- Immutable
- Elements are integers in range 0–255
- Not interchangeable with `str`
- Byte literals and constructor semantics differ, but both produce the same type

---

## `bytearray`

### Definition
Represents mutable sequences of bytes.

### Role
- In-place modification of binary data
- Efficient buffer manipulation

**Example:**
```python
data = bytearray(b"hello")
data[0] = 72
print(data)
```

**Output:**
```text
bytearray(b'Hello')
```

**Notes:**
- Mutable
- Same element semantics as `bytes`
- Useful for incremental binary processing

---

## `memoryview`

### Definition
Provides a view into the memory of another object.

### Role
- Zero-copy access to binary data
- Efficient data sharing
- Low-level buffer manipulation

**Example:**
```python
data = bytearray(b"hello")
view = memoryview(data)
view[0] = 72
print(data)
```

**Output:**
```text
bytearray(b'Hello')
```

**Notes:**
- Does not copy data
- Reflects changes in the underlying object
- Requires buffer-protocol support
- Exists to avoid copying large binary data across APIs

---

## Encoding and Decoding
Text and binary data are connected via encoding.  
Encoding errors are runtime failures, not implicit conversions.

**Example:**
```python
text = "hello"
data = text.encode("utf-8")
print(data)
```

**Output:**
```text
b'hello'
```
Decoding reverses the process.

---

## Design Notes
- Text and binary data are deliberately separated
- Explicit conversion avoids ambiguity
- Mutability is restricted to binary containers
- `memoryview` enables performance-critical workflows

---

## Summary
- `str` represents Unicode text
- `bytes` represents immutable binary data
- `bytearray` allows mutable binary buffers
- `memoryview` exposes zero-copy memory access

This file defines **Python’s text and binary data model**, not encoding practices.