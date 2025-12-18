# Remove Methods (`set`)

This section covers methods used to **remove elements** from a set.

All methods here **modify the set in place**, but their behavior differs significantly when elements are missing.

Choosing the wrong method can cause **unexpected errors**.

---

## `remove()`

### Description
- Removes a specified element from the set.

### Syntax
```python
set.remove(element)
```

**Parameters:**
- `element` – the element to remove

**Return Value:**
- `None`

**Example:**
```python
items = {1, 2, 3}
items.remove(2)

print(items)
```

**Output:**
```text
{1, 3}
```

**Error Case:**
```python
items.remove(99)
```

**Result:**
```text
KeyError: 99
```

**Notes:**
- Raises `KeyError` if the element does not exist
- Use only when you are certain the element is present
- Useful when missing data should be treated as a bug

---

## `discard()`

### Description
- Removes a specified element from the set **if it exists**.

### Syntax
```python
set.discard(element)
```

**Parameters:**
- `element` – the element to remove

**Return Value:**
- `None`

**Example:**
```python
items = {1, 2, 3}
items.discard(2)

print(items)
```

**Output:**
```text
{1, 3}
```

**Missing Element Case:**
```python
items.discard(99)
print(items)
```

**Output:**
```text
{1, 3}
```

**Notes:**
- Does **not** raise an error if the element is missing
- Safe for cleanup operations
- Preferred when absence is acceptable

---

## `pop()`

### Description
- Removes and returns an **arbitrary** element from the set.

### Syntax
```python
set.pop()
```

**Parameters:**
- None

**Return Value:**
- Returns the removed element

**Example:**
```python
items = {1, 2, 3}
value = items.pop()

print(value)
print(items)
```

**Output:**
```text
2
{1, 3}
```

**Empty Set Case:**
```python
empty = set()
empty.pop()
```

**Result:**
```text
KeyError: 'pop from an empty set'
```

**Notes:**
- The removed element is **not predictable**
- Do not rely on which element is removed
- Mainly used for iterative consumption
- Commonly used when repeatedly processing and emptying a set

---

## `clear()`

### Description
- Removes **all elements** from the set.

### Syntax
```python
set.clear()
```

**Parameters:**
- None

**Return Value:**
- `None`

**Example:**
```python
items = {1, 2, 3}
items.clear()

print(items)
```

**Output:**
```text
set()
```

**Notes:**
- Empties the set in place
- Does not delete the set object itself

---

## Comparison Summary

| Method       | Removes           | Missing Element  | Returns | Common Use        |
|--------------|:------------------|------------------|---------|-------------------|
| `remove()`   | specific element  | ❌ error          | `None`  | strict validation |
| `discard()`  | specific element  | ✅ no error       | `None`  | safe cleanup      |
| `pop()`      | arbitrary element | ❌ error if empty | element | consume elements  |
| `clear()`    | all elements      | —                | `None`  | reset state       |

## Common Mistakes

**❌ Using `remove()` when absence is normal**
```python
items.remove(x)
```
Use `discard()` instead if `x` may not exist.

**❌ Expecting `pop()` to remove a specific element**
```python
items.pop()
```
Sets are unordered. The removed element is arbitrary.

---

## Summary

- Use `remove()` when missing elements indicate a bug
- Use `discard()` when removal should be safe
- Use `pop()` when consuming elements arbitrarily
- Use `clear()` to reset a set completely
- All methods modify the set in place