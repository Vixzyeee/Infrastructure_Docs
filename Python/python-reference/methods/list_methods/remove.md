# Remove Methods (`list`)

Methods in this section are used to remove elements from a list.

All methods documented here **modify the list in place**.  
Some methods return the removed element, others return `None`.

---

## `pop()`

### Description
- Removes and returns an element from the list.
- By default, removes the last element.

### Syntax
```python
list.pop([index])
```

**Parameters:**
- `index` (optional) – position of the element to remove

**Return Value:**
- Returns the removed element

**Example:**
```python
numbers = [1, 2, 3]
value = numbers.pop()
print(value)
print(numbers)
```

**Output:**
```text
3
[1, 2]
```

**Example (with index):**
```python
numbers = [1, 2, 3]
value = numbers.pop(0)
print(value)
print(numbers)
```

**Output:**
```text
1
[2, 3]
```

**Notes:**
- Raises IndexError if the list is empty or index is out of range.
- Commonly used when treating a list like a stack.
- If no index is provided, the last element is removed.

---

## `remove()`

### Description
- Removes the first occurrence of a specified value from the list.

### Syntax
```python
list.remove(value)
```

**Parameters:**
- `value` – element to remove

**Return Value:**
- `None`

**Example:**
```python
numbers = [1, 2, 3, 2]
numbers.remove(2)
print(numbers)
```

**Output:**
```text
[1, 3, 2]
```

**Notes:**
- Only removes the first matching value.
- Raises ValueError if the value is not found.
- Does not return the removed element.

---

## `clear()`

### Description
- Removes all elements from the list.

### Syntax
```python
list.clear()
```

**Parameters:**
- None

**Return Value:**
- `None`

**Example:**
```python
numbers = [1, 2, 3]
numbers.clear()
print(numbers)
```

**Output:**
```text
[]
```

**Notes:**
- Empties the list in place.
- Keeps the same list object reference, so all references to the list see the change.

---

## Summary

- Use `pop()` when you need to remove and retrieve an element.
- Use `remove()` when you want to delete an element by value.
- Use `clear()` to empty a list completely.
