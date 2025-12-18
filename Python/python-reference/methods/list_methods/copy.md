# Copying Methods (`list`)

Methods in this section are used to create copies of a list.

These methods are useful when you want to duplicate a list without affecting the original object.

---

## `copy()`

### Description
- Creates a shallow copy of the list.

### Syntax
```python
list.copy()
```

**Parameters:**
- None

**Return Value:**
- Returns a new list object containing the same elements.

**Example:**
```python
original = [1, 2, 3]
copied = original.copy()

copied.append(4)

print(original)
print(copied)
```

**Output:**
```text
[1, 2, 3]
[1, 2, 3, 4]
```

**Notes:**
- The returned list is a **new object**.
- Only the list itself is copied; nested objects are shared (shallow copy).
- Changes to mutable elements inside the list will affect both lists.
- Use `copy.deepcopy()` for a full deep copy of nested objects.

---