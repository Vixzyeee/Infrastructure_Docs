# random — Reproducibility and Determinism

This document explains **reproducibility behavior** in Python’s `random` module.

It focuses on:
- deterministic execution
- seed control
- call-order sensitivity
- reproducible testing patterns
- common sources of non-deterministic bugs

This file does **not** cover:
- RNG internals (see `core.md`)
- sequence APIs (see `sequences.md`)
- statistical correctness of randomness

---

## Overview

The `random` module is **deterministic by design**.

Given:
- the same Python version
- the same seed
- the same call order
- the same input data

All four conditions must hold simultaneously.

The output sequence will be identical.

Reproducibility is a **feature**, not a side effect.

---

## Basic Determinism

### Example

```python
import random

random.seed(42)
print(random.random())
print(random.random())
```

**Output:**
```text
0.6394267984578837
0.025010755222666936
```

Running this code multiple times produces the same output.

---

## Seed as the Source of Truth
Seeding defines the **starting state** of the RNG.

Seeds do not guarantee stability if execution context changes.

**Example: Same Seed, Same Output**
```python
import random

random.seed(99)
print(random.randint(1, 10))
```

**Output:**
```text
7
```

Re-running the program yields the same value.

**Example: Different Seed, Different Output**
```python
import random

random.seed(100)
print(random.randint(1, 10))
```

**Output:**
```text
3
```

Changing the seed changes the entire sequence.

---

## Call Order Sensitivity
Reproducibility depends on **call order**, not just the seed.

**Example:**
```python
import random

random.seed(0)
print(random.random())
print(random.randint(1, 10))
```

**Output:**
```text
0.8444218515250481
7
```

Changing the order:
```python
import random

random.seed(0)
print(random.randint(1, 10))
print(random.random())
```

**Output:**
```text
7
0.7579544029403025
```

Same seed. Different results.

---

## Sequence Content Sensitivity
Randomness also depends on **input data**.

**Example:**
```python
import random

random.seed(0)
print(random.sample([1, 2, 3, 4], 2))
```

**Output:**
```text
[4, 2]
```

Changing the sequence:
```python
import random

random.seed(0)
print(random.sample([1, 2, 3, 4, 5], 2))
```

**Output:**
```text
[4, 5]
```

Same seed. Different input. Different result.

---

## Reproducibility in Tests

### Problem: Hidden Global State
```python
import random

def pick():
    return random.choice([1, 2, 3])

random.seed(0)
print(pick())
print(pick())
```

**Output:**
```text
2
2
```

This looks stable but is fragile.

Any additional random call elsewhere will change results.

---

## Recommended Pattern: Local RNG Instances

### Use isolated `Random` objects instead of the global RNG.

**Example:**
```python
import random

rng = random.Random(42)

print(rng.random())
print(rng.random())
```

**Output:**
```text
0.6394267984578837
0.025010755222666936
```

Benefits:
- No shared global state
- Safe for tests
- Predictable behavior

---

## Snapshotting RNG State
Advanced reproducibility can be achieved using state capture.

**Example:**
```python
import random

random.seed(5)
state = random.getstate()

print(random.random())
print(random.random())

random.setstate(state)
print(random.random())
```

**Output:**
```text
0.6229016948897019
0.7417869892607294
0.6229016948897019
```

**Warnings:**
- State objects are implementation-specific
- Not guaranteed stable across Python versions
- Use only within controlled environments

---

## Concurrency and Reproducibility
The global RNG is **shared across threads**.

Effects:
- Call interleaving
- Order-dependent output
- Non-deterministic behavior

**Example Pattern to Avoid:**
```python
import random
import threading

random.seed(0)

def worker():
    print(random.random())

t1 = threading.Thread(target=worker)
t2 = threading.Thread(target=worker)

t1.start()
t2.start()
```

Output order may vary between runs.

This makes global RNG usage unsafe in concurrent test environments.

---

## When Reproducibility Breaks

Reproducibility is lost when:
- seed is omitted or changed
- call order changes
- input data changes
- global RNG is shared across threads
- Python version changes

Determinism is **fragile by design**.

---

## What Reproducibility Is Not

Reproducibility does **not** mean:
- statistically unbiased randomness
- cryptographic safety
- identical output across Python implementations

Those concerns belong elsewhere.

---

## Summary

Key takeaways:
- `random` is deterministic and reproducible
- Seeds define the starting state
- Call order and input data matter
- Global RNG introduces hidden coupling
- Isolated RNG instances are preferred for tests
- Reproducibility is powerful but fragile

Understanding these constraints is essential for debugging, testing, and simulation accuracy.