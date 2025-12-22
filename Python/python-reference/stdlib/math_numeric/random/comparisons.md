# random — Comparisons and Proper Usage

This document explains **when to use `random` and when not to use it**.

It focuses on:
- comparing `random` with other randomness sources
- security implications
- correct tool selection based on intent
- common misuse patterns

This file does **not** cover:
- RNG internals (see `core.md`)
- sequence APIs (see `sequences.md`)
- reproducibility mechanics (see `reproducibility.md`)
- statistical distribution details (see `distributions.md`)

---

## Overview

Python provides **multiple sources of randomness**.

They exist for **different purposes**, not as interchangeable tools.

Using the wrong randomness source is not a minor mistake.
It can lead to:
- security vulnerabilities
- predictable tokens
- broken authentication
- incorrect assumptions about safety

---

## `random` Module

The `random` module provides:
- fast pseudo-random number generation
- deterministic behavior
- reproducible sequences

### Intended Use Cases
- simulations
- games
- randomized algorithms
- testing
- synthetic data generation

### Properties
- Deterministic
- State-based
- Predictable if state is known
- Not cryptographically secure

---

## `secrets` Module

The `secrets` module provides **cryptographically secure randomness**.

It is designed for:
- passwords
- tokens
- session identifiers
- API keys
- security-sensitive values

### Properties
- Non-deterministic
- OS-backed entropy
- Resistant to prediction
- Slower than `random`

**Example:**
```python
import secrets

print(secrets.token_hex(16))
```

**Output:**
```text
9f1c0a8e4c1b9d0a6f7e2c4a1b8d3f6e
```

Each call produces an unpredictable value.

---

## Key Differences

| Aspect        | `random`             | `secrets`                 |
|---------------|:---------------------|---------------------------|
| Deterministic | Yes                  | No                        |
| Reproducible  | Yes                  | No                        |
| Secure        | No                   | Yes                       |
| Performance   | Fast                 | Slower                    |
| Use Case      | Simulation / Testing | Security / Authentication |

These differences are **intentional**, not limitations.

---

## Common Misuse Patterns

### ❌ Using `random` for Security
```python
import random

token = str(random.random())
```

This token:
- is predictable
- can be guessed
- is not safe for authentication

This is a **security bug**, not a style issue.

---

### ✅ Correct Security Usage
```python
import secrets

token = secrets.token_urlsafe(32)
print(token)
```

**Output:**
```text
Dk9VZ5WlKcP1e2T4R8QJHkL3M0XyZaBcDeFg
```

This token is suitable for security-sensitive contexts.

---

## Reproducibility vs Security

Reproducibility and security are **mutually exclusive goals**.
- Reproducibility requires determinism
- Security requires unpredictability

Trying to achieve both simultaneously results in broken systems.

---

## Performance Considerations
- `random` is optimized for speed
- `secrets` prioritizes entropy quality

Using `secrets` in tight loops or simulations is unnecessary and inefficient.

Using `random` for secrets is dangerous.

---

## Decision Checklist

Ask yourself:
- Do I need reproducible results? → use `random`
- Do I need unpredictability? → use `secrets`
- Am I generating tokens or credentials? → use `secrets`
- Am I simulating or testing? → use `random`

If security is involved, **do not use `random`**.

---

## What This Comparison Is Not

This comparison does **not** imply:
- `secrets` is a better `random`
- `random` is obsolete
- one module should replace the other

They solve **different problems**.

---

## Summary

Key takeaways:
- `random` is fast, deterministic, and reproducible
- `secrets` is secure and unpredictable
- Choosing the wrong module is a design error
- Reproducibility and security serve different goals
- Correct tool selection prevents serious bugs

Understanding these distinctions is essential for writing safe and correct Python code.