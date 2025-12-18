# Remove Methods (`dict`)

Methods in this section are used to **remove keys and values** from a dictionary.

All methods documented here **modify the dictionary in place**.
Some methods return removed data, others return `None`.

---

## `pop()`

### Description
- Removes a specified key from the dictionary.
- Returns the corresponding value.

### Syntax
```python
dict.pop(key[, default])
```

**Parameters:**
- `key` – key to remove
- `default` (optional) – value to return if the key does not exist

**Return Value:**
- Returns the value associated with the removed key
- Returns `default` if the key does not exist and `default` is provided

**Example:**
```python
data = {"name": "Pito", "age": 21}

value = data.pop("age")
print(value)
print(data)
```

**Output:**
```text
21
{'name': 'Pito'}
```

**Example (with default):**
```python
data = {"name": "Pito"}

value = data.pop("email", "not found")
print(value)
print(data)
```

**Output:**
```text
not found
{'name': 'Pito'}
```

**Notes:**
- Raises `KeyError` if the key does not exist and no default is provided.
- Commonly used when you need both removal and the value.

---

## `popitem()`

### Description
- Removes and returns the **last inserted** key-value pair.

### Syntax
```python
dict.popitem()
```

**Parameters:**
- None

**Return Value:**
- Returns a tuple `(key, value)`

**Example:**
```python
data = {"a": 1, "b": 2}

item = data.popitem()
print(item)
print(data)
```

**Output:**
```text
('b', 2)
{'a': 1}
```

**Notes:**
- Raises `KeyError` if the dictionary is empty.
- Since Python 3.7+, removal order follows **insertion order**.
- Often used when treating a dictionary like a stack.

---

## `clear()`

### Description
- Removes all items from the dictionary.

### Syntax
```python
dict.clear()
```

**Parameters:**
- None

**Return Value:**
- `None`

**Example:**
```python
data = {"a": 1, "b": 2}
data.clear()
print(data)
```

**Output:**
```text
{}
```

**Notes:**
- Empties the dictionary in place.
- Keeps the same dictionary object reference.
- All references to the dictionary see the change.

---

## Summary

- Use `pop()` to remove a specific key and retrieve its value.
- Use `popitem()` to remove the most recently inserted item.
- Use `clear()` to empty the dictionary entirely.
- All methods in this section modify the dictionary in place.
