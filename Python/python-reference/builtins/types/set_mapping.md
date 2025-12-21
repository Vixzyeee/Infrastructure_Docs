# Set and Mapping Types

This file documents **Python’s built-in set and mapping types**.

These types define:
- uniqueness guarantees
- hash-based lookup
- unordered collection semantics

They are fundamental to Python’s data model and performance characteristics.

---

## Scope

Covered in this file:
- `set`
- `frozenset`
- `dict`

Not covered:
- set or dictionary methods
- ordering guarantees in specific Python versions
- algorithmic complexity details

---

## Hash-Based Model Overview

Set and mapping types rely on:
- object hashing
- equality comparison
- immutable keys

Correct behavior depends on consistent implementations of `__hash__` and `__eq__`.

---

## `set`

### Definition
A mutable, unordered collection of unique elements.

### Role
- Enforces uniqueness
- Supports fast membership testing
- Represents mathematical sets

**Example:**
```python
items = {1, 2, 2, 3}
print(items)
```

**Output:**
```text
{1, 2, 3}
```

**Notes:**
- Elements must be hashable
- No guaranteed order
- Optimized for membership checks

---

## `frozenset`

### Definition
An immutable version of `set`.

### Role
- Hashable set container
- Safe for use as dictionary keys or set elements
- Represents fixed collections of unique values

**Example:**
```python
fs = frozenset([1, 2, 3])
print(fs)
```

**Output:**
```text
frozenset({1, 2, 3})
```

**Notes:**
- Cannot be modified after creation
- Shares most behavior with `set`
- Exists primarily for immutability and hashing

---

## `dict`

### Definition
A mapping of unique keys to values.

### Role
- Core key-value data structure
- Fast lookup by key
- Central to Python’s object model and namespace management

**Example:**
```python
user = {"name": "admin", "id": 1}
print(user["name"])
```

**Output:**
```text
admin
```

**Notes:**
- Keys must be hashable
- Values can be any object
- Lookup is based on hash, not order

---

## Key Constraints

For set and dictionary keys:
- Keys must be immutable
- Hash value must not change over lifetime
- Equality and hash must agree

Violation of these rules leads to undefined behavior at the language level.

---

## Equality vs Identity

Set and mapping behavior depends on:
- `__hash__` for bucket placement
- `__eq__` for equality resolution

Object identity is irrelevant to set and dict behavior unless it affects equality or hashing.

---

## Design Notes
- These types trade ordering for performance
- Hashing enables constant-time average access
- Immutability enables correctness
- Mappings generalize sets by associating values
- Lack of order is a semantic property, not an implementation accident

---

## Summary
- `set` enforces uniqueness
- `frozenset` provides immutable sets
- `dict` maps keys to values
- Hashing underpins their behavior

This file defines **Python’s hash-based collection model**, not usage patterns.