# Conditional and Decision Making Keywords

## What is this?
Conditional keywords are used to make decisions in Python.<br>
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
**Use cases:**

- Basic decision making
- Input validation
- Feature toggles

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
**Use cases:**

- Handling multiple decision branches
- Replacing nested if statements

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
**Use cases:**

- Default or fallback behavior
- Handling unexpected or remaining cases

**Notes:**

- Optional
- Must be the last block in a conditional chain

---

## Nested Conditionals
**Purpose:** Use conditionals inside other conditionals for more complex logic.

```python
x = 10

if x > 0:
    if x % 2 == 0:
        print("positive even number")
```
**Output:**

```text
positive even number
```
**Use cases:**

- Multi-level decision logic
- Complex validation rules

**Notes:**

- Avoid deep nesting when possible
- Prefer elif for readability

---

## Conditional Expressions (Ternary)
**Purpose:** Write simple conditional logic in a single line.

```python
x = 10
result = "big" if x > 5 else "small"
print(result)
```
**Output:**

```text
big
```
**Use cases:**

- Simple value assignment based on condition
- Cleaner alternative to short if-else blocks

**Notes:**

- Use only for simple conditions
- Avoid chaining for readability

---

## Boolean Evaluation in Conditionals
**Purpose:** Understand how values are evaluated as True or False.

```python
if []:
    print("not empty")
else:
    print("empty")
```
**Output:**

```text
empty
```
**Use cases:**

- Checking empty lists, strings, or collections
- Simplifying conditional expressions

**Notes:**

- Empty values evaluate to False
- Non-empty values evaluate to True

---
