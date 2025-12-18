# Dictionary Methods (`dict`)

This directory documents commonly used **dictionary methods** in Python.

The focus of this section is:
- What each method does
- Whether it modifies the dictionary in place
- Return values
- Common pitfalls and behavioral details

This is a **reference**, not a tutorial.

---

## Method Categories

Dictionary methods in this directory are grouped by behavior and purpose.

### Access & Query
Methods used to safely access data or inspect dictionary contents  
(**do not modify the dictionary**).

- `get()`
- `keys()`
- `values()`
- `items()`

See: `access_query.md`

---

### Add & Modify
Methods used to add new key-value pairs or modify existing data  
(**modify the dictionary in place**).

- `setdefault()`
- `update()`

See: `add_modify.md`

---

### Remove
Methods used to remove keys and values from a dictionary  
(**modify the dictionary in place**).

- `pop()`
- `popitem()`
- `clear()`

See: `remove.md`

---

### View Objects
Conceptual explanation of dictionary view objects returned by certain methods.

- `dict_keys`
- `dict_values`
- `dict_items`

See: `view.md`

---

### Copying
Methods used to create copies of dictionaries.

- `copy()`

See: `copy.md`

---

## Important Notes

- Dictionaries are **mutable** objects.
- Keys must be **unique** and **hashable**.
- Most dictionary methods **modify the dictionary in place** and return `None`.
- Methods like `keys()`, `values()`, and `items()` return **view objects**, not lists.
- `dict.copy()` creates a **shallow copy**, not a deep copy.

Understanding these behaviors is essential to avoid unintended side effects.

---

## How to Use This Section

- Use this directory as a **quick reference** when working with dictionaries.
- Each file can be read independently.
- This section is designed to complement hands-on usage in an interactive Python shell.
