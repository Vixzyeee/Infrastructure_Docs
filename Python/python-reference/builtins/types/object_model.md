# Object Model Types

This file documents **the foundational object model types** in Python.

These types define:
- what an object is
- how objects are created
- how types relate to each other

Everything in Python is built on these concepts.

---

## Scope

Covered in this file:
- `object`
- `type`

Not covered:
- class syntax
- metaclass customization
- descriptor protocol
- inheritance patterns

---

## Object Model Overview

Python is a **fully object-oriented language** in the sense that:
- every value is an object
- every object has a type
- types themselves are objects

This model is uniform and recursive.

---

## `object`

### Definition
The base class of all Python objects.

### Role
- Provides fundamental object behavior
- Defines identity and basic attribute access
- Serves as the root of the inheritance hierarchy

**Example:**
```python
x = 10
print(isinstance(x, object))
```

**Output:**

```text
True
```

**Notes:**
- Every object implicitly inherits from `object`
- Provides default implementations for **identity, comparison, and attribute access**
- Rarely instantiated directly

---

## `type`

### Definition
The type of all classes.

### Role
- Creates classes
- Defines class behavior
- Acts as Python’s default metaclass

**Example:**
```python
class User:
    pass

print(type(User))
print(type(type))
```

**Output:**
```text
<class 'type'>
<class 'type'>
```

**Notes:**
- Classes are instances of `type`
- `type` is self-referential
- Custom metaclasses extend `type`
- Misuse of `type` usually indicates metaprogramming, not normal class design

---

## Object Creation Flow

Conceptually:
1. `type` constructs a class
2. The class acts as a callable
3. Calling the class creates an instance
4. The instance is an `object`
5. This flow is conceptual, not a literal execution trace

**Example:**
```python
class User:
    pass

u = User()
print(type(u))
```

**Output:**
```text
<class '__main__.User'>
```

---

## Identity vs Type

Two core concepts:
- **Identity**: what object this is
- **Type**: what kind of object this is

**Example:**
```python
a = []
b = []

print(a is b)
print(type(a) is type(b))
```

**Output:**
```text
False
True
```

**Notes:**
- Identity is unique per object
- Type defines behavior and structure
- Confusing the two leads to subtle bugs

---

## Dynamic Nature of Types

In Python:
- types exist at runtime
- classes can be created dynamically
- behavior can be modified after creation

**Example:**
```python
User = type("User", (), {})
print(User)
```

**Output:**
```text
<class '__main__.User'>
```

---

## Design Notes
- Python’s object model is minimal but powerful
- Uniformity enables introspection and metaprogramming
- Flexibility trades compile-time guarantees for runtime control
- Most complexity emerges from composition, not inheritance

---

## Summary
- `object` is the root of all objects
- `type` is the root of all classes
- Types are objects
- Python’s object model is consistent and recursive
- Understanding object and type explains most of Python’s dynamic behavior

This file defines **Python’s core object model**, not object-oriented techniques.