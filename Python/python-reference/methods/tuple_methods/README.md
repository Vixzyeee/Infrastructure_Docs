# Tuple Methods (`tuple`)

This directory documents **Python tuple methods**.

Tuples are **immutable sequences**.  
Because of this design choice, tuples expose **very few methods** compared to other built-in data types such as lists, dictionaries, or sets.

This is intentional.

---

## Scope

This directory focuses **strictly on tuple methods**, not tuple concepts.

Covered here:
- Available tuple methods
- Method behavior
- Return values
- Common pitfalls

Not covered here:
- Tuple creation
- Indexing and slicing
- Unpacking
- Immutability concepts
- Usage patterns

Those topics are documented separately under **tuple concepts**.

---

## Available Methods

Tuples provide only **two public methods**:

| Method    | Purpose                    |
|-----------|----------------------------|
| `count()` | Frequency inspection       |
| `index()` | Positional lookup          |

Both methods:
- Return values
- Do not modify the tuple
- Perform linear scans (`O(n)`)

---

## File Structure

```text
tuple_methods/
├── README.md
└── searching_indexing.md
```

### searching_indexing.md

Documents:
- `count()`
- `index()`
- Safe usage patterns
- Common mistakes

## Design Notes
- Tuples prioritize **data integrity** over flexibility
- The lack of mutating methods is a feature, not a limitation
- If frequent mutation or complex operations are required, use a list instead
- If frequent membership checks are required, consider using a set

This directory intentionally remains small to reflect the **minimal API surface** of tuples.

## Summary
- Tuples expose very few methods by design
- All tuple methods are read-only
- This directory documents tuple methods only
- Conceptual topics are documented elsewhere

This directory is intentionally minimal and complete.