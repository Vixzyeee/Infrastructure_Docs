# Add & Modify Methods (`list`)

Methods in this section are used to add new elements or modify existing list contents.

All methods documented here **modify the list in place** and return `None`.

---

## `append()`

### Description
- Adds a single element to the end of the list.

### Syntax
```python
list.append(item)
```

**Parameters:**
- `item` – element to be added to the list

**Return Value:**
- `None`

**Example:**
```python
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)
```

**Output:**
```text
[1, 2, 3, 4]
```

**Notes:**
- Only one element can be added at a time.
- To add multiple elements, use `extend()`.

---

## `extend()`

### Description
- Adds all elements from an iterable to the end of the list.

### Syntax
```python
list.extend(iterable)
```

**Parameters:**
- `iterable` – any iterable object (list, tuple, set, etc.)

**Return Value:**
- `None`

**Example:**
```python
numbers = [1, 2]
numbers.extend([3, 4, 5])
print(numbers)
```

**Output:**
```text
[1, 2, 3, 4, 5]
```

**Notes:**
- Each element of the iterable is added individually.
- Extending with a string will add each character separately.

---

## `insert()`

### Description
- Inserts an element at a specific index in the list.

### Syntax
```python
list.insert(index, item)
```

**Parameters:**
- `index` – position where the element should be inserted
- `item` – element to insert

**Return Value:**
- `None`

**Example:**
```python
numbers = [1, 3, 4]
numbers.insert(1, 2)
print(numbers)
```

**Output:**
```text
[1, 2, 3, 4]
```

**Notes:**
- Existing elements are shifted to the right.
- If index is out of range, the element is added at the start or end.
- Inserting near the beginning of large lists can be inefficient due to element shifting.

---

## Summary

- Use `append()` to add a single element to the end of a list.
- Use `extend()` to add multiple elements from another iterable.
- Use `insert()` when element position matters.
