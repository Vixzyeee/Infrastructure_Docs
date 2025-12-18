# Tuple Searching & Indexing (`tuple`)

This section covers methods used to **inspect tuple contents**.

All methods here:
- **Return values**
- **Do not modify** the tuple
- Are safe to use on immutable data structures

These methods are commonly used for:
- Validating fixed-position data
- Inspecting return values from functions
- Working with small, immutable collections

Tuples provide **very limited methods by design**.
These methods focus strictly on **value inspection**, not mutation.

---

## `count()`

### Description
- Counts how many times a value appears in the tuple.

### Syntax
```python
tuple.count(value)
```

**Return Value:**
- Returns an integer (`>= 0`)

**Example:**
```python
data = (1, 2, 2, 3, 2)
print(data.count(2))
```

**Output:**
```text
3
```

**Notes:**
- Performs a full scan of the tuple
- Time complexity: **O(n)**
- Suitable for small or fixed-size tuples
- Prefer sets if frequent membership counting is required
- Returns `0` when the value is not found (no exception is raised)

---

## `index()`

### Description
- Returns the index of the first occurrence of a value.

### Syntax
```python
tuple.index(value[, start[, end]])
```

**Return Value:**
- Returns an integer index
- Raises `ValueError` if the value is not found

**Example:**
```python
data = ("a", "b", "c", "b")
print(data.index("b"))
```

**Output:**
```text
1
```

**Example (with range):**
```python
data = ("a", "b", "c", "b")
print(data.index("b", 2))
```

**Output:**
```text
3
```

### Safe Usage Example
```python
if x in data:
    idx = data.index(x)
```

**Notes:**
- Stops searching at the first match
- Time complexity: **O(n)**
- Always handle `ValueError` when searching user input

---

## Common Mistakes

**❌ Assuming `index()` returns `None`**
```python
idx = data.index("x")  # raises ValueError
```

**❌ Using `index()` for existence checks**
```python
# bad
if data.index(x) >= 0:
```

Use:
```python
x in data
```

**❌ Expecting `index()` to return the last match**
```python
data = ("a", "b", "c", "b")
print(data.index("b"))  # returns 1, not 3
```

---

## Summary

- Tuple methods are **read-only**
- `count()` is used for frequency inspection
- `index()` is used for positional lookup
- Both methods are **linear time**
- Tuples are optimized for **immutability and safety**, not flexibility
- Prefer tuples when data structure should not change