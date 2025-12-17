# Case Transformation Methods (`str`)

Methods in this section are used to change the letter casing of a string.

All string case transformation methods return a new string.

---

## `lower()`

### Description
- Converts all alphabetic characters in the string to lowercase.

### Syntax
```python
str.lower()
```

**Parameters:**
- None

**Return Value:**
- Returns a new string with all characters converted to lowercase.

**Example:**
```python
text = "Hello WORLD"
result = text.lower()
print(result)
```

**Output:**
```text
hello world
```

**Notes:**
- The original string is not modified (strings are immutable).
- Commonly used for normalization before comparison.

---

## `upper()`

### Description
- Converts all alphabetic characters in the string to uppercase.

### Syntax
```python
str.upper()
```

**Parameters:**
- None

**Return Value:**
- Returns a new string with all characters converted to uppercase.

**Example:**
```python
text = "Hello world"
print(text.upper())
```

**Output:**
```text
HELLO WORLD
```

**Notes:**
- Does not affect non-alphabetic characters.
- Useful for formatting output or enforcing consistency.

---

## `capitalize()`

### Description
- Converts the first character of the string to uppercase and the rest to lowercase.

### Syntax
```python
str.capitalize()
```

**Parameters:**
- None

**Return Value:**
- Returns a new string with the first character capitalized.

**Example:**
```python
text = "hELLO WORLD"
print(text.capitalize())
```

**Output:**
```text
Hello world
```

**Notes:**
- Only affects the first character.
- Remaining characters are forced to lowercase.

---

## `title()`

### Description
- Converts the first character of each word to uppercase.

### Syntax
```python
str.title()
```

**Parameters:**
- None

**Return Value:**
- Returns a new string with each word capitalized.

**Example:**
```python
text = "hello world from python"
print(text.title())
```

**Output:**
```text
Hello World From Python
```

**Notes:**
- Word boundaries are determined by whitespace and punctuation.
- Not suitable for proper noun formatting in all languages.

---

## `swapcase()`

### Description
- Swaps the case of all alphabetic characters.
- Uppercase becomes lowercase and vice versa.

### Syntax
```python
str.swapcase()
```

**Parameters:**
- None

**Return Value:**
- Returns a new string with swapped character cases.

**Example:**
```python
text = "Hello WORLD"
print(text.swapcase())
```

**Output:**
```text
hELLO world
```

**Notes:**
- Useful for debugging or text transformations.
- Non-alphabetic characters are unchanged.

---

## `casefold()`

### Description
- Converts the string to a case-insensitive form suitable for comparison.

### Syntax
```python
str.casefold()
```

**Parameters:**
- None

**Return Value:**
- Returns a new string optimized for case-insensitive comparison.

**Example:**
```python
text = "Straße"
print(text.casefold())
```

**Output:**
```text
strasse
```

**Notes:**
- More aggressive than `lower()`.
- Recommended for internationalized string comparisons.
- Preferred over `lower()` when performing case-insensitive comparisons.

---
