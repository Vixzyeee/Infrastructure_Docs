# Python Operators Reference

This directory documents **Python operators** as a long-term technical reference.

Some operators are spelled as keywords (e.g. `and`, `or`, `not`), but their behavior is defined at the operator level.

Operators are **language-level constructs** that define how expressions are evaluated.
They are not functions, not methods, and not interchangeable with keywords or built-ins.

This reference focuses on **operator semantics and behavior**, not tutorials or beginner explanations.

---

## Scope

Covered in this directory:
- Arithmetic operators
- Comparison operators
- Assignment operators
- Logical operators
- Membership and identity operators
- Bitwise operators
- Operator precedence rules

Not covered here:
- Data type behavior
- Control flow (`if`, `while`, `for`)
- Operator overloading (`__add__`, `__eq__`, etc.)
- Boolean theory or formal grammar

Those topics are documented elsewhere in the repository.

---

## Directory Structure

```text
operators/
├── arithmetic.md
├── comparison.md
├── assignment.md
├── logical.md
├── membership_identity.md
├── bitwise.md
├── precedence.md
└── README.md
```

Each file focuses on **one operator category** and can be read independently.

---

## File Overview

### `arithmetic.md`

Covers numeric operators such as:
- `+`, `-`, `*`, `/`, `//`, `%`, `**`
- Unary `+` and `-`

Focus:
- Numeric behavior
- Floor division and modulo rules
- Operator semantics independent of data types

---

### `comparison.md`

Covers comparison operators:
- `==`, `!=`
- `<`, `<=`, `>`, `>=`

Focus:
- Value comparison vs identity
- Chained comparisons
- Type compatibility rules

---

### `assignment.md`

Covers assignment-related operators:
- `=`
- Augmented assignment (`+=`, `-=`, etc.)
- Assignment expressions (`:=`)

Focus:
- Binding vs mutation
- Evaluation order
- Common pitfalls with mutable objects

---

### `logical.md`

Covers logical operators:
- `and`, `or`, `not`

Focus:
- Short-circuit evaluation
- Truthiness-based behavior
- Return values that are not booleans

---

### `membership_identity.md`

Covers membership and identity operators:
- `in`, `not in`
- `is`, `is not`

Focus:
- Containment vs identity
- Correct and incorrect uses of `is`
- Common sources of subtle bugs

---

### `bitwise.md`

Covers bitwise operators:
- `&`, `|`, `^`, `~`
- `<<`, `>>`

Focus:
- Bit-level behavior
- Flags, masks, and shifts
- Differences from logical operators

---

### `precedence.md`

Covers operator precedence rules.

Focus:
- Evaluation order
- Right vs left associativity
- Practical precedence pitfalls
- When to use parentheses for clarity

---

## Design Principles
- **Concept-first:** explain behavior before usage patterns
- **No duplication:** operators are not re-explained in other sections
- **Practical focus:** real-world semantics over formal grammar
- **Long-term readability:** written to be useful months or years later

This directory is intended to be **read selectively**, not sequentially.

---

## Intended Audience

This reference is for:
- Developers who already use Python
- Readers who want precise operator behavior
- Anyone debugging expression-level logic

It is **not** a beginner tutorial.

## Final Notes

If you are unsure how an expression evaluates:
- Check the relevant operator file
- Check precedence rules
- Use parentheses explicitly
- When in doubt, choose clarity over cleverness

Python is predictable. Most bugs come from incorrect assumptions, not hidden behavior.