# Copying Methods (`set`)

This section covers how to **create a copy of a set**.

Copying is important to avoid **unintended side effects** when modifying data.

---

## `copy()`

### Description
- Creates a **shallow copy** of the set.

### Syntax
```python
set.copy()
```

**Parameters:**
- None

**Return Value:**
- Returns a new `set` object

**Example:**
```python
original = {1, 2, 3}
copied = original.copy()

copied.add(4)

print(original)
print(copied)
```

**Output:**
```text
{1, 2, 3}
{1, 2, 3, 4}
```

**Notes:**
- The returned set is a **new object**
- Changes to the copy do **not** affect the original
- This is a **shallow copy**

## Shallow Copy Behavior
A shallow copy duplicates the **set container**, not the objects inside it.

**Important context for sets:**
- Set elements must be **hashable**
- Most hashable types are immutable
- Therefore, shallow copy is usually **safe** for sets

## Copy vs Assignment

**❌ Assignment (Same Reference)**
```python
a = {1, 2, 3}
b = a

b.add(4)

print(a)
```

**Output:**
```text
{1, 2, 3, 4}
```
Both variables reference the **same set object**.

**✅ Copy (New Object)**
```python
a = {1, 2, 3}
b = a.copy()

b.add(4)

print(a)
```

**Output:**
```text
{1, 2, 3}
```

---

## Summary

- `set.copy()` creates a **new set object**
- It performs a **shallow copy**
- Assignment does **not** create a copy
- Use `copy()` when you want to modify data safely