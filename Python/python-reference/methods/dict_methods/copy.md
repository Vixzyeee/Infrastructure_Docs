# Copying Methods (`dict`)

Methods in this section are used to create copies of a dictionary.

These methods create **shallow copies** and **do not modify the original dictionary**.

---

## `copy()`

### Description
- Creates a shallow copy of the dictionary.
- The returned dictionary is a **new object** with the same key-value pairs.

### Syntax
```python
dict.copy()
```

**Parameters:**
- None

**Return Value:**
- Returns a new dictionary object

**Example:**
```python
original = {"a": 1, "b": 2}
copied = original.copy()

copied["c"] = 3

print(original)
print(copied)
```

**Output:**
```text
{'a': 1, 'b': 2}
{'a': 1, 'b': 2, 'c': 3}
```

---

## Shallow Copy Behavior

A shallow copy duplicates the dictionary structure, not the nested objects themselves.

**Example:**
```python
original = {"numbers": [1, 2, 3]}
copied = original.copy()

copied["numbers"].append(4)

print(original)
print(copied)
```

**Output:**
```text
{'numbers': [1, 2, 3, 4]}
{'numbers': [1, 2, 3, 4]}
```

**Notes:**
- The dictionary object itself is copied.
- Nested mutable objects are **shared** between the original and the copy.
- Use `copy.deepcopy()` to fully duplicate nested objects.

---

## Summary

- `copy()` creates a shallow copy of a dictionary.
- The returned dictionary is a new object.
- Nested mutable values remain shared.
- Use deep copy when independent nested data is required.
