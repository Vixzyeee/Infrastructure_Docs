# Runtime Introspection Built-in Functions

This file documents **built-in functions used for runtime inspection and introspection**.

These functions allow programs and developers to:
- examine objects
- inspect namespaces
- query runtime properties

They do **not** modify program behavior.
They reveal it.

---

## Scope

Covered in this file:
- `type`
- `id`
- `dir`
- `vars`
- `globals`
- `locals`
- `callable`
- `hasattr`
- `hash`
- `help`
- `isinstance`
- `issubclass`

Not covered:
- debugging tools
- reflection libraries
- static analysis
- metaprogramming patterns

---

## Introspection Context

Introspection operates at runtime and answers questions like:
- What is this object?
- What attributes exist?
- What namespace am I in?

These functions are **observational**, not transformational.

---

## `type()`

### Definition
Returns the type of an object.

### Syntax
```python
type(obj)
```

**Behavior:**
- Returns the object’s class
- Works for all objects

**Example:**
```python
print(type(10))
```

**Output:**
```text
<class 'int'>
```

**Notes:**
- Central to Python’s object model
- Distinct from `isinstance` checks
- Prefer isinstance for behavior checks, not type equality

---

## `id()`

### Definition
Returns the identity of an object.

### Syntax
```python
id(obj)
```

**Behavior:**
- Unique for the object’s lifetime
- Implementation-dependent meaning

**Example:**
```python
x = []
print(id(x))
```

**Output:**
```text
(an implementation-dependent integer)
```

**Notes:**
- Often corresponds to memory address
- Only meaningful for identity comparison

---

## `dir()`

### Definition
Returns a list of attribute names.

### Syntax
```python
dir(obj)
```

**Behavior:**
- Lists attributes available on the object
- Includes inherited attributes

**Example:**
```python
print(dir([]))
```

**Output:**
```text
['__add__', '__class__', '__contains__', ...]
```

**Notes:**
- Intended for exploration
- Output is not guaranteed stable
- Not intended for program logic

---

## `vars()`

### Definition
Returns the `__dict__` of an object.

### Syntax
```python
vars(obj)
```

**Behavior:**
- Exposes the object’s attribute dictionary
- Raises `TypeError` if unavailable

**Example:**
```python
class User:
    def __init__(self):
        self.name = "admin"

u = User()
print(vars(u))
```

**Output:**
```text
{'name': 'admin'}
```

**Notes:**
- Mutating the result mutates the object
- Not all objects have a `__dict__`

---

## `globals()`

### Definition
Returns the global namespace dictionary.

### Syntax
```python
globals()
```

**Behavior:**
- Reflects the current module’s globals
- Modifications affect global scope

**Example:**
```python
x = 10
print(globals()["x"])
```

**Output:**
```text
10
```

**Notes:**
- Highly context-dependent
- Use cautiously outside tooling
- These functions expose namespaces, not APIs

---

## `locals()`

### Definition
Returns the local namespace dictionary.

### Syntax
```python
locals()
```

**Behavior:**
- Reflects the current local scope
- Write behavior is implementation-dependent

**Example:**
```python
def f():
    y = 20
    print(locals())

f()
```

**Output:**
```text
{'y': 20}
```

**Notes:**
- Reading is reliable
- Writing is not guaranteed to affect locals
- These functions expose namespaces, not APIs

---

## `callable()`

### Definition
Checks whether an object can be called.

### Syntax
```python
callable(obj)
```

**Behavior:**
- Returns `True` if object implements call semantics

**Example:**
```python
print(callable(len))
print(callable(10))
```

**Output:**
```text
True
False
```

**Notes:**
- Does not guarantee correct call signature
- Used for capability checks

---

## `hasattr()`

### Definition
Checks whether an object has a named attribute.

### Syntax
```python
hasattr(obj, name)
```

**Behavior:**
- Returns `True` or `False`
- Suppresses `AttributeError`

**Example:**
```python
print(hasattr([], "append"))
```

**Output:**
```text
True
```

**Notes:**
- Internally calls `getattr`
- Can hide unexpected errors
- Including exceptions raised during attribute access

---

## `hash()`

### Definition
Returns the hash value of an object.

### Syntax
```python
hash(obj)
```

**Behavior:**
- Used in hash-based collections
- Must be consistent with equality

**Example:**
```python
print(hash("python"))
```

**Output:**
```text
<integer>
```

**Notes:**
- Immutable objects are typically hashable
- Mutable objects usually are not

---

## `help()`

### Definition
Displays help information for an object.

### Syntax
```python
help(obj)
```

**Behavior:**
- Launches interactive help viewer
- Extracts docstrings and metadata

**Example:**
```python
help(len)
```

**Output:**
```text
Help on built-in function len...
```

**Notes:**
- Interactive by design
- Not suitable for automated workflows

---

## `isinstance()`

### Definition
Checks whether an object is an instance of a type.

### Syntax
```python
isinstance(obj, type_or_tuple)
```

**Behavior:**
- Supports inheritance
- Accepts multiple types

**Example:**
```python
print(isinstance(10, int))
```

**Output:**
```text
True
```

**Notes:**
- Preferred over direct type comparison
- Supports polymorphism

---

## `issubclass()`

### Definition
Checks whether a class is a subclass of another.

### Syntax
```python
issubclass(cls, type_or_tuple)
```

**Behavior:**
- Evaluates inheritance relationships
- Accepts multiple types

**Example:**
```python
print(issubclass(bool, int))
```

**Output:**
```text
True
```

**Notes:**
- Operates on classes, not instances
- Central to type hierarchy inspection

---

## Design Notes
- Introspection tools observe runtime state
- They do not guarantee stability across implementations
- Excessive use can obscure program structure
- Best suited for tooling and diagnostics
- Introspection favors transparency over abstraction

---

## Summary
- Introspection reveals object and runtime properties
- These built-ins are observational tools
- Correct usage avoids side effects
- Clarity beats clever inspection
- Introspection is a diagnostic tool, not a design strategy

This file defines **Python’s runtime introspection surface**, not reflection frameworks.