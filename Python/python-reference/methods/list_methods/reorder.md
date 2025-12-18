# Reorder Methods (`list`)

Methods in this section are used to change the order of elements in a list.

All methods documented here **modify the list in place**.

---

## `reverse()`

### Description
- Reverses the order of elements in the list.

### Syntax
```python
list.reverse()
```

**Parameters:**
- None

**Return Value:**
- `None`

**Example:**
```python
numbers = [1, 2, 3, 4]
numbers.reverse()
print(numbers)
```

**Output:**
```text
[4, 3, 2, 1]
```

**Notes:**
- Modifies the list in place.
- Faster and more memory-efficient than slicing (`[::-1]`) for large lists.
- Does not create a new list.

---

## `sort()`

### Description
- Sorts the elements of the list in ascending order by default.

### Syntax
```python
list.sort(key=None, reverse=False)
```

**Parameters:**
- `key` (optional) – function that serves as a key for comparison
- `reverse` (optional) – if `True`, sorts the list in descending order

**Return Value:**
- `None`

**Example:**
```python
numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)
```

**Output:**
```text
[1, 2, 3, 4]
```

**Example (descending order):**
```python
numbers = [3, 1, 4, 2]
numbers.sort(reverse=True)
print(numbers)
```

**Output:**
```text
[4, 3, 2, 1]
```

**Example (using key):**
```python
words = ["apple", "Banana", "cherry"]
words.sort(key=str.lower)
print(words)
```

**Output:**
```text
['apple', 'Banana', 'cherry']
```

**Notes:**
- Modifies the list in place.
- Returns `None`.
- Use `sorted()` if you need a new sorted list without modifying the original.
- All elements must be comparable, otherwise a `TypeError` is raised.

---

## Summary

- Use `reverse()` to reverse a list in place.
- Use `sort()` to reorder elements permanently.
- Use `sorted()` when you want a sorted copy instead of modifying the original list.
