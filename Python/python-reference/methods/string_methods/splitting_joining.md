# Splitting, Joining & Partitioning Methods (`str`)

Methods in this section are used to split strings into parts, join iterables into strings, or divide strings into structured segments.

These methods are commonly used in parsing, data processing, and text manipulation.

---

## `split()`

### Description
- Splits the string into a list using a specified delimiter.

### Syntax
```python
str.split(sep=None, maxsplit=-1)
```

**Parameters:**
- `sep` (optional) – delimiter to split on (default: any whitespace)
- `maxsplit` (optional) – maximum number of splits

**Return Value:**
- Returns a list of substrings.

**Example:**
```python
text = "a,b,c,d"
print(text.split(",", 2))
```

**Output:**
```text
['a', 'b', 'c,d']
```

**Notes:**
- Consecutive whitespace is treated as a single separator when `sep` is `None`.
- If `sep` is specified, exact matches are used.
- Common source of bugs when input format is inconsistent.
- When `maxsplit` is specified, splitting is performed at most `maxsplit` times.
- Remaining content is included as the last element.
- When `sep` is an empty string, a `ValueError` is raised.

---

## `rsplit()`

### Description
- Splits the string from the right side.

### Syntax
```python
str.rsplit(sep=None, maxsplit=-1)
```

**Parameters:**
- `sep` (optional) – delimiter to split on (default: any whitespace)
- `maxsplit` (optional) – maximum number of splits

**Return Value:**
- Returns a list of substrings.

**Example:**
```python
text = "one-two-three"
print(text.rsplit("-", 1))
```

**Output:**
```text
['one-two', 'three']
```

**Notes:**
- Useful when only the last separator matters (e.g., file extensions).
- Splitting starts from the right, but the result order remains left to right.

--- 

## `splitlines()`

### Description
- Splits the string at line boundaries.

### Syntax
```python
str.splitlines(keepends=False)
```

**Parameters:**
- `keepends` (optional) – include line break characters if True

**Return Value:**
- Returns a list of lines.

**Example:**
```python
text = "line1\nline2\nline3"
print(text.splitlines())
```

**Output:**
```text
['line1', 'line2', 'line3']
```

**Notes:**
- Supports multiple line break formats.
- Safer than manually splitting on `\n`.
- Handles different newline conventions such as `\n`, `\r\n`, and `\r`.

---

## `join()`

### Description
- Joins elements of an iterable into a single string using the string as a separator.

### Syntax
```python
str.join(iterable)
```

**Parameters:**
- `iterable` – iterable containing string elements

**Return Value:**
- Returns a new joined string.

**Example:**
```python
items = ["one", "two", "three"]
print(",".join(items))
```

**Output:**
```text
one,two,three
```

**Notes:**
- All elements in the iterable must be strings.
- This method is often misunderstood: the separator is the string object itself.
- Raises `TypeError` if any element in the iterable is not a string.

---

## `partition()`

### Description
- Splits the string into three parts using the first occurrence of a separator.

### Syntax
```python
str.partition(sep)
```

**Parameters:**
- `sep` – separator string

**Return Value:**
- Returns a tuple: `(before, sep, after)`

**Example:**
```python
text = "user:password"
print(text.partition(":"))
```

**Output:**
```text
('user', ':', 'password')
```

**Notes:**
- Always returns a tuple of three elements.
- If the separator is not found, the result is:
  `("original_string", "", "")`

---

## `rpartition()`

### Description
- Splits the string into three parts using the last occurrence of a separator.

### Syntax
```python
str.rpartition(sep)
```

**Parameters:**
- `sep` – separator string

**Return Value:**
- Returns a tuple: `(before, sep, after)`

**Example:**
```python
text = "path/to/file.txt"
print(text.rpartition("/"))
```

**Output:**
```text
('path/to', '/', 'file.txt')
```

**Notes:**
- Useful for extracting filenames or extensions.
- Safer than `split()` when structure must be preserved.
- If the separator is not found, the result is:
  `("", "", "original_string")`

---

## Best Practices
- Prefer `partition()` / `rpartition()` when exact structure matters.
- Avoid using `split()` when the number of segments is unpredictable.
- Avoid chaining `split()` calls when a structured separator is available.
- Do not use `split()` as a replacement for structured parsing.
