# Context Keywords

## What is this?
Context keywords are used to manage resources and ensure proper setup and cleanup of operations.

---

## with
**Purpose:** Execute a block of code within a managed context.

```python
with open("example.txt", "w") as f:
    f.write("hello")
```

**Output:**

```text
(no output)
```

**Notes:**

- Ensures resources are properly released after use
- Commonly used with files and other managed resources

---
