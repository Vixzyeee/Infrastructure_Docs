# Interpreter Internals Built-in Objects

This file documents **built-in objects that exist primarily for the Python interpreter itself**.

These objects are:
- exposed in the global namespace
- required for interpreter operation
- **not public APIs**

They exist for correctness and bootstrapping, not for application use.

---

## Scope

Covered in this file:
- `__import__`
- `__build_class__`
- `__debug__`
- `__name__`
- `__spec__`
- `_` (underscore binding)

Not covered:
- importlib internals
- compiler implementation
- bytecode execution
- CPython-specific internals

---

## Important Warning

Objects documented here:
- may change behavior across versions
- are not guaranteed stable
- should not be relied upon in user code

If you are using these directly, you are likely:
- writing tooling
- reimplementing language features
- or doing something that deserves scrutiny

In normal application code, their appearance is usually a design smell.

---

## `__import__`

### Definition
Low-level import mechanism used by the interpreter.

### Role
- Implements the `import` statement
- Dispatches module loading
- Returns module objects

**Example:**
```python
math = __import__("math")
print(math.sqrt(4))
```

**Output:**
```text
2.0
```

**Notes:**
- Called implicitly by `import`
- Direct usage is discouraged in favor of `importlib`
- `importlib` provides the supported API

---

## `__build_class__`

### Definition
Internal helper used to construct classes.

### Role
- Invoked during class definition
- Coordinates class body execution
- Integrates metaclass logic

**Example:**
```python
print(__build_class__)
```

**Output:**
```text
<built-in function __build_class__>
```

**Notes:**
- Used by the compiler
- Not intended for direct invocation
- Central to class creation semantics

---

## `__debug__`

### Definition
Boolean flag indicating debug mode.

### Role
- Controls assertion behavior
- Evaluated at compile time

**Example:**
```python
print(__debug__)
```

**Output:**
```text
True
```

**Notes:**
- False only when Python runs with `-O`
- Cannot be reassigned
- Used by the compiler, not runtime logic

---

## `__name__`

### Definition
Identifier of the current module.

### Role
- Distinguishes main execution from import
- Provides module identity

**Example:**
```python
print(__name__)
```

**Output:**
```text
__main__
```

**Notes:**
- Set automatically by the interpreter
- Used in execution guards
- Always a string

---

## `__spec__`

### Definition
Holds import-related metadata for a module.

### Role
- Describes how a module was loaded
- Used by the import system

**Example:**
```python
print(__spec__)
```

**Output:**
```text
ModuleSpec(name='__main__', ...)
```

**Notes:**
- Primarily for import machinery
- May be `None` in interactive contexts
- Not a stable public interface

---

## `_` (underscore binding)

### Definition
Conventionally bound to the last evaluated expression in interactive mode.

### Role
- REPL convenience
- Temporary value access

**Example:**
```python
1 + 2
print(_)
```

**Output:**
```text
3
```

**Notes:**
- Exists only in interactive environments
- Overwritten frequently
- Not guaranteed outside REPL usage
- Shadowed easily by user assignments

---

## Design Notes
- These objects exist to support language execution
- Exposure does not imply endorsement
- Stability is not guaranteed
- Direct usage couples code to interpreter behavior

---

## Summary
- Internal built-ins support the interpreter itself
- They are not public APIs
- Usage outside tooling is discouraged
- Understanding their existence explains Python’s execution model

This file documents **Python’s exposed interpreter internals**, not supported extension points.