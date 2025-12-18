# Set Algebra Methods (`set`)

This section covers **set algebra operations**.

These methods are the **core strength of sets** and distinguish them from lists and dictionaries.

Set algebra is commonly used for:
- Comparing collections
- Filtering data
- Permission and role checks
- Logical operations on groups of values

---

## `union()`

### Description
- Returns a new set containing **all unique elements** from both sets.

### Syntax
```python
set.union(other)
```

**Return Value:**
- Returns a new set

**Example:**
```python
a = {1, 2, 3}
b = {3, 4, 5}

result = a.union(b)
print(result)
```

**Output:**
```text
{1, 2, 3, 4, 5}
```

**Notes:**
- Does not modify the original sets
- Equivalent operator: `|`

---

## `intersection()`

### Description
- Returns a new set containing elements **common to both sets**.

### Syntax
```python
set.intersection(other)
```

**Return Value:**
- Returns a new set

**Example:**
```python
a = {1, 2, 3}
b = {2, 3, 4}

result = a.intersection(b)
print(result)
```

**Output:**
```text
{2, 3}
```

**Notes:**
- Useful for finding overlaps
- Equivalent operator: `&`

---

## `difference()`

### Description
- Returns a new set containing elements that exist in the first set but `not` in the other.

### Syntax
```python
set.difference(other)
```

**Return Value:**
- Returns a new set

**Example:**
```python
a = {1, 2, 3}
b = {2, 4}

result = a.difference(b)
print(result)
```

**Output:**
```text
{1, 3}
```

**Notes:**
- Order matters (`a - b` ≠ `b - a`)
- Equivalent operator: `-`
- This operation is not symmetric

---

## `symmetric_difference()`

### Description
- Returns a new set containing elements that are in **either set, but not both**.

### Syntax
```python
set.symmetric_difference(other)
```

**Return Value:**
- Returns a new set

**Example:**
```python
a = {1, 2, 3}
b = {3, 4, 5}

result = a.symmetric_difference(b)
print(result)
```

**Output:**
```text
{1, 2, 4, 5}
```

**Notes:**
- Excludes common elements
- Equivalent operator: `^`

---

## In-Place Algebra Methods
These methods **modify the set directly** instead of returning a new one.

## `update()` (Union In-Place)
```python
set.update(other)
```

**Example:**
```python
a = {1, 2}
a.update({2, 3})

print(a)
```

**Output:**
```text
{1, 2, 3}
```

## `intersection_update()`
```python
set.intersection_update(other)
```

**Example:**
```python
a = {1, 2, 3}
a.intersection_update({2, 3, 4})

print(a)
```

**Output:**
```text
{2, 3}
```

## `difference_update()`
```python
set.difference_update(other)
```

**Example:**
```python
a = {1, 2, 3}
a.difference_update({2})

print(a)
```

**Output:**
```text
{1, 3}
```

## `symmetric_difference_update()`
```python
set.symmetric_difference_update(other)
```

**Example:**
```python
a = {1, 2, 3}
a.symmetric_difference_update({3, 4})

print(a)
```

**Output:**
```text
{1, 2, 4}
```

## Method vs Operator Summary

| Operation            | Method                   | Operator |
|----------------------|:-------------------------|----------|
| Union                | `union()`                |          |`|`|
| Intersection         | `intersection()`         | `&`      |
| Difference           | `difference()`           | `-`      |
| Symmetric Difference | `symmetric_difference()` | `^`      |

## Choosing Between Method and Operator

- Use **methods** for clarity and readability
- Use **operators** for concise expressions
- Prefer methods in documentation and shared codebases

---

## Summary

- Set algebra operations return **new sets** by default
- In-place variants modify the original set
- Operators are shorthand equivalents of methods
- These operations are the primary reason to use sets