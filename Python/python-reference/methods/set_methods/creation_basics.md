# Creation & Basic Operations (`set`)

This section covers **how to create a set** and its **core behaviors**.

These concepts are fundamental.  
Misunderstanding them leads to subtle logic bugs.

---

## What Is a Set?

A `set` is a collection that is:
- **Unordered**
- **Mutable**
- Contains **unique elements only**
- Elements must be **hashable**

Sets are commonly used for:
- Membership testing
- Deduplication
- Set algebra (union, intersection, etc.)

---

## Creating a Set

### Using `set()`

#### Syntax
```python
set(iterable)
```

**Parameters:**
- `iterable` – any iterable object (list, tuple, string, etc.)

**Return Value:**
- Returns a new `set` **object**

**Example:**
```python
numbers = set([1, 2, 3, 3])
print(numbers)
```

**Output:**
```text
{1, 2, 3}
```

**Notes:**
- Duplicate values are automatically removed
- Order is not preserved

## Empty Set Pitfall

### ❌ Incorrect
```python
empty = {}
```
This creates a **dictionary**, not a set.

### ✅ Correct
```python
empty = set()
```

**Notes:**
- `{}` is always a `dict`
- An empty set must be created using `set()`
- This design choice exists because `{}` was reserved for dictionaries

---

## Automatic Uniqueness
Sets **enforce uniqueness** by design.

**Example:**
```python
data = {1, 2, 2, 3, 3, 3}
print(data)
```

**Output:**
```text
{1, 2, 3}
```

**Notes:**
- No error is raised
- Duplicates are silently discarded

---

## Unordered Nature
Sets do **not** preserve insertion order.

**Example:**
```python
s = {"a", "b", "c"}
print(s)
```

**Output:**
```text
{'b', 'a', 'c'}
```

**Notes:**
- Do not rely on order
- If order matters, use `list` instead
- Never use set indexing (`set[0]`) — it does not exist

---

## Membership Testing

#### Syntax
```python
value in set
value not in set
```

**Example:**
```python
users = {"admin", "editor", "viewer"}

print("admin" in users)
print("guest" in users)
```

**Output:**
```text
True
False
```

**Notes:**
- Membership checks are **O(1)** average time
- One of the main reasons to use a set
- Use sets when **uniqueness and fast lookup** matter more than order

---

## Length of a Set

#### Syntax
```python
len(set)
```

**Example:**
```python
items = {1, 2, 3}
print(len(items))
```

**Output:**
```text
3
```

---

## Hashable Elements Requirement
Elements in a set **must be hashable**.

### ✅ Valid Elements
- `int`
- `float`
- `str`
- `tuple` (if it contains only hashable elements)

### ❌ Invalid Elements
- `list`
- `dict`
- `set`

**Example (Invalid):**
```python
s = {[1, 2, 3]}
```

**Result:**
```text
TypeError: unhashable type: 'list'
```

**✅ Valid Example (Tuple Elements)**
```python
s = {(1, 2), (3, 4)}
print(s)
```

**Result:**
```text
{(1, 2), (3, 4)}
```

**Notes:**
- `tuple` is hashable **only if all its elements are hashable**
- The order of elements is **not guaranteed**
- This makes tuples suitable as set elements, unlike lists

---

## Summary
- Use `set()` to create sets
- `{}` creates a dictionary, not a set
- Sets store **unique** elements only
- Sets are **unordered**
- Membership checks are fast and efficient
- Elements must be **hashable**

This file defines the **core mental model** for working with sets.