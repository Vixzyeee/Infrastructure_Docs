# Sequence Types

This file documents **Python’s built-in sequence types**.

Sequence types define:
- ordered collections
- positional access
- slicing semantics

They participate in the **sequence protocol**, which underpins iteration,
indexing, and many built-in operations.

---

## Scope

Covered in this file:
- `list`
- `tuple`
- `range`
- `slice`

Not covered:
- sequence methods
- iteration syntax
- sequence operators

---

## Sequence Model Overview

A sequence in Python is defined by:
- a well-defined order
- zero-based indexing
- support for slicing

Not all sequences are mutable, and not all sequences store concrete elements.

---

## `list`

### Definition
A mutable, ordered collection of objects.

### Role
- General-purpose container
- Dynamic sizing
- Supports in-place modification

**Example:**
```python
items = [1, 2, 3]
items[0] = 10
print(items)
```

**Output:**
```text
[10, 2, 3]
```

**Notes:**
- Elements can be of mixed types
- Backed by a dynamic array
- Mutation affects all references
- Assignment and mutation affect all references to the same list object

---

## `tuple`

### Definition
An immutable, ordered collection of objects.

### Role
- Fixed structure
- Safe for use as dictionary keys when all elements are hashable, due to immutability
- Often used for grouping related values

**Example:**
```python
point = (1, 2)
print(point[0])
```

**Output:**
```text
1
```

**Notes:**
- Immutability is structural, not recursive
- Enables hashing and safe reuse
- Often optimized by the interpreter

---

## `range`

### Definition
Represents an arithmetic progression of integers.

### Role
- Memory-efficient numeric sequences
- Commonly used for iteration
- Does not store all values explicitly

**Example:**
```python
r = range(0, 5)
print(list(r))
```

**Output:**
```text
[0, 1, 2, 3, 4]
```

**Notes:**
- Lazy and immutable
- Supports indexing and slicing
- Values are computed on demand

---

## `slice`

### Definition
Represents a slicing specification.

### Role
- Encapsulates start, stop, and step
- Used internally by slicing syntax
- Can be constructed explicitly

**Example:**
```python
s = slice(1, 5, 2)
print(s.start, s.stop, s.step)
```

**Output:**
```text
1 5 2
```

**Notes:**
- Used by `__getitem__` implementations
- Separates slicing logic from containers
- Rarely instantiated directly in application code
- `slice` represents slicing intent, not the slicing operation itself

---

## Indexing Semantics
Indexing rules shared by sequence types:
- Zero-based indexing
- Negative indices count from the end
- Raises `IndexError` when out of range

**Example:**
```python
seq = [10, 20, 30]
print(seq[-1])
```

**Output:**
```text
30
```

---

## Slicing Semantics
Slicing produces a subsequence.

Rules:
- Start is inclusive
- Stop is exclusive
- Step controls stride direction and size

**Example:**
```python
seq = [0, 1, 2, 3, 4, 5]
print(seq[1:5:2])
```

**Output:**
```text
[1, 3]
```

## Design Notes
- Sequence types separate order from mutability
- Slicing is a first-class language concept
- `range` demonstrates sequence behavior without storage
- `slice` exists to expose slicing as data

## Summary
- Sequence types define ordered access
- Mutability varies by type
- Indexing and slicing follow consistent rules
- Protocols matter more than concrete storage

This file defines **Python’s sequence model**, not container APIs.