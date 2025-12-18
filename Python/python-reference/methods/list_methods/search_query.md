# Search & Query Methods (`list`)

Methods in this section are used to query information from a list.

These methods **do not modify the list**.  
They are commonly used to locate elements or count occurrences.

---

## `index()`

### Description
- Returns the index of the first occurrence of a specified value.

### Syntax
```python
list.index(value[, start[, end]])
```

**Parameters:**
- `value` – element to search for
- `start` (optional) – starting index for the search
- `end` (optional) – ending index for the search

**Return Value:**
- Returns the index of the first matching element

**Example:**
```python
numbers = [1, 2, 3, 2]
idx = numbers.index(2)
print(idx)
```

**Output:**
```text
1
```

**Example (with index):**
```python
numbers = [1, 2, 3, 2]
idx = numbers.index(2, 2)
print(idx)
```

**Output:**
```text
3
```

**Notes:**
- Raises `ValueError` if the value is not found.
- Always returns the first match within the specified range.
- Commonly paired with `in` to avoid exceptions.

---

## `count()`

### Description
- Counts how many times a specified value appears in the list.

### Syntax
```python
list.count(value)
```

**Parameters:**
- `value` – element to count

**Return Value:**
- Returns the number of occurrences

**Example:**
```python
numbers = [1, 2, 3, 2, 2]
count = numbers.count(2)
print(count)
```

**Output:**
```text
3
```

**Notes:**
- Returns `0` if the value is not found.
- Does not raise exceptions.
- Useful for quick frequency checks.

---

## Summary

- Use `index()` when you need the position of an element.
- Use `count()` when you need to know how often a value appears.
- Use `in` before `index()` when the value may not exist.
