# Conditional and Decision Making Keywords

## What is this?
Conditional keywords are used to make decisions in Python.

They control which block of code is executed based on conditions.

---

## if
**Purpose:** Execute a block of code when a condition evaluates to True.

```python
x = 10

if x > 5:
    print("greater than five")
```
**Output:**

```text
greater than five
```

**Notes:**

- Condition must evaluate to a boolean value
- Code block runs only when condition is True

---

## elif
**Purpose:** Check additional conditions when previous if or elif conditions are False.

```python
x = 10

if x < 5:
    print("small")
elif x < 15:
    print("medium")
```
**Output:**

```text
medium
```

**Notes:**

- Can appear multiple times
- Evaluated top-down
- First matching condition stops further checks

---

## else
**Purpose:** Execute a block of code when all previous conditions are False.

```python
x = 10

if x < 5:
    print("small")
elif x < 8:
    print("medium")
else:
    print("large")
```
**Output:**

```text
large
```

**Notes:**

- Optional
- Must be the last block in a conditional chain

---
