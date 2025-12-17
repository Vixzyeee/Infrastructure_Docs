# Encoding & Formatting Methods (`str`)

Methods in this section are used to encode strings into bytes or adjust text layout for formatting purposes.

These methods are commonly used in file handling, networking, and working with legacy or structured text.

---

## `encode()`

### Description
- Encodes the string into a bytes object using a specified encoding.

### Syntax
```python
str.encode(encoding="utf-8", errors="strict")
```

**Parameters:**
- `encoding` (optional) – text encoding to use (default: "`utf-8`")
- `errors` (optional) – error handling scheme

**Return Value:**
- Returns a bytes object.

**Example:**
```python
text = "hello"
data = text.encode("utf-8")
print(data)
```

**Output:**
```text
b'hello'
```

**Notes:**
- Strings (`str`) and bytes (`bytes`) are different types in Python.
- Encoding converts text into bytes for storage or transmission.
- Common encodings include "`utf-8`", "`ascii`", and "`latin-1`".
- Encoding errors only occur when the target encoding cannot represent certain characters.

---

## `encode()` error handling

### Description
- Controls how encoding errors are handled.

**Common Error Modes:**
- "`strict`" – raises a `UnicodeEncodeError`
- "`ignore`" – skips characters that cannot be encoded
- "`replace`" – replaces invalid characters with `?`
- "backslashreplace" – uses python escape sequences

**Example:**
```python
text = "café"
print(text.encode("ascii", errors="replace"))
```

**Output:**
```text
b'caf?'
```

**Notes:**
- "`ignore`" may silently lose data.
- "`replace`" is safer for logging and debugging.
- "`strict`" is recommended when data integrity matters.
- Decoding is the reverse operation and is performed on `bytes`, not `str`.

---

## `expandtabs()`

### Description
- Replaces tab characters (`\t`) with spaces.

### Syntax
```python
str.expandtabs(tabsize=8)
```

**Parameters:**
- `tabsize` (optional) – number of spaces per tab stop (default: `8`)

**Return Value:**
- Returns a new string with tabs expanded to spaces.

**Example:**
```python
text = "a\tb\tc"
print(text.expandtabs(4))
```

**Output:**
```text
a   b   c
```

**Notes:**
- Useful when normalizing text from legacy systems.
- Helps align text for display or logging.
- Does not affect spaces already present in the string.
- Tab expansion depends on the current column position, not a fixed number of spaces.

---

## Common Pitfalls
- Encoding is not encryption.
- Encoding is not compression.
- Do not mix str and bytes without explicit encoding or decoding.
- Always know whether your data is text or binary.

---

## Best Practices
- Encode strings only at system boundaries (files, network, APIs).
- Use UTF-8 unless you have a strong reason not to.
- Avoid "`ignore`" unless data loss is acceptable.
- Use `expandtabs()` only for presentation, not data storage.

