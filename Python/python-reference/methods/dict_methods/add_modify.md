# Add & Modify Methods (`dict`)

Methods in this section are used to **add new key-value pairs** or **modify existing data** in a dictionary.

All methods documented here **modify the dictionary in place**.

---

## `setdefault()`

### Description
- Returns the value of a key if it exists.
- If the key does not exist, inserts the key with a default value and returns that value.

### Syntax
```python
dict.setdefault(key[, default])
```

**Parameters:**
- `key` – key to look up or insert
- `default` (optional) – value to set if the key does not exist (default: `None`)

**Return Value:**
- Returns the value associated with the key
- Returns `default` if the key was newly inserted

**Example:**
```python
data = {"name": "Pito"}

value = data.setdefault("name", "Anonymous")
print(value)
print(data)

value = data.setdefault("age", 21)
print(value)
print(data)
```

**Output:**
```text
Pito
{'name': 'Pito'}
21
{'name': 'Pito', 'age': 21}
```

**Notes:**
- Modifies the dictionary **only if the key does not exist**.
- Often used to initialize missing keys.
- Be careful when using mutable defaults (e.g. lists or dicts).

---

## `update()`

### Description
- Updates the dictionary with key-value pairs from another mapping or iterable.
- Existing keys are overwritten.

### Syntax
```python
dict.update([other])
```

**Parameters:**
- `other` – another dictionary or iterable of key-value pairs

**Return Value:**
- `None`

**Example (with dictionary):**
```python
data = {"name": "Pito"}
data.update({"age": 21, "role": "engineer"})
print(data)
```

**Output:**
```text
{'name': 'Pito', 'age': 21, 'role': 'engineer'}
```

**Example (with iterable):**
```python
data = {"a": 1}
data.update([("b", 2), ("c", 3)])
print(data)
```

**Output:**
```text
{'a': 1, 'b': 2, 'c': 3}
```

**Notes:**
- Existing keys are silently overwritten.
- Commonly used for merging dictionaries.
- Equivalent to multiple assignments using `dict[key] = value`.

---

## Summary

- Use `setdefault()` to safely initialize missing keys.
- Use `update()` to merge or bulk-update dictionary data.
- Both methods **modify the dictionary in place**.
- Neither method returns the updated dictionary.