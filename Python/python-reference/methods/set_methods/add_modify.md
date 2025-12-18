# Add & Modify Methods (`set`)

This section covers methods used to **add elements** to a set.

All methods here **modify the set in place** and **do not return a new set**.

---

## `add()`

### Description
- Adds a single element to the set.

### Syntax
```python
set.add(element)
```

**Parameters:**
- `element` – a hashable object to add to the set

**Return Value:**
- `None`

**Example:**
```python
items = {1, 2, 3}
items.add(4)

print(items)
```

**Output:**
```text
{1, 2, 3, 4}
```

**Notes:**
- Only one element can be added at a time
- If the element already exists, nothing happens
- No error is raised for duplicates
- The set is modified in place

---

## `update()`

### Description
- Adds multiple elements from an iterable to the set.

### Syntax
```python
set.update(iterable)
```

**Parameters:**
- `iterable` – any iterable object (list, tuple, set, string, etc.)

**Return Value:**
- `None`

**Example (List):**
```python
items = {1, 2}
items.update([2, 3, 4])

print(items)
```

**Output:**
```text
{1, 2, 3, 4}
```

**Example (String):**
```python
letters = set()
letters.update("hello")

print(letters)
```

**Output:**
```text
{'h', 'e', 'l', 'o'}
```

**Notes:**
- Each element of the iterable is added individually
- Strings are treated as sequences of characters
- Duplicate elements are silently ignored
- The set is modified in place

---

## `add()` vs `update()`

| Method     | Accepts        | Adds           | Common Use          |
|------------|:---------------|----------------|---------------------|
| `add()`    | single element | one item       | adding one value    |
| `update()` | iterable       | multiple items | merging collections |

## Common Mistakes

**❌ Expecting a return value**
```python
result = items.add(5)
print(result)
```

**Output:**
```text
None
```

**❌ Passing multiple elements to `add()`**
```python
items.add(1, 2)
```

**Output:**
```text
TypeError: add() takes exactly one argument (2 given)
```

---

## Summary

- `add()` adds one element
- `update()` adds elements from an iterable
- Both methods modify the set in place
- Both return `None`
- Duplicate values are ignored silently
- Prefer `update()` when merging data from another collection

Use these methods when you want to **grow a set without caring about order or duplicates.**