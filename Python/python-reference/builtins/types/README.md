# Python Built-ins Reference

This directory documents **Python built-in objects**.

Built-ins are the objects that are:
- always available
- implicitly available in the global namespace
- fundamental to Python’s execution model

This directory exists to describe **what Python provides by default**, not how to learn Python.

---

## What Are Built-ins

Built-ins are:
- functions
- types
- constants
- internal helpers  
  Objects exposed for interpreter and runtime coordination, not intended as public APIs

that exist in the global namespace without requiring imports.

They form the **baseline environment** every Python program starts with.

---

## What This Directory Is

This directory is:
- a long-term technical reference
- a conceptual map of Python’s core objects
- documentation of language-level primitives

It focuses on:
- definitions
- roles
- semantics
- design intent

---

## What This Directory Is Not

This directory is **not**:
- a tutorial
- a beginner guide
- a syntax explanation
- a replacement for official documentation

It intentionally avoids:
- step-by-step usage
- learning exercises
- opinionated best practices

---

## Built-ins vs Standard Library

Built-ins:
- are always present
- require no imports
- are implemented directly by the interpreter

Standard library modules:
- must be imported
- provide higher-level abstractions
- build on top of built-ins

Example:
- `len` is a built-in
- `math.sqrt` is a library function

This separation is fundamental.

---

## Built-ins vs Methods

Built-ins:
- operate **across objects**
- exist independently of any specific type

Methods:
- are behaviors **attached to a type**
- require an object to exist

Example:
- `len(x)` is a built-in function
- `x.append()` is a method

Methods are documented separately under `methods/`.

---

## Directory Structure

Built-ins are grouped by **conceptual role**, not alphabetically.

```text
builtins/
├── README.md
├── constants.md # Global built-in objects
├── introspection.md # Runtime inspection helpers
├── internals.md # Interpreter-level internals
├── functions/ # Cross-type operations
│ ├── numeric.md
│ ├── iteration.md
│ ├── ordering.md
│ ├── representation.md
│ ├── object_model.md
│ ├── io.md
│ ├── runtime.md
│ └── environment.md
└── types/ # Language primitives
├── numeric.md
├── sequence.md
├── set_mapping.md
├── text_binary.md
└── object_model.md
```

Each file documents **one conceptual category**, not a raw symbol list.

---

## Relationship to Other Directories

This directory deliberately does not overlap with:

- `exceptions/`  
  Exception classes are built-in types, but their behavior and hierarchy
  are documented separately.

- `methods/`  
  Methods describe behavior bound to types, not global objects.

- `keywords/`  
  Keywords define syntax, not runtime objects.

- `operators/`  
  Operators define evaluation rules, not callable objects.

Each directory exists to keep concerns separated.

---

## Design Principles

This reference follows strict rules:

- Concepts over syntax
- Semantics over examples
- Minimal examples only
- No duplication across directories

If a concept belongs elsewhere, it is not documented here.

---

## Intended Audience

This directory is written for:
- developers who already use Python
- readers seeking deeper language understanding
- long-term reference usage

It assumes familiarity with Python syntax.

---

## Summary

- Built-ins define Python’s baseline environment
- They are always present and interpreter-backed
- This directory documents their roles and semantics
- Understanding built-ins explains why Python behaves the way it does

This directory defines **Python’s built-in object surface**, not how to program in Python.