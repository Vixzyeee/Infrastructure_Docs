# Python String Methods (`str`)

This directory provides a structured reference for Python `str` methods.
Methods are grouped by behavior and intent, not alphabetically.

This is a **reference**, not a tutorial.

---

## Overview

Python strings are **immutable**.
All string methods return a new string and never modify the original value.

This directory focuses on:
- Correct method usage
- Behavioral differences between similar methods
- Practical, real-world examples
- Avoiding common misuse and bugs

---

## Directory Structure

| File | Description |
|-----|------------|
| `case_transformation.md` | Change character casing (`lower`, `upper`, `casefold`, etc.) |
| `checking_validation.md` | Validate string content (`isalpha`, `isdigit`, etc.) |
| `searching_indexing.md` | Locate substrings and indexes (`find`, `index`, `count`) |
| `trimming_padding.md` | Remove or add characters for layout (`strip`, `ljust`, `zfill`) |
| `splitting_joining.md` | Split, join, and partition strings |
| `prefix_suffix.md` | Semantic prefix and suffix checks |
| `replacing_modifying.md` | Modify string content safely |
| `translation_helpers.md` | Character-level transformations (`maketrans`, `translate`) |
| `encoding_formatting.md` | Encoding and layout normalization |
| `formatting.md` | String formatting (`format`, `format_map`) |

---

## Recommended Reading Order

If you are new to string manipulation, read in this order:

1. `case_transformation.md`
2. `checking_validation.md`
3. `searching_indexing.md`
4. `trimming_padding.md`
5. `splitting_joining.md`
6. `prefix_suffix.md`
7. `replacing_modifying.md`
8. `translation_helpers.md`
9. `encoding_formatting.md`
10. `formatting.md`

If you are using this as a reference, jump directly to the relevant file.

---

## Usage Principles

- Prefer **semantic methods** (`startswith`, `removeprefix`) over generic ones (`find`, `replace`) when intent matters.
- Avoid chaining multiple string operations when a dedicated method exists.
- Use character-level methods (`translate`) only when substring methods are insufficient.
- Encode strings only at system boundaries (files, network, APIs).

---

## Scope Notes

This directory does **not** cover:
- Regular expressions
- Bytes (`bytes`) methods
- Localization or internationalization APIs

Those topics belong in separate references.

---

## Status

This reference is designed for long-term maintenance and extension.
New methods or clarifications should follow the existing structure and style.
