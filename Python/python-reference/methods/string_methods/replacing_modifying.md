# Replacing & Modifying Methods (`str`)

Methods in this section are used to modify string content by replacing, removing, or transforming specific parts of a string.

These methods return a new string and do not modify the original string.

---

## `replace()`

### Description
- Replaces occurrences of a substring with another substring.

### Syntax
```python
str.replace(old, new[, count])
```

**Parameters:**
- `old` – substring to be replaced
- `new` – replacement string
- `count` (optional) – maximum number of replacements

**Return Value:**
- Returns a new string with the specified replacements applied.

**Example:**
```python
text = "one one one"
print(text.replace("one", "two", 2))
```

**Output:**
```text
two two one
```

**Notes:**
- Replaces all occurrences if count is not specified.
- Does not modify the original string.
- Avoid using `replace()` for strict prefix or suffix removal.
- `replace()` performs literal substring replacement, not pattern-based replacement.

---

## `removeprefix()`

### Description
- Removes the specified prefix from the string if it exists.

### Syntax
```python
str.removeprefix(prefix)
```

**Parameters:**
- `prefix` – prefix string to remove

**Return Value:**
- Returns a new string with the prefix removed if present.
- Returns the original string if the prefix does not exist.
- No exception is raised.

**Example:**
```python
text = "v1_report.pdf"
print(text.removeprefix("v1_"))
```

**Output:**
```text
report.pdf
```

**Notes:**
- Performs an exact prefix match.
- Safer and clearer than using `replace()` for prefix handling.
- Does not raise an error if the prefix is not found.

---

## `removesuffix()`

### Description
- Removes the specified suffix from the string if it exists.

### Syntax
```python
str.removesuffix(suffix)
```

**Parameters:**
- `suffix` – suffix string to remove

**Return Value:**
- Returns a new string with the suffix removed if present.
- Returns the original string if the suffix does not exist.

**Example:**
```python
filename = "archive.tar.gz"
print(filename.removesuffix(".gz"))
```

**Output:**
```text
archive.tar
```

**Notes:**
- Performs an exact suffix match.
- Prefer this over `replace()` when working with file extensions.
- Avoids accidental middle-string modifications.

---

## Best Practices
- Use `replace()` for general content replacement.
- Use `removeprefix()` and `removesuffix()` for structural string cleanup.
- Do not use `replace()` when you only intend to modify prefixes or suffixes.
- Prefer semantic methods over generic replacements.