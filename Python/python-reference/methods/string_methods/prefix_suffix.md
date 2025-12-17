# Prefix & Suffix Methods (`str`)

Methods in this section are used to check whether a string starts or ends with a specific substring.

These methods are commonly used for validation, parsing, filtering, and enforcing naming or format rules.

---

## `startswith()`

### Description
- Checks whether the string starts with the specified prefix.

### Syntax
```python
str.startswith(prefix[, start[, end]])
```

**Parameters:**
- `prefix` – string or tuple of strings to check
- `start` (optional) – starting index
- `end` (optional) – ending index

**Return Value:**
- Returns `True` if the string starts with the given prefix.
- Returns `False` otherwise.

**Example:**
```python
filename = "report.pdf"
print(filename.startswith("report"))
```

**Output:**
```text
True
```

**Example (tuple usage):**
```python
filename = "image.png"
print(filename.startswith(("image", "photo")))
```

**Output:**
```text
True
```

**Notes:**
- Does not search the entire string, only checks the beginning.
- Accepting a tuple makes this useful for validating multiple prefixes.
- Safer and clearer than using slicing or `find()` for prefix checks.
- Supports optional start and end indexes for partial string checks.

---

## `endswith()`

### Description
- Checks whether the string ends with the specified suffix.

### Syntax
```python
str.endswith(suffix[, start[, end]])
```

**Parameters:**
- `suffix` – string or tuple of strings to check
- `start` (optional) – starting index
- `end` (optional) – ending index

**Return Value:**
- Returns `True` if the string ends with the given suffix.
- Returns `False` otherwise.

**Example:**
```python
filename = "archive.tar.gz"
print(filename.endswith(".gz"))
```

**Output:**
```text
True
```

**Example (tuple usage):**
```python
filename = "script.py"
print(filename.endswith((".py", ".sh")))
```

**Output:**
```text
True
```

**Notes:**
- Commonly used for file extension validation.
- More readable and less error-prone than manual slicing.
- Works reliably even when suffix length varies.
- Optional start and end parameters allow suffix checks on substrings.

---

## Best Practices
- Use these methods for semantic checks, not substring searching.
- Prefer tuple arguments when validating multiple prefixes or suffixes.
