# String Formatting Methods (`str`)

Methods in this section are used to format strings by substituting values into placeholders.

These methods predate f-strings and are still widely used in legacy code, libraries, and dynamic formatting scenarios.

---

## `format()`

### Description
- Formats a string by replacing placeholders with provided values.

### Syntax
```python
str.format(*args, **kwargs)
```

**Parameters:**
- `*args` – positional values to substitute
- `**kwargs` – keyword values to substitute

**Return Value:**
- Returns a new formatted string.

**Example (positional arguments):**

```python
text = "Hello, {}!"
print(text.format("Pito"))
```

**Output:**
```text
Hello, Pito!
```

**Example (keyword arguments):**
```python
text = "User: {name}, Age: {age}"
print(text.format(name="Pito", age=21))
```

**Output:**
```text
User: Pito, Age: 21
```

**Notes:**
- Placeholders are defined using `{}`.
- Positional and keyword arguments can be mixed.
- Raises `KeyError` if a named placeholder is missing.
- Extra arguments are ignored if not referenced in the format string.

## Format Specifiers

### Description
- Controls alignment, width, precision, and numeric formatting.

**Example:**
```python
value = 3.14159
print("Pi: {:.2f}".format(value))
```

**Output:**
```text
Pi: 3.14
```

**Notes:**
- Format specifiers follow the syntax `{value:format}`.
- Common specifiers include:
  - `.2f` – floating-point precision
  - `>10` – right alignment with width
  - `<10` – left alignment with width
  - `^10` – center alignment

## `format_map()`

### Description
- Similar to format(), but uses a mapping (dictionary-like object) instead of keyword arguments.

### Syntax
```python
str.format_map(mapping)
```

**Parameters:**
- mapping – a dictionary or mapping object

**Return Value:**
- Returns a new formatted string.

**Example:**
```python
data = {"name": "Pito", "role": "Backend"}
text = "Name: {name}, Role: {role}"
print(text.format_map(data))
```

**Output:**
```text
Name: Pito, Role: Backend
```

**Notes:**
- Useful when formatting from dynamic data sources.
- Avoids unpacking dictionaries into keyword arguments.
- Raises `KeyError` if a placeholder is missing.

## Comparison with f-strings

| Feature       | `format()` / `format_map()`  | f-strings   |
|---------------|:-----------------------------|-------------|
| Introduced in | Python 2.6                   | Python 3.6  |
| Readability   | Medium                       | High        |
| Dynamic keys  | Yes                          | Limited     |
| Performance   | Slower                       | Faster      |
| Legacy code   | Common                       | Rare        |

## Best Practices
- Prefer f-strings for new code when values are known at write-time.
- Use `format()` or `format_map()` when formatting dynamically.
- Avoid mixing formatting styles in the same codebase.
- Always validate external data before formatting into strings.