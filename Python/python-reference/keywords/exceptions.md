# Exception Keywords

## What is this?
Exception keywords are used to handle runtime errors and
control the flow of execution when errors occur.

---

## try
**Purpose:** Wrap code that may raise an exception.

```python
try:
    x = int("10")
    print(x)
except ValueError:
    print("conversion failed")
```

**Output:**

```text
10
```

**Notes:**

- Code inside try is monitored for exceptions
- Must be followed by at least one except or finally

---

## except
**Purpose:** Catch and handle exceptions raised in a try block.

```python
try:
    x = int("abc")
except ValueError:
    print("conversion failed")
```

**Output:**

```text
conversion failed
```

**Notes:**

- Can catch specific exception types
- Multiple except blocks are allowed

---

## finally
**Purpose:** Execute code regardless of whether an exception occurs.

```python
try:
    x = int("10")
except ValueError:
    print("error")
finally:
    print("done")
```

**Output:**

```text
10
done
```

**Notes:**

- Always executed
- Commonly used for cleanup logic

---

## raise
**Purpose:** Explicitly raise an exception.

```python
raise ValueError("invalid value")
```

**Output:**

```text
ValueError: invalid value
```

**Notes:**

- Used to trigger exceptions manually
- Can raise built-in or custom exceptions

---

## assert
**Purpose:** Raise an exception if a condition is False.

```python
x = 5
assert x > 0
print("ok")
```

**Output:**

```text
ok
```

**Notes:**

- Used for debugging checks
- Raises `AssertionError` when condition is False

---
