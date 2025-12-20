# Iteration Built-in Functions

This file documents **iteration-related built-in functions** in Python.

These functions define and expose Python’s **iteration protocol**, which underpins:
- loops
- comprehensions
- generators
- async iteration

This file focuses on **protocol behavior**, not data structures.

---

## Scope

Covered in this file:
- `len`
- `iter`
- `next`
- `enumerate`
- `zip`
- `aiter`
- `anext`

Not covered:
- iteration syntax (`for`, `async for`)
- generator keywords (`yield`)
- iterator methods (`__iter__`, `__next__`)

---

## Iteration Model (Context)

Python iteration is based on two concepts:
- **iterable**: can produce an iterator
- **iterator**: produces values one at a time

These built-ins operate directly on that model.

---

## `len()`

### Definition
Returns the number of items in a container.

### Syntax
```python
len(obj)
```

**Behavior:**
- Delegates to `obj.__len__()`
- Returns a non-negative integer
- Raises `TypeError` if length is undefined

**Example:**
```python
print(len([1, 2, 3]))
print(len("python"))
```

**Output:**
```text
3
6
```

**Notes:**
- `len()` is constant-time for built-in containers
- Does not imply iterability
- Not available for infinite iterators
- Objects may be iterable without defining length

---

## `iter()`

### Definition
Returns an iterator from an iterable object.

### Syntax
```python
iter(obj)
iter(callable, sentinel)
```

**Behavior:**
- Calls `obj.__iter__()` if available
- Falls back to sequence protocol (`__getitem__`)
- Callable form produces values until sentinel is reached

**Example:**
```python
it = iter([1, 2, 3])
print(next(it))
```

**Output:**
```text
1
```

**Notes:**
- Core entry point into iteration
- The callable form is rarely used but powerful
- Does not consume values by itself

---

## `next()`

### Definition
Retrieves the next item from an iterator.

### Syntax
```python
next(iterator[, default])
```

**Behavior:**
- Advances the iterator
- Raises `StopIteration` when exhausted
- Returns `default` instead of raising if provided

**Example:**
```python
it = iter([1])
print(next(it))
print(next(it, "done"))
```

**Output:**
```text
1
done
```

**Notes:**
- `for` loops call this internally
- Manual usage implies manual exhaustion handling

---

## `enumerate()`

### Definition
Wraps an iterable and returns index-value pairs.

### Syntax
```python
enumerate(iterable, start=0)
```

**Behavior:**
- Produces tuples of `(index, value)`
- Index increments independently of the iterable

**Example:**
```python
for i, v in enumerate(["a", "b", "c"], start=1):
    print(i, v)
```

**Output:**
```text
1 a
2 b
3 c
```

**Notes:**
- Preferred over manual counters
- Produces an iterator, not a list

---

## `zip()`

### Definition
Aggregates elements from multiple iterables.

### Syntax
```python
zip(*iterables)
```

**Behavior:**
- Stops at the shortest iterable
- Returns tuples combining elements positionally

**Example:**
```python
print(list(zip([1, 2], ["a", "b", "c"])))
```

**Output:**
```text
[(1, 'a'), (2, 'b')]
```

**Notes:**
- Lazy and memory-efficient
- Does not pad by default
- Strict behavior available via `itertools`

---

## `aiter()`

### Definition
Returns an asynchronous iterator.

### Syntax
```python
aiter(obj)
```

**Behavior:**
- Calls `obj.__aiter__()`
- Used by `async for`

**Example:**
```python
ait = aiter(async_iterable)
```

**Output:**
```text
<async_iterator>
```

**Notes:**
- Only valid in async contexts
- Mirrors `iter()` for async protocols

---

## `anext()`

### Definition
Retrieves the next item from an async iterator.

### Syntax
```python
await anext(async_iterator[, default])
```

**Behavior:**
- Awaits the next value
- Raises `StopAsyncIteration` when exhausted

**Example:**
```python
value = await anext(async_iterator)
print(value)
```

**Output:**
```text
<next async value>
```

**Notes:**
- Async counterpart to `next()`
- Rarely called directly outside low-level async code

---

## Design Notes
- Iteration built-ins expose Python’s core data flow model
- They are protocol-driven, not type-specific
- Lazy evaluation is a deliberate design choice
- Async variants mirror synchronous semantics

---

## Summary
- Iteration is based on iterables and iterators
- `iter()` and `next()` define the core protocol
- Higher-level helpers (`enumerate`, `zip`) build on it
- Async iteration follows the same conceptual model

This file defines **Python’s iteration primitives**, not looping syntax.