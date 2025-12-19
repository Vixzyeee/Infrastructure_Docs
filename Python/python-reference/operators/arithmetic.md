# Arithmetic Operators

Arithmetic operators are used to perform **numeric computations** in Python.

They work primarily with numeric types such as:
- `int`
- `float`
- `complex`

These operators form the foundation of expressions and are evaluated **before** most higher-level constructs.

This file focuses on **operator behavior**, not numeric types or math libraries.

---

## Addition (`+`)

### Description
Adds two operands.

### Syntax
```python
a + b
```

**Example:**
```python
print(2 + 3)
print(1.5 + 2.5)
```

**Output:**
```text
5
4.0
```

**Notes:**
- Works with integers, floats, and complex numbers
- Some types overload this operator (e.g. string concatenation); the behavior is defined by the operand types, not the operator itself

---

## Subtraction (`-`)

### Description
Subtracts the right operand from the left operand.

### Syntax
```python
a - b
```

**Example:**
```python
print(10 - 4)
print(5.5 - 2)
```

**Output:**
```text
6
3.5
```

**Notes:**
- Straightforward arithmetic subtraction

---

## Multiplication (`*`)

### Description
Multiplies two operands.

### Syntax
```python
a * b
```

**Example:**
```python
print(3 * 4)
print(2.5 * 2)
```

**Output:**

```text
12
5.0
```

**Notes:**
- Repeated sequence behavior (e.g. `"a" * 3`) is type-specific and not part of arithmetic itself

---

## True Division (`/`)

### Description
Divides the left operand by the right operand and always returns a float.

### Syntax
```python
a / b
```

**Example:**
```python
print(5 / 2)
print(4 / 2)
```

**Output:**
```text
2.5
2.0
```

**Notes:**
- Always returns `float`, even when the division is exact
- Raises `ZeroDivisionError` if the divisor is zero

---

## Floor Division (`//`)

### Description
Performs division and returns the **floored result**.

### Syntax
```python
a // b
```

**Example:**
```python
print(5 // 2)
print(-5 // 2)
```

**Output:**
```text
2
-3
```

**Notes:**
- Result is rounded **toward negative infinity**
- This behavior surprises many people
- The result type depends on operand types (`int` vs `float`)
- This is intentional and mathematically correct under floor division rules

---

## Modulo (`%`)

### Description
Returns the remainder of a division.

### Syntax
```python
a % b
```

**Example:**
```python
print(5 % 2)
print(-5 % 2)
```

**Output:**
```text
1
1
```

**Notes:**
- The result follows the sign of the **divisor**
- Closely related to floor division:
    ```python
    a == (a // b) * b + (a % b)
    ```
- This identity always holds in Python

---

## Exponentiation (`**`)

### Description
Raises the left operand to the power of the right operand.

### Syntax
```python
a ** b
```

**Example:**
```python
print(2 ** 3)
print(9 ** 0.5)
```

**Output:**
```text
8
3.0
```

**Notes:**
- Higher precedence than multiplication
- Right-associative:
    ```python
    2 ** 3 ** 2  # evaluated as 2 ** (3 ** 2)
    ```

---

## Unary Plus (`+x`) and Unary Minus (`-x`)

### Description
Unary operators that indicate numeric sign.

### Syntax
```python
+x
-x
```

**Example:**
```python
x = 5
print(+x)
print(-x)
```

**Output:**
```text
5
-5
```

**Notes:**
- Unary plus does not change the value
- Unary minus returns the negated value
- Often used implicitly in expressions

---

## Zero Division Behavior

**Example:**
```python
print(10 / 0)
```

**Result:**
```text
ZeroDivisionError
```

**Notes:**
- Division by zero is a runtime error
- Applies to `/`, `//`, and `%`

---

## Summary
- Arithmetic operators operate on numeric values
- `/` always returns a float
- `//` performs floor division toward negative infinity
- `%` follows the sign of the divisor
- Operator behavior is independent of type-specific implementations

This file defines **core arithmetic behavior** used throughout Python expressions.