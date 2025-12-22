# `random` — Pseudo-Random Number Generation

This directory documents Python’s built-in `random` module as a **technical reference**.

It explains how pseudo-randomness works in Python, how the APIs are structured,
and how to use them correctly without introducing subtle bugs or security issues.

This is **not** a tutorial and **not** a beginner guide.

---

## What This Directory Covers

This documentation focuses on:

- how Python generates pseudo-random values
- the deterministic nature of the `random` module
- sequence-based randomness
- statistical distribution helpers
- reproducibility and testing implications
- correct usage vs dangerous misuse

All content assumes basic familiarity with Python.

---

## What This Directory Does *Not* Cover

This directory intentionally avoids:

- teaching probability or statistics
- cryptographic randomness
- step-by-step beginner tutorials
- performance benchmarking
- replacing official Python documentation

Those topics either belong elsewhere or require specialized libraries.

---

## File Structure

```text
random/
├── README.md           # This file
├── core.md             # RNG mechanics and global state
├── sequences.md        # Random operations on sequences
├── reproducibility.md  # Determinism, testing, and debugging
├── distributions.md   # Statistical distribution helpers
└── comparisons.md     # Proper usage and security decisions
```

Each file focuses on **one conceptual layer** of the module.

---

## How to Read This Documentation

Recommended order:
1. **`core.md`**  
   Understand how the RNG works and why `random` is deterministic.
2. **`sequences.md`**  
   Learn how randomness is applied to lists, ranges, and other sequences.
3. **`reproducibility.md`**  
   Internalize how seeds, call order, and global state affect results.
4. **`distributions.md`**  
   Explore available probability distributions and when to use them.
5. **`comparisons.md`**  
   Learn when not to use `random`, especially in security contexts.

Skipping `core.md` often leads to misuse later.

---

## Design Philosophy

The `random` module is designed to be:
- fast
- deterministic
- reproducible
- suitable for simulations and testing

It is **not** designed to be secure.

Predictability is a feature, not a flaw.

---

## Common Mistake This Documentation Tries to Prevent
Using `random` where unpredictability is required.

If you need:
- tokens
- passwords
- session identifiers
- security-sensitive values

`random` is the wrong tool.

That decision is explained in `comparisons.md`.

---

## Scope and Longevity

This reference is written to be:
- stable across Python versions
- useful months or years later
- readable without external context

It prioritizes **conceptual correctness** over exhaustive API listings.

---

## Summary

This directory exists to answer one question:
“How do I use Python’s `random` module correctly without lying to myself?”

Misunderstanding `random` is a common source of subtle bugs.

If you understand everything here, you understand `random` well enough to use it safely and intentionally.

Anything beyond this belongs to statistics, cryptography, or specialized simulation tooling.