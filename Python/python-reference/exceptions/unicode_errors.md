# Unicode Errors (Text Encoding & Decoding Failures)

This document covers **Unicode-related exceptions**.

These exceptions occur when Python fails to **encode, decode, or translate text** between Unicode (`str`) and byte representations (`bytes`).

Unicode errors are runtime errors and inherit from `UnicodeError`.

---

## Overview

Unicode errors usually indicate:
- Mismatched text encodings
- Incorrect assumptions about input data
- Mixing `str` and `bytes` improperly
- Invalid byte sequences

These errors are extremely common when dealing with:
- Files
- Network data
- External APIs
- Legacy systems

---

## `UnicodeError`

### Description
Base class for all Unicode-related exceptions.

**Example:**
```python
raise UnicodeError("Generic Unicode failure")
```

**Error:**
```text
UnicodeError: Generic Unicode failure
```

**Notes:**
- Rarely raised directly
- Most Unicode failures raise specific subclasses

**Rule:**
Always catch specific Unicode error subclasses.

---

## `UnicodeDecodeError`

### Description
Raised when **decoding bytes into text fails**.

This happens when Python encounters **invalid byte sequences** for the specified encoding.

**Example:**
```python
data = b"\xff"
data.decode("utf-8")
```

**Error:**
```text
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff
```

**Notes:**
- Most common Unicode error
- Often caused by assuming UTF-8 incorrectly

**Rule:**
Never assume encoding. Detect or define it explicitly.

---

## `UnicodeEncodeError`

### Description
Raised when **encoding text into bytes fails**.

This happens when characters cannot be represented in the target encoding.

**Example:**
```python
text = "€"
text.encode("ascii")
```

**Error:**
```text
UnicodeEncodeError: 'ascii' codec can't encode character
```

**Notes:**
- Common when using legacy encodings
- ASCII cannot represent most non-English characters

**Rule:**
Use UTF-8 unless you have a very good reason not to.

---

## `UnicodeTranslateError`

### Description
Raised when **character mapping fails during translation**.

Usually occurs when using `str.translate()` with incomplete mappings.

**Example:**
```python
table = {ord("a"): None}
"abc".translate(table)
```

**Error:**
```text
UnicodeTranslateError
```

**Notes:**
- Rare compared to encode/decode errors
- Mostly appears in advanced text processing

**Rule:**
Ensure translation tables handle all expected characters.

---

## Common Patterns & Mistakes

**❌ Mixing `str` and `bytes`**
```python
data = b"hello"
print(data + "world")
```

This will raise a `TypeError`, not a Unicode error, but it usually leads to Unicode bugs later.

❌ Assuming UTF-8 Everywhere
```python
open("data.txt").read()
```

This assumes UTF-8 implicitly.

**✅ Explicit Encoding**
```python
open("data.txt", encoding="utf-8").read()
```

**✅ Defensive Decoding**
```python
data.decode("utf-8", errors="replace")
```

---

## Summary
- Unicode errors involve text encoding and decoding
- `UnicodeError` is the base class
- `UnicodeDecodeError` is the most common
- `UnicodeEncodeError` appears with legacy encodings
- `UnicodeTranslateError` is rare but real
- Always be explicit about encodings

If text breaks silently, your encoding assumptions are wrong.