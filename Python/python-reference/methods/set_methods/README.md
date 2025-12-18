# Set Methods (`set`)

This directory documents commonly used **Python `set` methods**.

The focus is on:
- Core behavior of sets
- Method intent and side effects
- Return values
- Common pitfalls and correct usage patterns

This is a **reference**, not a tutorial.

---

## What Is a Set?

A `set` is a collection that is:
- Unordered
- Mutable
- Contains unique elements only
- Stores hashable objects

Sets are best suited for:
- Fast membership testing
- Deduplication
- Set algebra (union, intersection, difference)
- Logical comparisons between collections

---

## Directory Structure

| File                 | Description                                        |
|----------------------|----------------------------------------------------|
| `creation_basics.md` | Creating sets and understanding core behavior      |
| `add_modify.md`      | Adding elements to a set                           |
| `remove.md`          | Removing elements and handling missing values      |
| `algebra.md`         | Set algebra operations (union, intersection, etc.) |
| `relations.md`       | Comparing relationships between sets               |
| `copy.md`            | Copying sets safely                                |

Each file can be read independently.

---

## Usage Principles

- Prefer **sets** when uniqueness and fast lookup matter more than order
- Do not rely on element order in a set
- Understand whether a method:
  - modifies the set in place, or
  - returns a new set
- Use algebra and relation methods instead of manual loops

---

## Common Pitfalls

- Using `{}` to create an empty set (this creates a dictionary)
- Expecting set methods to preserve order
- Using `remove()` when element absence is normal
- Assuming assignment creates a copy

These issues are explicitly covered in the corresponding files.

---

## Scope Notes

This directory does **not** cover:
- `frozenset` (documented separately)
- Regular expressions
- Performance benchmarking
- Internal hashing implementation details

---

## Status

This reference is designed for **long-term maintenance**.

Updates should:
- Preserve the existing structure
- Avoid adding tutorial-style explanations
- Focus on behavior, intent, and correctness
