# Translation Helper Methods (`str`)

Methods in this section are used to translate or transform characters in a string using mapping tables.

These methods are optimized for character-level transformations and are commonly used for sanitization and normalization.

---

## `maketrans()`

### Description
- Creates a translation table to be used with `translate()`.

### Syntax
```python
str.maketrans(x[, y[, z]])
```

**Parameters:**
- `x` – mapping source (string, dict, or Unicode ordinals)
- `y` (optional) – target string (must be the same length as x)
- `z` (optional) – characters to be removed

**Return Value:**
- Returns a translation table (dictionary mapping Unicode ordinals).

**Example (string-to-string mapping):**
```python
table = str.maketrans("abc", "123")
print(table)
```

**Output:**
```text
{97: 49, 98: 50, 99: 51}
```

**Notes:**
- When using two strings, `x` and `y` must have the same length.
- Characters are mapped by position.
- The resulting table is intended for use with `translate()`.

---

## `translate()`

### Description
- Translates characters in a string using a translation table.

### Syntax
```python
str.translate(table)
```

**Parameters:**
- `table` – translation table created by `maketrans()`

**Return Value:**
- Returns a new string with characters translated or removed.

**Example (character replacement):**
```python
table = str.maketrans("abc", "123")
text = "a big cab"
print(text.translate(table))
```

**Output:**
```text
1 2ig 312
```

**Notes:**
- Operates at the character level, not substrings.
- Characters not present in the translation table remain unchanged.
- Faster than chaining multiple `replace()` calls for large strings.
- Cannot perform pattern-based or contextual replacements.
- The translation table keys must be Unicode ordinals, not characters.

---

## Character Removal with `maketrans()`

### Description
- Removes specified characters during translation.

### Syntax
```python
str.maketrans(x, y, z)
```

**Parameters:**
- `z` – string containing characters to be removed

**Return Value:**
- Returns a translation table (dictionary mapping Unicode ordinals).

**Example:**
```python
table = str.maketrans("", "", "aeiou")
text = "hello world"
print(text.translate(table))
```

**Output:**
```text
hll wrld
```

**Notes:**
- Characters listed in z are removed entirely.
- Useful for sanitization and filtering.

## Dictionary-based translation

### Description
- Uses a dictionary mapping Unicode ordinals to replacement characters.

### Syntax
```python
str.translate(mapping)
```

**Parameters:**
- `mapping` – dictionary mapping Unicode ordinal values to: replacement characters, or None to remove the character

**Return Value:**
- Returns a new string with characters translated or removed based on the mapping.

**Example:**
```python
mapping = {
    ord("a"): "1",
    ord("b"): "2",
    ord("c"): None
}

text = "abcabc"
print(text.translate(mapping))
```

**Output:**
```text
1212
```

**Notes:**
- Mapping a character to None removes it.
- Allows fine-grained control over transformations.

---

## Best Practices
- Use `translate()` for bulk character transformations.
- Prefer `translate()` over multiple `replace()` calls for performance.
- Use dictionary-based mappings for complex rules.
- Avoid using these methods for substring or pattern-based transformations.