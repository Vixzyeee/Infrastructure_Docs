# Logical Operators

Logical operators are used to **combine, negate, and control the evaluation of expressions**.

They are commonly used in:
- conditionals
- guards
- validation logic
- control flow expressions

This file focuses on **logical operator behavior**, not boolean theory or control structures.

---

## Logical AND (`and`)

### Description
Evaluates to the second operand if the first operand is truthy; otherwise returns the first operand.

### Syntax
```python
a and b
```

**Example:**
```python
print(True and True)
print(True and False)
print(0 and 10)
print(5 and 10)
```

**Output:**
```text
True
False
0
10
```

**Notes:**
- Uses short-circuit evaluation
- Returns one of the operands, not necessarily a boolean
- Commonly used for guard expressions

---

## Logical OR (`or`)

### Description
Evaluates to the first operand if it is truthy; otherwise returns the second operand.

### Syntax
```python
a or b
```

**Example:**
```python
print(False or True)
print(0 or 10)
print("" or "fallback")
```

**Output:**
```text
True
10
fallback
```

**Notes:**
- Uses short-circuit evaluation
- Returns one of the operands
- Often used for default values
- Can be problematic when falsy values (e.g. 0, "") are valid inputs

---

## Logical NOT (`not`)

### Description
Negates the truth value of an expression.

### Syntax
```python
not expression
```
**Example:**
```python
print(not True)
print(not 0)
print(not "")
```

**Output:**
```text
False
True
True
```

**Notes:**
- Always returns a boolean value
- Has higher precedence than `and` and `or`

---

## Short-Circuit Evaluation

### Description
Logical operators stop evaluating as soon as the result is determined.

**Example:**
```python
def check():
    print("called")
    return True

print(False and check())
print(True or check())
```

**Output:**
```text
False
True
```

**Notes:**
- `check()` is never called
- This behavior is intentional
- Frequently used to avoid errors or unnecessary computation

---

## Logical Operators and Truthiness

### Description
Logical operators rely on **truthiness**, not strict boolean values.

**Example:**
```python
print([] and "yes")
print([1] and "yes")
print(None or "default")
```

**Output:**
```text
[]
yes
default
```

**Notes:**
- Any object can be used in logical expressions
- Truthiness rules are defined by the object, not the operator
- Empty collections and `None` are falsy

## Common Pattern: Guard Expressions

**Example:**
```python
user = None
print(user and user.name)
```

**Notes:**
- Prevents attribute access errors
- Relies on short-circuit behavior
- Can reduce the need for explicit conditionals
- Prefer explicit checks when readability matters more than conciseness

---

## Logical Operators vs Bitwise Operators

### Important Distinction
```python
a and b    # logical
a & b      # bitwise
```

**Notes:**
- Logical operators work on truthiness
- Bitwise operators work on bits
- Confusing the two leads to bugs and regret

---

## Operator Precedence

### Order (High → Low)
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

**Notes:**
- Parentheses improve readability
- Do not rely on precedence for complex expressions

---

## Summary
- Logical operators control expression evaluation
- `and` / `or` return operands, not booleans
- `not` always returns a boolean
- Short-circuit evaluation is intentional and useful
- Truthiness drives logical behavior, not type

This file defines **core logical operator semantics** in Python expressions.