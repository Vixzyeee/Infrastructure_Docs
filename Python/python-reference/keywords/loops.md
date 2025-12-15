# Loop Keywords

## What is this?
Loop keywords are used to repeatedly execute a block of code based on a condition or sequence.

---

## for
**Purpose:** Iterate over a sequence and execute a block of code for each item.

```python
for i in [1, 2, 3]:
    print(i)
```

**Output:**

```text
1
2
3
```

**Notes:**

- Iterates over items in a sequence
- Commonly used with lists, tuples, ranges, and strings

---

## while

**Purpose:** Execute a block of code repeatedly while a condition is True.

```python
count = 0

while count < 3:
    print(count)
    count += 1
```

**Output:**

```text
0
1
2
```

**Notes:**

- Condition is evaluated before each iteration
- Can result in infinite loops if condition never becomes False

---

## break

**Purpose:** Exit the nearest enclosing loop immediately.

```python
for i in range(5):
    if i == 3:
        break
    print(i)
```

**Output:**

```text
0
1
2
```

**Notes:**

- Terminates only the nearest loop
- Commonly used inside conditional statements

---

## continue

**Purpose:** Skip the current iteration and continue with the next one.

```python
for i in range(5):
    if i == 3:
        continue
    print(i)
```

**Output:**

```text
0
1
2
4
```

**Notes:**

- Skips remaining code in the current iteration
- Loop continues normally afterward

---

## pass

**Purpose:** Act as a placeholder where a statement is syntactically required.

```python
for i in range(3):
    pass
```

**Output:**

```text
(no output)
```

**Notes:**

- Does nothing
- Useful for stubs and empty blocks

---
