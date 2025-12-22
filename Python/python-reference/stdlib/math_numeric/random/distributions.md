# random — Statistical Distributions

This document covers **statistical distribution APIs** provided by Python’s `random` module.

It focuses on:
- supported probability distributions
- parameter behavior
- common usage patterns
- conceptual differences between distributions

This file does **not** cover:
- RNG internals (see `core.md`)
- sequence operations (see `sequences.md`)
- reproducibility mechanics (see `reproducibility.md`)
- statistical theory or proofs

---

## Overview

The `random` module provides several functions for generating values
according to **specific probability distributions**.

These functions are primarily used for:
- simulations
- probabilistic modeling
- randomized testing
- synthetic data generation

All distributions:
- rely on the same underlying PRNG
- are deterministic given the same seed and call order
- are **not suitable for cryptographic use**

---

## Uniform Distribution

### `uniform(a, b)`

Generates a floating-point number uniformly distributed
in the range `[a, b]`.

```python
import random

random.seed(0)
print(random.uniform(1.0, 5.0))
```

**Output:**
```text
4.3776874061001925
```

Each value in the interval has equal probability.

The distribution is continuous, not discrete.

---

## Triangular Distribution

### `triangular(low, high, mode)`

Generates values with a **peak probability at `mode`**.
```python
import random

random.seed(0)
print(random.triangular(0, 10, 5))
```

**Output:**
```text
7.148397144271142
```

Useful when:
- minimum, maximum, and most-likely values are known
- exact statistical modeling is not required
- This distribution is often used as a heuristic when data is scarce

---

## Normal (Gaussian) Distributions

### `normalvariate(mu, sigma)`

Generates values following a **normal distribution**.
```python
import random

random.seed(0)
print(random.normalvariate(0, 1))
```

**Output:**
```text
0.9417154046806644
```

### `gauss(mu, sigma)`

Similar to `normalvariate`, but slightly faster.
```python
import random

random.seed(0)
print(random.gauss(0, 1))
```

**Output:**
```text
0.9417154046806644
```

**Notes:**
- Both produce bell-shaped distributions
- `gauss()` may reuse internal state for efficiency
- Outputs are unbounded

---

## Exponential Distribution

### `expovariate(lambd)`

Generates values according to an **exponential distribution**.
```python
import random

random.seed(0)
print(random.expovariate(1.0))
```

**Output:**
```text
1.8606071110652234
```

Commonly used for:
- modeling time between events
- queue simulations

---

## Gamma and Related Distributions

### `gammavariate(alpha, beta)`

```python
import random

random.seed(0)
print(random.gammavariate(2.0, 1.0))
```

**Output:**
```text
2.050589258386151
```

Other related distributions:
- `betavariate(alpha, beta)`
- `lognormvariate(mu, sigma)`
- `paretovariate(alpha)`
- `weibullvariate(alpha, beta)`
- `vonmisesvariate(mu, kappa)`

These are specialized and typically used in statistical or domain-specific simulations.

---

## Integer Distribution

### `randint(a, b)`

Produces a **discrete uniform distribution** over integers.
```python
import random

random.seed(0)
print(random.randint(1, 6))
```

**Output:**
```text
4
```

Although simple, this is still a distribution and should be treated as such in simulations.

---

## Common Pitfalls

### Assuming Statistical Correctness

The distributions:
- are suitable for simulations
- are **not** validated for scientific rigor
- should not replace dedicated statistical libraries
- using the wrong distribution is a modeling error, not a randomness issue

For serious statistical work, consider specialized tools.

---

## Confusing Distribution Shape

Using the wrong distribution can lead to:
- unrealistic simulations
- misleading test data
- incorrect assumptions

Always choose a distribution that matches the underlying process being modeled.

---

## Determinism Reminder

All distribution functions are:
- deterministic given the same seed
- sensitive to call order
- dependent on input parameters

```python
import random

random.seed(42)
print(random.normalvariate(0, 1))
```

**Output:**
```text
0.4967141530112327
```

Changing any of the above conditions changes the result.

---

## Summary

Key takeaways:
- `random` provides multiple distribution generators
- All distributions rely on the same PRNG
- Outputs follow defined probability shapes
- Results are deterministic but context-sensitive
- Not suitable for cryptographic or scientific-grade statistics

These APIs are best used for simulations, testing, and controlled randomness scenarios.