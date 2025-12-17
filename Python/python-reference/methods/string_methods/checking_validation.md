# Checking & Validation Methods (`str`)

Methods in this section are used to validate string content.

All methods return a boolean value (`True` or `False`).

These methods are commonly used for input validation, parsing, and data sanitization.

---

## `isalnum()`

### Description
- Checks whether all characters in the string are alphanumeric.
- Letters and numbers are allowed.
- Whitespace and symbols are not allowed.

### Syntax
```python
str.isalnum()
```

**Parameters:**
None

**Return Value:**
Returns True if all characters are alphanumeric and the string is not empty.

**Example:**
```python
text = "User123"
print(text.isalnum())
```

**Output:**
```text
True
```

**Notes:**
- Returns False if the string contains spaces or special characters.
- An empty string returns False.

---

## `isalpha()`

### Description
- Checks whether all characters in the string are alphabetic.

### Syntax
```python
str.isalpha()
```

**Parameters:**
None

**Return Value:**
Returns True if all characters are letters and the string is not empty.

**Example:**
```python
text = "Python"
print(text.isalpha())
```

**Output:**
```text
True
```

**Notes:**
- Spaces and numbers cause this method to return False.

---

## `isascii()`

### Description
- Checks whether all characters in the string are ASCII characters.

### Syntax
```python
str.isascii()
```

**Parameters:**
None

**Return Value:**
Returns True if all characters are within the ASCII range.

**Example:**
```python
text = "Hello!"
print(text.isascii())
```

**Output:**
```text
True
```

**Notes:**
- Non-ASCII characters such as accented letters return False.

---

## `isdecimal()`

### Description
- Checks whether all characters in the string are decimal characters.

### Syntax
```python
str.isdecimal()
```

**Parameters:**
None

**Return Value:**
Returns True if all characters are decimal digits.

**Example:**
```python
text = "123"
print(text.isdecimal())
```

**Output:**
```text
True
```

**Notes:**
- Only accepts characters used in base-10 numbers.
- Useful for validating numeric input.

---

## `isdigit()`

### Description
- Checks whether all characters in the string are digits.

### Syntax
```python
str.isdigit()
```

**Parameters:**
None

**Return Value:**
Returns True if all characters are digits.

**Example:**
```python
text = "²"
print(text.isdigit())
```

**Output:**
```text
True
```

**Notes:**
- Accepts digits beyond base-10.
- Slightly broader than `isdecimal()`.

---

## `isnumeric()`

### Description
- Checks whether all characters in the string are numeric characters.

### Syntax
```python
str.isnumeric()
```

**Parameters:**
None

**Return Value:**
Returns True if all characters are numeric.

**Example:**
```python
text = "½"
print(text.isnumeric())
```

**Output:**
```text
True
```

**Notes:**
- Most permissive numeric check.
- Includes fractions and other numeric symbols.

---

## `isidentifier()`

### Description
- Checks whether the string is a valid Python identifier.

### Syntax
```python
str.isidentifier()
```

**Parameters:**
None

**Return Value:**
Returns True if the string is a valid identifier.

**Example:**
```python
text = "variable_name"
print(text.isidentifier())
```

**Output:**
```text
True
```

**Notes:**
- Useful when validating dynamic variable or attribute names.
- Keywords are not checked here.

---

## `islower()`

### Description
- Checks whether all alphabetic characters in the string are lowercase.

### Syntax
```python
str.islower()
```

**Parameters:**
None

**Return Value:**
Returns True if all letters are lowercase.

**Example:**
```python
text = "hello"
print(text.islower())
```

**Output:**
```text
True
```

**Notes:**
- Non-alphabetic characters are ignored.

---

## `isupper()`

### Description
- Checks whether all alphabetic characters in the string are uppercase.

### Syntax
```python
str.isupper()
```

**Parameters:**
None

**Return Value:**
Returns True if all letters are uppercase.

**Example:**
```python
text = "HELLO"
print(text.isupper())
```

**Output:**
```text
True
```

**Notes:**
- Returns `False` if there are no alphabetic characters in the string.
- Non-alphabetic characters are ignored.

---

## `istitle()`

### Description
- Checks whether the string follows title case formatting.

### Syntax
```python
str.istitle()
```

**Parameters:**
None

**Return Value:**
Returns True if each word starts with an uppercase letter.

**Example:**
```python
text = "Hello World"
print(text.istitle())
```

**Output:**
```text
True
```

**Notes:**
- Useful for formatting checks, not language correctness.

---

## `isspace()`

### Description
- Checks whether the string contains only whitespace characters.

### Syntax
```python
str.isspace()
```

**Parameters:**
None

**Return Value:**
Returns True if the string contains only whitespace.

**Example:**
```python
text = "   "
print(text.isspace())
```

**Output:**
```text
True
```

**Notes:**
- Returns `False` if the string is empty.
- Includes spaces, tabs, and newline characters.

---

## `isprintable()`

### Description
- Checks whether all characters in the string are printable.

### Syntax
```python
str.isprintable()
```

**Parameters:**
None

**Return Value:**
Returns True if all characters can be printed.

**Example:**
```python
text = "Hello\n"
print(text.isprintable())
```

**Output:**
```text
False
```

**Notes:**
- Newline and tab characters are not considered printable.

---
