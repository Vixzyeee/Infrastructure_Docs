# Ordering and Aggregation Built-in Functions

This file documents **built-in functions related to ordering and aggregation**.

These functions operate on iterables to:
- select extreme values
- aggregate numeric data
- reorder elements

They are protocol-driven and work with any iterable that provides comparable elements.

---

## Scope

Covered in this file:
- `max`
- `min`
- `sum`
- `sorted`
- `reversed`

Not covered:
- comparison operators
- custom sorting algorithms
- ordering methods on specific types

---

## `max()`

### Definition
Returns the largest item in an iterable or among multiple arguments.

### Syntax
```python
max(iterable, *, key=None, default=...)
max(arg1, arg2, *args, key=None)
```

**Behavior:**
- Compares elements using ordering semantics
- `key` transforms values before comparison
- `default` is returned for empty iterables

**Example:**
```python
print(max([3, 1, 5]))
print(max(["apple", "banana"], key=len))
```

**Output:**
```text
5
banana
```

**Notes:**
- Raises `ValueError` for empty iterables without `default`
- Does not sort the entire iterable
- Comparison cost depends on element type

---

## `min()`

### Definition
Returns the smallest item in an iterable or among multiple arguments.

### Syntax
```python
min(iterable, *, key=None, default=...)
min(arg1, arg2, *args, key=None)
```

**Behavior:**
- Semantically identical to `max()` with inverted comparison
- Supports `key` and `default`

**Example:**
```python
print(min([3, 1, 5]))
print(min(["apple", "banana"], key=len))
```

**Output:**
```text
1
apple
```

**Notes:**
- Same performance characteristics as `max()`
- Comparison must be well-defined for elements

---

## `sum()`

### Definition
Aggregates values by repeated addition.

### Syntax
```python
sum(iterable, start=0)
```

**Behavior:**
- Adds elements sequentially
- Uses `start` as the initial value
- Returns the accumulated result

**Example:**
```python
print(sum([1, 2, 3]))
print(sum([1, 2, 3], 10))
```

**Output:**
```text
6
16
```

**Notes:**
- Intended for numeric data
- Inefficient for string or sequence concatenation
- Precision depends on numeric type

---

## `sorted()`

### Definition
Returns a new sorted list from an iterable.

### Syntax
```python
sorted(iterable, *, key=None, reverse=False)
```

**Behavior:**
- Always returns a list
- Stable sort (preserves relative order)
- Does not mutate the original iterable

**Example:**
```python
print(sorted([3, 1, 2]))
print(sorted(["apple", "banana"], key=len))
```

**Output:**
```text
[1, 2, 3]
['apple', 'banana']
```

**Notes:**
- Uses Timsort
- Stability enables multi-pass sorting
- Memory cost proportional to input size

---

## `reversed()`

### Definition
Returns an iterator that yields elements in reverse order.

### Syntax
```python
reversed(sequence)
```

**Behavior:**
- Requires a reversible sequence
- Produces a lazy iterator
- Does not copy elements

**Example:**
```python
print(list(reversed([1, 2, 3])))
```

**Output:**
```text
[3, 2, 1]
```

**Notes:**
- Not all iterables support reversal
- Prefer over slicing for large sequences
- Works with sequences implementing the reverse protocol

---

## Design Notes
- These functions separate **ordering** from **storage**
- They operate on any compatible iterable
- Laziness and stability are intentional design choices
- Performance depends on comparison cost, not just size
- These functions do not enforce ordering semantics, they rely on them.

---

## Summary
- `max` and `min` select extreme values without sorting
- `sum` aggregates numeric data
- `sorted` provides stable ordering
- `reversed` enables lazy reverse traversal

This file defines **Python’s ordering and aggregation primitives**, not sorting theory.