# Membership and Identity Operators

Membership and identity operators are used to test **containment** and **object identity**.

They answer two very different questions:
- “Is this value contained here?”
- “Is this the exact same object?”

Confusing these concepts leads to subtle and persistent bugs.

This file focuses on **operator semantics**, not data structures or object lifetimes.

---

## Membership Operator: `in`

### Description
Checks whether a value exists within a container.

### Syntax
```python
value in container
```

**Example:**
```python
print(2 in [1, 2, 3])
print("a" in "cat")
print("key" in {"key": 1})
```

**Output:**
```text
True
True
True
```

**Notes:**
- Works with sequences, sets, dictionaries, and strings
- For dictionaries, membership checks **keys**, not values
- Behavior depends on the container type

---

## Membership Operator: `not in`

### Description
Checks whether a value does **not** exist within a container.

### Syntax
```python
value not in container
```

**Example:**
```python
print(4 not in [1, 2, 3])
print("z" not in "cat")
```

**Output:**
```text
True
True
```

**Notes:**
- Logical negation of `in`
- Often clearer than using `not (value in container)`

---

## Identity Operator: `is`

### Description
Checks whether two variables reference the **same object in memory**.

### Syntax
```python
a is b
```

**Example:**
```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)
print(a is c)
```

**Output:**
```text
True
False
```

**Notes:**
- Compares object identity, not value equality
- Equivalent to comparing object IDs
- Almost never what you want for value comparison

---

## Identity Operator: `is not`

### Description
Checks whether two variables do **not** reference the same object.

### Syntax
```python
a is not b
```

**Example:**
```python
x = []
y = []

print(x is not y)
```

**Output:**
```text
True
```

**Notes:**
- Logical negation of `is`
- Same identity rules apply

---

## Identity vs Equality

### Critical Distinction
```python
a == b    # value equality
a is b    # object identity
```

**Example:**
```python
x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)
print(x is y)
```

**Output:**
```text
True
False
```

**Notes:**
- `==` compares values using type-defined logic
- `is` compares object identity only
- Using `is` for value comparison is a bug

---

## Correct Use of `is`

### Description
Use identity comparison when checking against singleton objects.

### Recommended Pattern
```python
value = None

print(value is None)
print(value == None)
```

**Output:**
```text
True
True
```

**Notes:**
- `None` is a singleton object
- Identity comparison (`is None`) is the intended and idiomatic usage
- `== None` may work but relies on equality semantics, not identity
- Always prefer `is None` for clarity and correctness

---

## Common Mistake: Using `is` for Literals

**Example:**
```python
print(256 is 256)
print(257 is 257)
```

**Result:**
```text
True
False
```

**Notes:**
- This behavior is an implementation detail
- Integer caching is not guaranteed across values or implementations
- Never rely on this behavior
- Results may differ across Python versions and implementations

---

## Membership vs Identity

**Example:**
```python
items = [1, 2, 3]

print(2 in items)
print(2 is items)
```

**Output:**
```text
True
False
```

**Notes:**
- `in` checks containment
- `is` checks identity
- They answer completely different questions

---

## Summary
- `in` / `not in` test membership
- `is` / `is not` test object identity
- Identity is not equality
- `is` should primarily be used with `None`
- Misusing identity operators leads to subtle bugs
- Membership and identity operators answer fundamentally different questions

This file defines **core membership and identity semantics** in Python expressions.