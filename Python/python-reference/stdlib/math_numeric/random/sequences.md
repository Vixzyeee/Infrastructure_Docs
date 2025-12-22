# random — Sequence Operations

This document covers **sequence-related APIs** provided by Python’s `random` module.

It focuses on:
- random selection from sequences
- sampling behavior
- in-place shuffling
- population-based randomness

This file does **not** cover:
- RNG internals (see `core.md`)
- statistical distributions (see `distributions.md`)
- testing strategy (see `reproducibility.md`)

---

## Overview

Sequence operations in `random` work on **finite iterables**, typically:
- lists
- tuples
- ranges
- other sequence types

All operations draw randomness from the **same RNG source** described in `core.md`.

These functions are commonly used for:
- randomized algorithms
- sampling
- simulations
- simple games
- test data generation

---

## `choice()`

Selects **one random element** from a non-empty sequence.

```python
import random

random.seed(0)
data = ["a", "b", "c", "d"]

print(random.choice(data))
```

**Output:**
```text
d
```

**Notes:**
- Sequence must be non-empty
- Raises `IndexError` if empty
- Selection is uniform
- For large populations, repeated `choice()` calls may bias performance expectations

---

## `choices()`

Selects **one or more elements with replacement**.

```python
import random

random.seed(0)
data = ["a", "b", "c"]

print(random.choices(data, k=5))
```

**Output:**
```text
['c', 'c', 'b', 'a', 'b']
```

**Characteristics:**
- Sampling **with replacement**
- Elements may repeat
- Supports weighting

### Weighted Example

```python
import random

random.seed(0)
data = ["low", "medium", "high"]
weights = [1, 2, 5]

print(random.choices(data, weights=weights, k=5))
```

**Output:**
```text
['high', 'high', 'medium', 'low', 'high']
```

---

## `sample()`

Selects **unique elements without replacement**.

```python
import random

random.seed(0)
data = [1, 2, 3, 4, 5]

print(random.sample(data, k=3))
```

**Output:**
```text
[4, 5, 1]
```

**Notes:**
- Sampling **without replacement**
- `k` must be ≤ length of sequence
- Original sequence is not modified

This function is ideal for:
- drawing hands
- selecting subsets
- randomized but unique selections

---

## `shuffle()`

Randomly reorders a **mutable sequence in place**.

```python
import random

random.seed(0)
data = [1, 2, 3, 4, 5]

random.shuffle(data)
print(data)
```

**Output:**
```text
[3, 2, 1, 5, 4]
```

**Important Characteristics:**
- Operates **in place**
- Returns `None`
- Only works on mutable sequences

This is a **destructive operation**.

---

## Common Pitfalls

### Expecting `shuffle()` to return a value
```python
result = random.shuffle([1, 2, 3])
print(result)
```

**Output:**
```text
None
```

The sequence is shuffled in place.  
Do not assign its return value.

---

## Confusing `choices()` and `sample()`

| Function       | Replacement | Duplicates Possible |
|----------------|:------------|---------------------|
| `choice()`     | Yes         | N/A (single item)   |
| `choices()`    | Yes         | Yes                 |
| `sample()`     | No          | No                  |

Using the wrong function can introduce subtle bugs.

---

## Determinism with Sequences

All sequence operations are deterministic given:
- the same seed
- the same input sequence
- the same call order

Any change in sequence contents or call order will change the result.

**Example:**
```python
import random

random.seed(42)
print(random.sample(range(10), 3))
```

**Output:**
```text
[1, 0, 4]
```

Re-running this code produces identical results.

---

## Performance Notes
- `choice()` is O(1)
- `sample()` complexity grows with `k` and population size
- `shuffle()` is O(n)

For very large populations, be mindful of memory and runtime behavior.

---

## Summary

Key takeaways:
- Sequence APIs provide high-level randomness over iterables
- `choice()` selects one element
- `choices()` samples with replacement
- `sample()` samples without replacement
- `shuffle()` mutates sequences in place
- All operations depend on the same RNG source

These functions are convenient but must be chosen carefully to match the intended sampling semantics.

