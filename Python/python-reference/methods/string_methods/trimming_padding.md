# Trimming & Padding Methods (`str`)

Methods in this section are used to remove unwanted characters or adjust string length by adding padding characters.

These methods are commonly used for input cleanup, formatting output, and alignment.

---

## `strip()`

### Description
- Removes leading and trailing whitespace characters from the string.

### Syntax
```python
str.strip()
```

**Parameters:**
- None

**Return Value:**
- Returns a new string with leading and trailing whitespace removed.

**Example:**
```python
text = "   hello world   "
print(text.strip())
```

**Output:**
```text
hello world
```

**Notes:**
- Does not remove whitespace in the middle of the string.
- Useful for cleaning user input.
- Can optionally remove specified characters instead of whitespace.

---

## `lstrip()`

### Description
- Removes leading whitespace characters from the string.

### Syntax
```python
str.lstrip()
```

**Parameters:**
- None

**Return Value:**
- Returns a new string with leading whitespace removed.

**Example:**
```python
text = "   hello world"
print(text.lstrip())
```

**Output:**
```text
hello world
```

**Notes:**
- Only affects the left side of the string.
- Can optionally remove specified characters instead of whitespace.

---

## `rstrip()`

### Description
- Removes trailing whitespace characters from the string.

### Syntax
```python
str.rstrip()
```

**Parameters:**
- None

**Return Value:**
- Returns a new string with trailing whitespace removed.

**Example:**
```python
text = "hello world   "
print(text.rstrip())
```

**Output:**
```text
hello world
```

**Notes:**
- Only affects the right side of the string.
- Can optionally remove specified characters instead of whitespace.

---

## `center()`

### Description
- Centers the string within a specified width.

### Syntax
```python
str.center(width[, fillchar])
```

**Parameters:**
- `width` – total width of the resulting string
- `fillchar` (optional) – padding character (default is space)

**Return Value:**
- Returns a new string centered within the given width.

**Example:**
```python
text = "hello"
print(text.center(11, "-"))
```

**Output:**
```text
---hello---
```

**Notes:**
- If `width` is less than the string length, the original string is returned.
- `fillchar` must be exactly one character.

---

## `ljust()`

### Description
- Left-justifies the string within a specified width.

### Syntax
```python
str.ljust(width[, fillchar])
```

**Parameters:**
- `width` – total width of the resulting string
- `fillchar` (optional) – padding character

**Return Value:**
- Returns a left-aligned string padded to the specified width.

**Example:**
```python
text = "hello"
print(text.ljust(10, "."))
```

**Output:**
```text
hello.....
```

**Notes:**
- Commonly used for tabular text output.

---

## `rjust()`

### Description
- Right-justifies the string within a specified width.

### Syntax
```python
str.rjust(width[, fillchar])
```

**Parameters:**
- `width` – total width of the resulting string
- `fillchar` (optional) – padding character

**Return Value:**
- Returns a right-aligned string padded to the specified width.

**Example:**
```python
text = "hello"
print(text.rjust(10, "."))
```

**Output:**
```text
.....hello
```

**Notes:**
- Useful for aligning numbers in text-based reports.

---

## `zfill()`

### Description
- Pads the string on the left with zeros until it reaches the specified width.

### Syntax
```python
str.zfill(width)
```

**Parameters:**
- `width` – total width of the resulting string

**Return Value:**
- Returns a string left-padded with zeros.

**Example:**
```python
text = "42"
print(text.zfill(5))
```

**Output:**
```text
00042
```

**Notes:**
- Preserves leading sign characters (+ or -).
- Commonly used for numeric string formatting.
- Does not truncate the string if width is smaller than the string length.

---

## Best Practices
- Use trimming methods for input sanitation, not data transformation.
- Use padding methods for presentation purposes only.
