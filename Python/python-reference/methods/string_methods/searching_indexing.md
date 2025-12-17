# Searching & Indexing Methods (`str`)

Methods in this section are used to search for substrings and retrieve their positions.

Some methods return indexes, while others raise errors when a match is not found.

Understanding the difference between these behaviors is critical to avoid runtime errors.

---

## `find()`

### Description
- Searches for a substring and returns the lowest index where it is found.

### Syntax
```python
str.find(sub[, start[, end]])
```

**Parameters:**
- `sub` – substring to search for
- `start` (optional) – starting index
- `end` (optional) – ending index

**Return Value:**
- Returns the index of the first occurrence of the substring.
- Returns `-1` if the substring is not found.

**Example:**
```python
text = "hello world"
print(text.find("world"))
```

**Output:**
```text
6
```

**Notes:**
- Does not raise an error if the substring is not found.
- Preferred when failure is expected or acceptable.
- Index is zero-based.

---

## `rfind()`

### Description
- Searches for a substring and returns the highest index where it is found.

### Syntax
```python
str.rfind(sub[, start[, end]])
```

**Parameters:**
- `sub` – substring to search for
- `start` (optional) – starting index
- `end` (optional) – ending index

**Return Value:**
- Returns the index of the last occurrence of the substring.
- Returns `-1` if not found.

**Example:**
```python
text = "one two one"
print(text.rfind("one"))
```

**Output:**
```text
8
```

**Notes:**
- Searches from right to left.
- Returns `-1` when the substring is not found.

---

## `index()`

### Description
- Searches for a substring and returns its lowest index.

### Syntax
```python
str.index(sub[, start[, end]])
```

**Parameters:**
- `sub` – substring to search for
- `start` (optional) – starting index
- `end` (optional) – ending index

**Return Value:**
- Returns the index of the first occurrence.

**Raises:**
- `ValueError` if the substring is not found.

**Example:**
```python
text = "hello world"
print(text.index("world"))
```

**Output:**
```text
6
```

**Notes:**
- Use only when the substring is guaranteed to exist.
- Otherwise, wrap in `try-except`.
- Using this method without validation may cause runtime errors.

---

## `rindex()`

### Description
- Searches for a substring and returns the highest index.

### Syntax
```python
str.rindex(sub[, start[, end]])
```

**Parameters:**
- `sub` – substring to search for
- `start` (optional) – starting index
- `end` (optional) – ending index

**Return Value:**
- Returns the index of the last occurrence.

**Raises:**
- `ValueError` if not found.

**Example:**
```python
text = "one two one"
print(text.rindex("one"))
```

**Output:**
```text
8
```

**Notes:**
- Searches from the right side of the string.
- Raises `ValueError` if the substring is not found.

---

## `count()`

### Description
- Counts the number of non-overlapping occurrences of a substring.

### Syntax
```python
str.count(sub[, start[, end]])
```

**Parameters:**
- `sub` – substring to count
- `start` (optional)
- `end` (optional)

**Return Value:**
- Returns the number of occurrences.

**Example:**
```python
text = "banana"
print(text.count("a"))
```

**Output:**
```text
3
```

**Notes:**
- Overlapping matches are not counted.
- Returns `0` if the substring is not found.
- Useful for simple frequency checks without slicing or looping.
- Does not provide position information.
- Not suitable when exact match positions are required.

---

## Comparison Summary

| Method   | Not Found Behavior  | Search Direction |
|----------|---------------------|------------------|
| `find`   | Returns `-1`        | Left → Right |
| `rfind`  | Returns `-1`        | Right → Left |
| `index`  | Raises `ValueError` | Left → Right |
| `rindex` | Raises `ValueError` | Right → Left |
| `count`  | Returns `0`         | N/A |

## Best Practices
- Use `find()` / `rfind()` when absence is a valid outcome.
- Use `index()` / `rindex()` only when the substring is guaranteed to exist.
- Avoid using `index()` without validation in user-facing input.
