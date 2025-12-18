# Access & Query Methods (`dict`)

Methods in this section are used to **access data** from a dictionary or **query its contents**.

These methods **do not modify the dictionary**.  
They are safe to use for reading operations.

---

## `get()`

### Description
- Returns the value for a given key.
- If the key does not exist, returns a default value instead of raising an error.

### Syntax
```python
dict.get(key[, default])
```

**Parameters:**
- `key` – key to look up
- `default` (optional) – value to return if the key is not found (default: `None`)

**Return Value:**
- Returns the value associated with the key
- Returns default if the key does not exist

**Example:**
```python
data = {"name": "Pito", "age": 21}

print(data.get("name"))
print(data.get("email"))
print(data.get("email", "not provided"))
```

**Output:**
```text
Pito
None
not provided
```

**Notes:**
- Preferred over `dict[key]` when the key may not exist.
- Does **not** raise `KeyError`.
- Commonly used for safe reads and configuration lookups.
- Unlike `dict[key]`, `get()` never raises `KeyError`.

---

## `keys()`

### Description
- Returns a view object containing all keys in the dictionary.

### Syntax
```python
dict.keys()
```

**Parameters:**
- None

**Return Value:**
- Returns a `dict_keys` view object

**Example:**
```python
data = {"a": 1, "b": 2}

keys = data.keys()
print(keys)
```

**Output:**
```text
dict_keys(['a', 'b'])
```

**Notes:**
- The returned object is a **view**, not a list.
- Reflects changes to the dictionary in real time.
- Convert to a list explicitly if needed:
    ```python
    list(data.keys())
    ```

---

## `values()`

### Description
- Returns a view object containing all values in the dictionary.

### Syntax
```python
dict.values()
```

**Parameters:**
- None

**Return Value:**
- Returns a `dict_values` view object

**Example:**
```python
data = {"a": 1, "b": 2}

values = data.values()
print(values)
```

**Output:**
```text
dict_values([1, 2])
```

**Notes:**
- Returns values only, without keys.
- Order follows insertion order of the dictionary.
- Changes to the dictionary are reflected in the view.

---

## `items()`

### Description
- Returns a view object containing key-value pairs as tuples.

### Syntax
```python
dict.items()
```

**Parameters:**
- None

**Return Value:**
- Returns a `dict_items` view object containing `(key, value)` tuples

**Example:**
```python
data = {"a": 1, "b": 2}

items = data.items()
print(items)
```

**Output:**
```text
dict_items([('a', 1), ('b', 2)])
```

**Notes:**
- Commonly used for iteration:
    ```python
    for key, value in data.items():
        print(key, value)
    ```
- The returned object is a live view, not a snapshot.

---

## Summary

- Use `get()` for safe value access without risking `KeyError`.
- Use `keys()`, `values()`, and `items()` to inspect dictionary contents.
- All methods in this section **do not modify** the dictionary.
- View objects reflect changes to the dictionary dynamically.
