# String Methods

This document covers commonly used Python string methods.
Strings in Python are immutable. All methods return a new string.

---

## str.upper()
Convert all characters to uppercase.

### Syntax
```python
str.upper()
```

**Parameters:**

None

**Return Value:**
str

**Example:**
```python
text = "hello world"
result = text.upper()
print(result)
```

**Output:**
```text
HELLO WORLD
```

**Notes:**
- Original string is not modified

## str.lower()
Convert all characters to lowercase.

Syntax
python
Copy code
str.lower()
Parameters
None

Return Value
str

Example
python
Copy code
text = "HeLLo"
print(text.lower())
Output
text
Copy code
hello
Notes
Useful for case-insensitive comparison

## str.strip()
Remove leading and trailing whitespace.

Syntax
python
Copy code
str.strip()
Parameters
None

Return Value
str

Example
python
Copy code
text = "   hello   "
print(text.strip())
Output
text
Copy code
hello
Notes
Does not remove internal spaces

## str.split()
Split string into a list.

Syntax
python
Copy code
str.split(separator=None)
Parameters
separator (optional): delimiter string

Return Value
list[str]

Example
python
Copy code
text = "a,b,c"
print(text.split(","))
Output
text
Copy code
['a', 'b', 'c']
Notes
Default splits on whitespace

## str.join()
Join iterable elements into a string.

Syntax
python
Copy code
str.join(iterable)
Parameters
iterable: sequence of strings

Return Value
str

Example
python
Copy code
items = ["a", "b", "c"]
print(",".join(items))
Output
text
Copy code
a,b,c
Notes
All elements must be strings

## str.replace()
Replace occurrences of a substring.

Syntax
python
Copy code
str.replace(old, new, count=-1)
Parameters
old: substring to replace

new: replacement

count (optional): max replacements

Return Value
str

Example
python
Copy code
text = "hello world"
print(text.replace("world", "python"))
Output
text
Copy code
hello python
Notes
Replaces all occurrences by default

## str.startswith()
Check if string starts with a prefix.

Syntax
python
Copy code
str.startswith(prefix)
Parameters
prefix: string or tuple of strings

Return Value
bool

Example
python
Copy code
text = "hello.py"
print(text.startswith("hello"))
Output
text
Copy code
True
Notes
Case-sensitive

## str.endswith()
Check if string ends with a suffix.

Syntax
python
Copy code
str.endswith(suffix)
Parameters
suffix: string or tuple of strings

Return Value
bool

Example
python
Copy code
filename = "script.py"
print(filename.endswith(".py"))
Output
text
Copy code
True
Notes
Commonly used for file validation
