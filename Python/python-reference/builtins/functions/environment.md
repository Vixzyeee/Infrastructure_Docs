# Environment and Interactive Built-in Functions

This file documents **built-in functions intended for interactive environments**.

These functions exist to support:
- the Python REPL
- learning and exploration
- license and environment introspection

They are **not part of Python’s application runtime model**.

---

## Scope

Covered in this file:
- `exit`
- `quit`
- `copyright`
- `credits`
- `license`

Not covered:
- process termination APIs
- system-level exit behavior
- application shutdown patterns

---

## Environment Context

These built-ins are injected primarily for:
- interactive sessions
- educational clarity
- convenience in REPL usage
- They may not exist in embedded or restricted Python environments

They should not appear in production code.

---

## `exit()`

### Definition
Terminates the interpreter session.

### Syntax
```python
exit([status])
```

**Behavior:**
- Raises `SystemExit`
- Terminates the current interpreter
- Accepts an optional status code

**Example:**
```python
exit()
```

**Output:**
```text
(interpreter exits)
```

**Notes:**
- Intended for interactive use
- Internally delegates to `sys.exit`
- Should not be used in libraries

---

## `quit()`

### Definition
Terminates the interpreter session.

### Syntax
```python
quit([status])
```

**Behavior:**
- Alias of `exit()`
- Exists for user convenience

**Example:**
```python
quit()
```

**Output:**
```text
(interpreter exits)
```

**Notes:**
- Same behavior as `exit`
- Provided for readability in REPL contexts

---

## `copyright`

### Definition
Displays Python copyright information.

### Syntax
```python
copyright
```

**Behavior:**
- Prints copyright text
- No return value

**Example:**
```python
print(copyright)
```

**Output:**
```text
Copyright (c) Python Software Foundation
```

**Notes:**
- Exists only for informational purposes
- Meaningful only in interactive sessions

---

## `credits`

### Definition
Displays credits for Python contributors.

### Syntax
```python
credits
```

**Behavior:**
- Prints contributor acknowledgements
- No return value

**Example:**
```python
print(credits)
```

**Output:**

```text
Thanks to CWI, CNRI, BeOpen.com, Zope Corporation...
```

**Notes:**
- Non-programmatic
- Informational only

---

## `license`

### Definition
Displays Python license information.

### Syntax
```python
license
```

**Behavior:**
- Prints license text
- No return value

**Example:**
```python
print(license)
```

**Output:**
```text
Type license() to see the full license text
```

**Notes:**
- Intended for human reading
- Not suitable for automated tooling

---

## Design Notes
- These built-ins exist for **human interaction**, not automation
- They are injected by the interactive environment
- Their presence does not imply production suitability

## Summary
- Environment built-ins support REPL workflows
- They are not part of application logic
- Usage in libraries or services is a design error
- Their inclusion is about user experience, not language power

This file defines **Python’s interactive helper surface**, not runtime APIs.