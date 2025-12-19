# Assignment Operators

Assignment operators are used to **bind values to names** and update existing bindings.

They define how state is introduced and modified in a Python program.

This file focuses on **assignment semantics**, not variable scope, mutability in depth, or control flow.

---

## Simple Assignment (`=`)

### Description
Binds a value to a variable name.

### Syntax
```python
name = value
```

**Example:**
```python
x = 10
y = x
```

**Notes:**
- Assignment creates a **binding**, not a copy
- The right-hand side is evaluated before assignment
- Multiple names can reference the same object

---

## Multiple Assignment

### Description
Assigns multiple values in a single statement.

### Syntax
```python
a, b = value1, value2
```

**Example:**
```python
a, b = 1, 2
print(a, b)
```

**Output:**
```text
1 2
```

**Notes:**
- Commonly used for unpacking
- Right-hand side is evaluated first as a tuple-like structure
- Assignment fails if the number of values does not match the number of targets

---

## Augmented Assignment Operators

### Description
Combine an operation with assignment.

### Syntax
```python
a += b
a -= b
a *= b
a /= b
a //= b
a %= b
a **= b
```

**Example:**
```python
x = 10
x += 5
print(x)
```

**Output:**
```text
15
```

**Notes:**
- Often more concise than separate operation and assignment
- Behavior may differ from `a = a + b`, especially for mutable objects
- Augmented assignment can perform **in-place modification**

---

## Augmented Assignment and Mutability

**Example:**
```python
a = [1, 2]
b = a

a += [3]
print(a)
print(b)
```

**Output:**
```text
[1, 2, 3]
[1, 2, 3]
```

**Notes:**
- `+=` may mutate the object instead of rebinding the name
- This behavior depends on the operand type
- This is a common source of bugs

---

## Assignment vs Mutation

### Important Distinction
```python
a = [1, 2, 3]
b = a

a = a + [4]   # rebinding
```

```python
a = [1, 2, 3]
b = a

a += [4]     # mutation
```

**Notes:**
- Rebinding changes what the name points to
- Mutation changes the object itself
- Assignment operators can trigger either behavior

## Assignment Expressions (Walrus Operator `:=`)

### Description
Assigns a value to a variable **as part of an expression**.

### Syntax
```python
name := expression
```

**Example:**
```python
if (n := len(data)) > 10:
    print(n)
```

**Notes:**
- Introduced in Python 3.8
- Useful for avoiding repeated computation
- Should be used sparingly for readability

---

## Chained Assignment

### Description
Assigns the same value to multiple variables.

### Syntax
```python
a = b = c = value
```

**Example:**
```python
x = y = 0
```

**Notes:**
- All variables reference the same object
- Be careful when assigning mutable values, as all names will reference the same object

---

## Assignment Order of Evaluation

**Rule:**
1. Evaluate the right-hand side
2. Perform assignment left to right

**Example:**
```python
a, b = b, a
```

**Notes:**
- This works without a temporary variable
- The swap is safe and deterministic

---

## Summary
- Assignment binds names to values
- Augmented assignment may mutate objects
- Rebinding and mutation are not the same
- Assignment expressions allow inline binding
- Evaluation order is well-defined and predictable

This file defines **core assignment behavior** in Python expressions.