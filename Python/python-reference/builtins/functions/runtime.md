# Runtime Code Execution Built-in Functions

This file documents **built-in functions that execute or manipulate code at runtime**.

These functions operate on Python code objects or source code directly.
They are powerful, dangerous, and intentionally low-level.

---

## Scope

Covered in this file:
- `eval`
- `exec`
- `compile`
- `breakpoint`

Not covered:
- debugging tools
- AST manipulation
- sandboxing techniques
- security hardening

---

## Runtime Context

Python allows code to be:
- generated dynamically
- compiled explicitly
- executed at runtime

These built-ins expose that capability directly.
They exist for **interpreter control and tooling**, not application logic.

---

## `eval()`

### Definition
Evaluates a Python expression and returns its result.

### Syntax
```python
eval(expression[, globals[, locals]])
```

**Behavior:**
- Accepts a single expression
- Executes in the given namespace
- Returns the evaluated value

**Example:**
```python
print(eval("1 + 2"))
```

**Output:**
```text
3
```

**Notes:**
- Executes arbitrary code
- Input must be trusted
- Almost never appropriate in production
- Namespace control does not make it safe
- Evaluating expressions still allows function calls and attribute access.

---

## `exec()`

### Definition
Executes dynamically generated Python code.

### Syntax
```python
exec(source[, globals[, locals]])
```

**Behavior:**
- Accepts statements and blocks
- Executes code with side effects
- Returns `None`

**Example:**
```python
code = "x = 10\nprint(x)"
exec(code)
```

**Output:**
```text
10
```

**Notes:**
- More powerful than `eval`
- Cannot return values directly
- Creates or mutates runtime state
- Extremely difficult to reason about safely

---

## `compile()`

### Definition
Compiles source code into a code object.

### Syntax
```python
compile(source, filename, mode)
```

**Behavior:**
- Produces a code object
- Does not execute code
- `mode` controls allowed syntax

**Example:**
```python
code = compile("1 + 2", "<expr>", "eval")
print(eval(code))
```

**Output:**
```text
3
```

**Notes:**
- Used internally by the interpreter
- Enables separation of compilation and execution
- Common in tooling and REPL implementations

---

## `breakpoint()`

### Definition
Invokes the debugger at the call site.

### Syntax
```python
breakpoint()
```

**Behavior:**
- Delegates to the configured debugger
- Defaults to `pdb`
- Can be globally overridden

**Example:**
```python
x = 10
breakpoint()
print(x)
```

**Output:**
```text
(Pdb)
```

**Notes:**
- Intended for debugging only
- May be disabled in production or optimized runtimes
- Behavior depends on environment configuration

---

## Design Notes
- These functions exist for **runtime control**, not business logic
- They bypass normal code structure and safety
- Readability, predictability, and security suffer
- Use only when no safer alternative exists
- These functions intentionally break normal reasoning guarantees in Python code.

---

## Summary
- `eval` evaluates expressions
- `exec` executes statements
- `compile` produces code objects
- `breakpoint` hooks into debugging tools
- If you are unsure whether you need these functions, you probably do not.

These functions define **Python’s runtime execution surface**, not safe application APIs.