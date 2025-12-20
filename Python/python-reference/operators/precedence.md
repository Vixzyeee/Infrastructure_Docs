# Operator Precedence

Operator precedence defines the **order in which operators are evaluated** in an expression.

When multiple operators appear in a single expression, precedence determines:
- which operation runs first
- how the expression is grouped
- what the final result is

Misunderstanding precedence leads to subtle logic bugs that are hard to spot.

This file focuses on **practical precedence rules**, not exhaustive grammar tables.

---

## Why Precedence Matters

**Example:**
```python
print(2 + 3 * 4)
```

**Output:**
```text
14
```

### Explanation
```text
3 * 4  -> 12
2 + 12 -> 14
```

**Notes:**
- Multiplication has higher precedence than addition
- The expression is not evaluated left to right

---

## Common Precedence Order (High → Low)
This list covers the **most commonly used operators**.

1. Parentheses `()`
2. Unary operators `+x`, `-x`, `not`
3. Exponentiation `**`
4. Multiplication, division, floor division, modulo `* / // %`
5. Addition, subtraction `+ -`
6. Comparisons `< <= > >= == !=`
7. Membership and identity `in`, `not in`, `is`, `is not`
8. Logical `and`
9. Logical `or`
10. Assignment `=`, `+=`, `:=`, etc.

**Notes:**
- Comparison, membership, and identity operators share the same precedence level and are evaluated left to right

---

## Parentheses Override Everything

**Example:**
```python
print((2 + 3) * 4)
```

**Output:**
```text
20
```

**Notes:**
- Parentheses explicitly control evaluation order
- Prefer parentheses when readability matters

---

## Exponentiation Is Right-Associative

**Example:**
```python
print(2 ** 3 ** 2)
```

**Output:**
```text
512
```

### Explanation
```text
2 ** (3 ** 2)
2 ** 9 -> 512
```

**Notes:**
- Exponentiation does not evaluate left to right
- This surprises many people

---

## Unary Operators vs Exponentiation

**Example:**
```python
print(-2 ** 2)
print((-2) ** 2)
```

**Output:**
```text
-4
4
```

### Explanation
```text
-2 ** 2   -> -(2 ** 2)
(-2) ** 2 -> 4
```

**Notes:**
- Unary operators have lower precedence than `**`
- Parentheses remove ambiguity

---

## Comparison Chaining and Precedence

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
- Chained comparisons are evaluated left to right
- Each comparison is evaluated once
- This is a special rule, not a generic precedence shortcut

---

## Logical Operator Precedence

### Order
1. `not`
2. `and`
3. `or`

**Example:**
```python
print(not False and False)
```

**Output:**
```text
False
```

### Explanation
```text
(not False) and False
True and False -> False
```

---

## Assignment and Precedence

**Example:**
```python
a = 1 + 2 * 3
```

**Notes:**
- Assignment has very low precedence
- The right-hand side is fully evaluated first
- This rule makes assignment predictable
- Assignment expressions (`:=`) have lower precedence than most operators and often require parentheses

---

## Readability Rule (The Only One That Matters)

### Guideline
If you have to think about precedence, **use parentheses**.

**Example:**
```python
result = (a and b) or (c and d)
```

**Notes:**
- Explicit grouping beats clever expressions
- Readability is more important than brevity

---

## Summary
- Operator precedence defines evaluation order
- Not all operators evaluate left to right
- Exponentiation and unary operators have special rules
- Parentheses override precedence and improve clarity
- When in doubt, be explicit

This file defines **practical operator precedence rules** used throughout Python expressions.