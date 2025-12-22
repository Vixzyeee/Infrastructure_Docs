# random — Core RNG Mechanics

This document covers the **core mechanics** of Python’s `random` module.

It focuses on:
- the underlying random number generator (RNG)
- global generator state
- deterministic behavior
- fundamental number-generation APIs

Statistical theory and high-level use cases are intentionally excluded
and documented elsewhere.

---

## Overview

The `random` module implements a **pseudo-random number generator (PRNG)**.

Key characteristics:
- Deterministic
- State-based
- Not cryptographically secure
- Shared global generator by default

All top-level functions in `random` operate on a **single global RNG instance**
unless a custom `Random` object is created.

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

Each call advances the same internal RNG state.

---

## Underlying Generator
Python’s `random` module uses the **Mersenne Twister** algorithm.

Properties:
- Period: 2³¹⁹⁹³⁷ − 1
- Very fast
- Excellent statistical properties for simulation
- Predictable if internal state is known
- Given enough output values, the internal state can be reconstructed

This design is optimized for:
- simulations
- games
- randomized algorithms
- testing utilities

It is **not suitable** for cryptography or security-sensitive randomness.

---

## Global Generator Model

When you write:
```python
import random
random.random()
```

You are interacting with:
- a module-level global RNG
- shared across all calls in the process

Consequences:
- Calls affect each other
- Seeding affects all subsequent random values
- Call order matters

**Example: Shared State**
```python
import random

random.seed(10)
print(random.random())

print(random.random())
```

**Output:**
```text
0.5714025946899135
0.4288890546751146
```

The second call depends on the first.

---

## Seeding (`seed()`)
```python
random.seed(a=None)
```

Purpose:
- Initialize or reset the RNG state

Behavior:
- Same seed → same sequence
- Different seed → different sequence

**Example:**
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

Re-running this program produces the same output.

## Global State Side Effects
```python
import random

random.seed(1)
random.random()

random.seed(1)
print(random.random())
```

**Output:**
```text
0.13436424411240122
```

Re-seeding resets the global state.

---

## Generator State (`getstate()` / `setstate()`)
These functions expose the **entire internal state** of the RNG.

**Example:**
```python
import random

random.seed(7)
state = random.getstate()

print(random.random())
print(random.random())

random.setstate(state)
print(random.random())
```

**Output:**
```text
0.32383276483316237
0.15084917392450192
0.32383276483316237
```

This enables deterministic replay of random sequences.

**Warnings:**
- State format is implementation-specific
- Not guaranteed stable across Python versions
- Rarely required in application code
- Restored states should only be reused within the same Python runtime family

---

## Core Number Generation APIs

### `random()`
Returns a float in `[0.0, 1.0)`.

```python
import random

random.seed(0)
print(random.random())
```

**Output:**
```text
0.8444218515250481
```

---

### `randrange()`
Integer generation similar to `range()`.

```python
import random

random.seed(0)
print(random.randrange(10))
print(random.randrange(1, 10, 2))
```

**Output:**
```text
6
7
```

---

### `randint()`
Inclusive integer generation.

```python
import random

random.seed(0)
print(random.randint(1, 6))
```

**Output:**
```text
4
```

---

### `getrandbits()`
Low-level random bit generation.

```python
import random

random.seed(0)
print(random.getrandbits(8))
```

**Output:**
```text
216
```

---

## Determinism and Predictability
The `random` module is deterministic by design.

Given:
- the same Python version
- the same seed
- the same call order

The output sequence will be identical.

This behavior is a **feature**, not a flaw.

Security-sensitive code must use `secrets` or OS-provided randomness instead.

---

## Threading and Concurrency Notes
- The global RNG is **not isolated per thread**
- Calls from multiple threads interleave
- Results depend on execution order
- This makes tests flaky if the global RNG is shared across threads

### Recommended Pattern
```python
import random

rng = random.Random(42)
print(rng.random())
```

**Output:**
```text
0.6394267984578837
```

Using separate generator instances avoids shared state.

---

## Summary

Key takeaways:
- `random` uses a fast, deterministic PRNG
- All top-level functions share a global RNG
- Seeding controls reproducibility
- State can be saved and restored
- Predictability is intentional
- Not suitable for cryptographic use

Understanding these mechanics is essential before using higher-level APIs in this module.