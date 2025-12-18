# Set Relations & Comparison (`set`)

This section covers methods used to **compare relationships between sets**.

All methods here **return boolean values** and **do not modify** the original sets.

These methods are commonly used for:
- Permission checks
- Role validation
- Feature flag logic
- Access control rules

---

## `issubset()`

### Description
- Checks whether all elements of a set exist in another set.

### Syntax
```python
set.issubset(other)
```

**Return Value:**
- Returns `True` or `False`

**Example:**
```python
required = {"read", "write"}
user_perms = {"read", "write", "delete"}

print(required.issubset(user_perms))
```

**Output:**
```text
True
```

**Notes:**
- Order does not matter
- Equivalent operator: `<=`
- Commonly used to verify required permissions

---

## `issuperset()`

### Description
- Checks whether a set contains all elements of another set.

### Syntax
```python
set.issuperset(other)
```

**Return Value:**
- Returns `True` or `False`

**Example:**
```python
user_perms = {"read", "write", "delete"}
required = {"read", "write"}

print(user_perms.issuperset(required))
```

**Output:**
```text
True
```

**Notes:**
- Logical inverse of `issubset()`
- Equivalent operator: `>=`

---

## `isdisjoint()`

### Description
- Checks whether two sets have **no elements in common**.

### Syntax
```python
set.isdisjoint(other)
```

**Return Value:**
- Returns `True` or `False`

**Example:**
```python
admin_roles = {"admin", "root"}
guest_roles = {"guest", "anonymous"}

print(admin_roles.isdisjoint(guest_roles))
```

**Output:**
```text
True
```

**Notes:**
- Returns `True` when there is no overlap
- Useful for conflict detection
- Faster and clearer than manual intersection checks
- Returns immediately on first match

---

## Method vs Operator Summary

| Relationship  | Method         | Operator |
|---------------|:---------------|----------|
| Subset        | `issubset()`   | `<=`     |
| Superset      | `issuperset()` | `>=`     |

## Common Mistakes

**❌ Confusing subset direction**
```python
a.issubset(b)
```

Means:
```text
all elements of a are in b
```
Not the other way around.

**❌ Using intersection for boolean checks**
```python
a.intersection(b)
```
Use `isdisjoint()` or `issubset()` instead when you only need a boolean result.

---

## Summary

- Relation methods return **boolean values**
- They do **not modify** sets
- Use `issubset()` to validate requirements
- Use `issuperset()` to confirm ownership
- Use `isdisjoint()` to detect conflicts