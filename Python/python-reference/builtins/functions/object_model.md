# Object Model Built-in Functions

This file documents **built-in functions that interact directly with Python’s object model**.

These functions expose mechanisms for:
- attribute access
- method binding
- class construction
- inheritance resolution

They operate at the **runtime object layer**, not at the syntax level.

---

## Scope

Covered in this file:
- `getattr`
- `setattr`
- `delattr`
- `property`
- `super`
- `classmethod`
- `staticmethod`

Not covered:
- attribute access syntax (`obj.attr`)
- class definition syntax
- descriptor protocol details
- metaclass customization

---

## Object Model Context

In Python:
- Everything is an object
- Attribute access is dynamic
- Classes are runtime objects, not compile-time constructs

These built-ins exist to expose and control that behavior explicitly.

---

## `getattr()`

### Definition
Retrieves an attribute value from an object by name.

### Syntax
```python
getattr(obj, name[, default])
```

**Behavior:**
- Semantically equivalent to `obj.name` access
- Resolves attributes dynamically at runtime
- Returns `default` if provided and attribute is missing

**Example:**
```python
class User:
    name = "admin"

print(getattr(User, "name"))
print(getattr(User, "age", None))
```

**Output:**
```text
admin
None
```

**Notes:**
- Attribute lookup follows the full resolution chain
- Commonly used for dynamic access
- Avoid when static access is sufficient

---

## `setattr()`

### Definition
Sets an attribute on an object dynamically.

### Syntax
```python
setattr(obj, name, value)
```

**Behavior:**
- Equivalent to `obj.name = value`
- Creates the attribute if it does not exist
- Triggers descriptor logic if applicable

**Example:**
```python
class User:
    pass

u = User()
setattr(u, "role", "admin")
print(u.role)
```

**Output:**
```text
admin
```

**Notes:**
- Mutates object state
- Can bypass expected attribute constraints
- Use with care in public APIs
- Can bypass `__init__`-level invariants

---

## `delattr()`

### Definition
Deletes an attribute from an object.

### Syntax
```python
delattr(obj, name)
```

**Behavior:**
- Equivalent to `del obj.name`
- Removes attribute from the object namespace

**Example:**
```python
class User:
    role = "admin"

delattr(User, "role")
print(hasattr(User, "role"))
```

**Output:**
```text
False
```

**Notes:**
- Raises `AttributeError` if attribute does not exist
- Can break invariants if misused

---

## `property()`

### Definition
Creates a managed attribute with getter, setter, and deleter hooks.

### Syntax
```python
property(fget=None, fset=None, fdel=None, doc=None)
```

**Behavior:**
- Implements the descriptor protocol
- Allows method access via attribute syntax
- Executes logic on access or assignment

**Example:**
```python
class User:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    name = property(get_name)

u = User("admin")
print(u.name)
```

**Output:**
```text
admin
```

**Notes:**
- Bridges attribute access and method execution
- Prefer over manual getter methods
- Adds indirection at access time

---

## `super()`

### Definition
Returns a proxy for delegating method calls to a parent class.

### Syntax
```python
super()
super(type, obj)
```

**Behavior:**
- Resolves methods using method resolution order (MRO)
- Works only within class hierarchies
- Requires cooperative multiple inheritance

**Example:**
```python
class Base:
    def greet(self):
        return "base"

class Child(Base):
    def greet(self):
        return super().greet()

print(Child().greet())
```

**Output:**
```text
base
```

**Notes:**
- Not a reference to a specific parent
- Depends on runtime MRO, not lexical structure
- Misuse leads to subtle bugs

---

## `classmethod()`

### Definition
Defines a method bound to the class, not the instance.

### Syntax
```python
classmethod(function)
```

**Behavior:**
- Receives the class as the first argument
- Can be called on class or instance
- Shared across all instances

**Example:**
```python
class User:
    role = "admin"

    @classmethod
    def get_role(cls):
        return cls.role

print(User.get_role())
```

**Output:**
```text
admin
```

**Notes:**
- Operates at the class level
- Often used for alternative constructors
- Does not access instance state directly
- Unlike `staticmethod`, this participates in inheritance

---

## `staticmethod()`

### Definition
Defines a method without implicit instance or class binding.

### Syntax
```python
staticmethod(function)
```

**Behavior:**
- Behaves like a plain function
- Lives in the class namespace
- Does not receive `self` or `cls`

**Example:**
```python
class Math:
    @staticmethod
    def add(a, b):
        return a + b

print(Math.add(2, 3))
```

**Output:**
```text
5
```

**Notes:**
- Namespaced utility function
- No access to class or instance state
- Often overused
- Unlike `classmethod`, this does not receive dynamic class context

---

## Design Notes
- These built-ins expose Python’s dynamic object system
- Attribute access and binding are runtime operations
- Power comes with complexity and risk
- Explicit usage should be deliberate

## Summary
- Attribute access can be controlled dynamically
- `property` integrates behavior into attribute syntax
- `super` relies on cooperative inheritance
- Method binding affects how functions receive context
- These primitives expose Python’s object mechanics directly and should be used to control behavior, not to replace normal attribute syntax.

This file defines **Python’s object model primitives**, not object-oriented design patterns.