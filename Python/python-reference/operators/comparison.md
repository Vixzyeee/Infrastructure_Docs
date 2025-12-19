# Comparison Operators

Comparison operators are used to **compare two values** and produce a boolean result.

They are fundamental to:
- conditionals
- loops
- filtering
- validation logic

This file focuses on **comparison semantics and behavior**, not control flow or data structures.

---

## Equality (`==`) and Inequality (`!=`)

### Description
Compare whether two values are **equal** or **not equal**.

### Syntax
```python
a == b
a != b
```

**Example:**
```python
print(5 == 5)
print(5 != 3)
print(5 == 5.0)
```

**Output:**
```text
True
True
True
```

**Notes:**
- `==` compares **values**, not object identity
- Different numeric types can be equal if their values match
- Equality behavior is defined by the operand types

---

## Less Than (`<`) and Greater Than (`>`)

### Description
Compare whether one value is strictly smaller or larger than another.

### Syntax
```python
a < b
a > b
```

**Example:**
```python
print(3 < 5)
print(10 > 2)
```

**Output:**
```text
True
True
```

**Notes:**
- Operands must be **comparable**
- Python 3 does not allow ordering comparisons between unrelated types

---

## Less Than or Equal (`<=`) and Greater Than or Equal (`>=`)

### Description
Compare whether a value is smaller/larger than or equal to another.

### Syntax
```python
a <= b
a >= b
```

**Example:**
```python
print(5 <= 5)
print(7 >= 3)
```

**Output:**
```text
True
True
```

**Notes:**
- Inclusive comparisons
- Commonly used for bounds checking

---

## Chained Comparisons

### Description
Python allows **multiple comparisons in a single expression**.

### Syntax
```python
a < b < c
```

**Example:**
```python
x = 5
print(0 < x < 10)
```

**Output:**
```text
True
```

**Notes:**
- Evaluated as:
    ```python
    (a < b) and (b < c)
    ```
- Each operand is evaluated only once
- This is not syntactic sugar; it has defined semantics

---

## Comparison Between Different Types

**Example:**
```python
print(1 < "2")
```

**Result:**
```text
TypeError
```

**Notes:**
- Python 3 forbids ordering comparisons between unrelated types
- This prevents silent logic errors
- Equality comparisons (`==`) may still be valid across types
- This behavior differs from Python 2 and is a deliberate design decision

---

## Boolean Result Guarantee

### Description
All comparison operators return a boolean value.

**Example:**
```python
result = (3 > 1)
print(type(result))
```

**Output:**
```text
<class 'bool'>
```

**Notes:**
- Comparison operators always return `bool`
- Safe for direct use in conditional expressions

---

## Comparison vs Identity

### Important Distinction
```python
a == b   # value comparison
a is b   # identity comparison
```

**Example:**
```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)
```

**Output:**
```text
True
False
```

**Notes:**
- `==` checks value equivalence
- `is` checks whether both variables reference the same object
- Identity comparisons are covered in `membership_identity.md`

---

## Summary
- Comparison operators evaluate relationships between values
- `==` checks value equality, not identity
- Ordering comparisons require compatible types
- Chained comparisons are evaluated efficiently and correctly
- All comparison operators return boolean values

This file defines **core comparison semantics** used throughout Python expressions.