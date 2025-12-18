# View Objects (`dict`)

This section explains **dictionary view objects** returned by certain dictionary methods.

View objects provide a **dynamic view** of the dictionary’s contents.  
They are **not copies** and **do not store data independently**.

---

## What Are View Objects?

Dictionary view objects are returned by:
- `dict.keys()`
- `dict.values()`
- `dict.items()`

They reflect the **current state** of the dictionary at all times.

---

## Common View Types

## `dict_keys`

- Returned by `dict.keys()`
- Represents a dynamic view of dictionary keys

**Example:**
```python
data = {"a": 1, "b": 2}
keys = data.keys()

data["c"] = 3
print(keys)
```

**Output:**
```text
dict_keys(['a', 'b', 'c'])
```

---

## `dict_values`

- Returned by `dict.values()`
- Represents a dynamic view of dictionary values

**Example:**
```python
data = {"a": 1}
values = data.values()

data["b"] = 2
print(values)
```

**Output:**
```text
dict_values([1, 2])
```

---

## `dict_items`

- Returned by `dict.items()`
- Represents a dynamic view of `(key, value)` pairs

**Example:**
```python
data = {"a": 1}
items = data.items()

data["b"] = 2
print(items)
```

**Output:**
```text
dict_items([('a', 1), ('b', 2)])
```

## Key Characteristics

- View objects **do not copy data**
- Changes to the dictionary are reflected immediately
- View objects are iterable
- View objects support membership testing using `in`

## Converting Views to Lists
If a static snapshot is needed, convert explicitly:
```python
list(data.keys())
list(data.values())
list(data.items())
```
This creates a **separate list copy** that will not change.

---

## Summary

- Dictionary view objects provide a live view of dictionary data.
- They update automatically when the dictionary changes.
- Views are not copies and should not be treated as such.
- Convert to a list when a fixed snapshot is required.