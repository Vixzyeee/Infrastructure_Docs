# Scope and Namespace Keywords

## What is this?
Scope and namespace keywords are used to control how variables are bound, accessed, and removed within different scopes.

---

## global
**Purpose:** Declare that a variable refers to the global scope.

```python
x = 10

def update():
    global x
    x = 20

update()
print(x)
```

**Output:**

```text
20
```

**Notes:**

- Allows modification of global variables inside a function
- Refers to the module-level scope

---

## nonlocal
**Purpose:** Declare that a variable refers to an enclosing (non-global) scope.

```python
def outer():
    x = 10

    def inner():
        nonlocal x
        x = 20

    inner()
    return x

print(outer())
```

**Output:**

```text
20
```

**Notes:**

- Used in nested functions
- Refers to the nearest enclosing scope that is not global

---

## del
**Purpose:** Remove a variable binding or object reference.

```python
x = 10
del x
```

**Output:**

```text
(no output)
```

**Notes:**

- Removes the name binding from the current namespace
- Does not necessarily delete the object from memory

---
