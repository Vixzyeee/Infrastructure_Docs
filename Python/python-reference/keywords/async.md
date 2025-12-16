# Async Keywords

## What is this?
Async keywords are used to define and control asynchronous execution in Python.

---

## async
**Purpose:** Define an asynchronous function.

```python
async def greet():
    return "hello"
```

**Output:**

```text
(no output)
```

**Notes:**

- Used to declare an asynchronous function
- Must be used with `await` when called

---

## await
**Purpose:** Pause execution until an asynchronous operation completes.

```python
import asyncio

async def greet():
    return "hello"

async def main():
    result = await greet()
    print(result)

asyncio.run(main())
```

**Output:**

```text
hello
```

**Notes:**

- Can only be used inside an async function
- Suspends execution until the awaited task finishes

---
