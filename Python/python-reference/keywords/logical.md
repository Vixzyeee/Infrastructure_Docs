# Logical and Membership Keywords

## What is this?
Logical and membership keywords are used to combine conditions, negate expressions, and test identity or membership.

---

## and
**Purpose:** Return True if both conditions are True.

```python
x = 5
print(x > 0 and x < 10)
```

**Output:**

```text
True
```

**Notes:**

- Both conditions must evaluate to True
- Evaluation stops when a False condition is found

---

## or
**Purpose:** Return True if at least one condition is True.

```python
x = 5
print(x < 0 or x < 10)
```

**Output:**

```text
True
```

**Notes:**

- Returns True if any condition is True
- Evaluation stops when a True condition is found

---

## not
**Purpose:** Negate a boolean expression.

```python
x = 5
print(not x > 10)
```

**Output:**

```text
True
```

**Notes:**

- Inverts the boolean result
- Has higher precedence than `and` and `or`

---

## is
**Purpose:** Test whether two variables refer to the same object.

```python
a = [1, 2, 3]
b = a
print(a is b)
```

**Output:**

```text
True
```

**Notes:**

- Checks object identity, not value equality
- Commonly used to compare with `None`

---

## in
**Purpose:** Test whether a value exists within a collection.

```python
items = [1, 2, 3]
print(2 in items)
```

**Output:**

```text
True
```

**Notes:**

- Works with sequences and collections
- Returns True if the value is found

---
