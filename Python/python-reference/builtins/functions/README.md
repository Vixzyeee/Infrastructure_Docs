# Built-in Types

This directory documents **Python’s built-in types as language primitives**.

Built-in types define:
- how values are represented conceptually in memory
- how objects behave at runtime
- which operations are fundamentally supported by the language

This directory focuses on **what these types are**, not how to use them.

---

## What Are Built-in Types

Built-in types are:
- always available
- implemented by the interpreter
- fundamental to Python’s execution model

They are not libraries and not optional abstractions.
They form the **core object universe** of Python.

---

## Types vs Methods

This directory documents **types**, not their methods.

- A *type* defines structure, identity, and behavior contracts
- A *method* is behavior attached to a specific type

Methods are documented separately under `methods/` to avoid:
- repetition
- mixing structure with behavior
- bloated type documentation

---

## Types vs Built-in Functions

- Built-in functions **operate on objects**
- Built-in types **define what objects are**

Example:
- `len()` is a built-in function
- `list` is a built-in type that defines how length works

This separation is intentional.

---

## Design Philosophy

Built-in types are:
- minimal
- composable
- protocol-driven

Most advanced behavior emerges from:
- method composition
- protocol participation
- interoperability between types

Not from deep inheritance trees.

---

## Directory Structure

This directory groups built-in types by **conceptual role**, not inheritance.  
Files are ordered from concrete data types to abstract object model concepts.

```text
types/
├── numeric.md # Numeric primitives and truth values
├── sequence.md # Ordered, indexable collections
├── set_mapping.md # Unordered collections and key-value mappings
├── text_binary.md # Text and binary data representations
└── object_model.md # Root object model types
```

Each file documents:
- the role of the types
- their conceptual behavior
- how they fit into the language model

---

## Scope Rules

This directory:
- does NOT document methods
- does NOT explain syntax
- does NOT provide usage tutorials

Each type description includes:
- definition
- role in the language
- minimal examples
- critical semantic notes

---

## Relationship to Other Directories

- `methods/`  
  Documents behavior attached to types.

- `functions/`  
  Documents operations that act across types.

- `exceptions/`  
  Documents error signaling via exception objects.

- `keywords/`  
  Documents syntax-level constructs, not objects.

Each directory serves a distinct purpose.

---

## Intended Audience

This directory is written for:
- developers who already write Python
- readers who want to understand *why* Python behaves as it does
- long-term reference usage

It is not beginner material.

---

## Summary

- Built-in types are Python’s core primitives
- They define structure, identity, and behavior
- This directory documents types as concepts, not as APIs
- Understanding these types explains most Python behavior
- Most Python behavior becomes predictable once these types are understood

This directory defines **Python’s foundational object types**, not programming patterns.