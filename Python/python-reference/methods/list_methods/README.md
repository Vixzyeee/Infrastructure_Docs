# List Methods (`list`)

This directory documents commonly used **list methods** in Python.

The focus is on:
- What each method does
- Whether it modifies the list in place
- Return values
- Common pitfalls and usage notes

This section is intended as a **practical reference**, not a tutorial.

---

## Method Categories

The list methods are grouped by behavior and purpose:

- **Add & Modify**
  - `append()`
  - `extend()`
  - `insert()`

- **Remove**
  - `pop()`
  - `remove()`
  - `clear()`

- **Search & Query**
  - `index()`
  - `count()`

- **Reorder**
  - `reverse()`
  - `sort()`

- **Copying**
  - `copy()`

Each category is documented in its own file.

---

## Important Notes

- Most list methods **modify the list in place** and return `None`.
- Some methods return values (`pop()`, `index()`), others do not.
- Lists are **mutable** objects. Changes affect all references unless explicitly copied.
- `list.copy()` creates a **shallow copy**, not a deep copy.

Understanding these behaviors is critical to avoid unintended side effects.

---

## How to Use This Section

- Use this as a quick reference when working with Python lists.
- Read category files independently; they are not meant to be read in order.
- Combine this section with examples and experiments in an interactive Python shell.
