# Python Built-ins Reference

This directory documents **Python built-in objects**.

Built-ins are objects that:
- are always available
- exist in the global namespace
- are provided directly by the interpreter

They define Python’s **baseline execution environment**.

This directory focuses on **what Python provides by default**, not how to write Python code.

---

## What Are Built-ins

Built-ins include:
- functions
- types
- constant objects
- interpreter-level helpers

They are:
- loaded automatically
- accessible without `import`
- fundamental to language semantics

Every Python program starts with these objects already present.

---

## What This Directory Is

This directory is a **long-term technical reference**.

It documents:
- definitions
- conceptual roles
- runtime semantics
- design intent

It is written to be:
- stable across time
- readable without surrounding context
- useful as a refresher months or years later

---

## What This Directory Is Not

This directory is **not**:
- a tutorial
- a beginner guide
- a step-by-step explanation
- a replacement for official documentation

It intentionally avoids:
- learning exercises
- syntax walkthroughs
- “how to use” patterns
- opinionated best practices

If you are learning Python, this is **not** the right entry point.

---

## Built-ins vs Standard Library

Built-ins:
- are always present
- require no imports
- are implemented by the interpreter itself

Standard library modules:
- must be imported
- provide higher-level abstractions
- are layered on top of built-ins

Example:
- `len` is a built-in function
- `math.sqrt` is a standard library function

This separation is fundamental to Python’s design.

---

## Built-ins vs Methods

Built-ins:
- operate across objects
- exist independently of any specific type

Methods:
- are behaviors attached to a type
- require an object instance or class

Example:
- `len(x)` is a built-in function
- `x.append()` is a method of `list`

This distinction separates operations from capabilities.

Methods are documented separately under `methods/`.

---

## Built-ins vs Keywords and Operators

Built-ins are **runtime objects**.

Keywords:
- define syntax
- are handled by the compiler
- are not objects

Operators:
- define evaluation rules
- may map to special methods
- are not callable objects

These concepts are documented separately under:
- `keywords/`
- `operators/`

---

## Directory Structure

Built-ins are grouped by **conceptual role**, not alphabetically.

```text
builtins/
├── README.md # This document
├── constants.md # Global constant objects
├── introspection.md # Runtime inspection helpers
├── internals.md # Interpreter-level internals
├── functions/ # Cross-type operations
│ ├── README.md
│ ├── numeric.md
│ ├── iteration.md
│ ├── ordering.md
│ ├── representation.md
│ ├── object_model.md
│ ├── io.md
│ ├── runtime.md
│ └── environment.md
└── types/ # Language primitives
├── README.md
├── numeric.md
├── sequence.md
├── set_mapping.md
├── text_binary.md
└── object_model.md
```

Each file documents **one conceptual domain**, not a raw symbol list.

---

## constants.md

Documents **singleton built-in objects** that encode language-level meaning.

Includes:
- `None`
- `True`
- `False`
- `NotImplemented`
- `Ellipsis`

Focus:
- identity
- semantics
- correct usage
- common misuse

These are objects, not keywords.

---

## introspection.md

Documents built-ins used to **inspect runtime state**.

Includes:
- type inspection
- namespace inspection
- attribute discovery
- inheritance checks

These tools are:
- observational
- non-transformational
- primarily for diagnostics and tooling

---

## internals.md

Documents **interpreter-facing built-ins**.

Includes:
- low-level helpers
- execution metadata
- REPL bindings

These objects:
- are not public APIs
- may change across versions
- should not appear in application code

This file is intentionally defensive.

---

## functions/

Documents **built-in functions** that operate across types.

These functions:
- are protocol-driven
- are type-agnostic
- expose core language behavior

They expose behavior that is meaningful across multiple types.

Each file groups functions by **semantic domain**, such as:
- numeric operations
- iteration mechanics
- ordering and aggregation
- representation and conversion
- object model interaction
- I/O primitives
- runtime execution
- interactive environment helpers

---

## types/

Documents **built-in types as language primitives**.

These types:
- define object behavior
- participate in protocols
- form Python’s core object universe

They define structure and identity before any behavior is applied.

This directory focuses on:
- conceptual role
- semantic behavior
- interaction with the language model

Methods are intentionally documented elsewhere.

---

## Design Principles

This directory follows strict rules:

- Concepts over syntax
- Semantics over usage
- Minimal examples only
- No overlap with other domains
- No duplication across directories

If a topic belongs elsewhere, it is not documented here.

---

## Intended Audience

This directory is written for:
- developers already familiar with Python
- readers seeking deeper language understanding
- long-term reference usage

It assumes:
- knowledge of Python syntax
- familiarity with basic programming concepts

---

## Summary

- Built-ins define Python’s baseline environment
- They are always present and interpreter-backed
- This directory documents their roles and semantics
- Understanding built-ins explains most Python behavior
- This directory is meant to be read slowly, revisited often, and rarely modified

This directory defines **Python’s built-in object surface**, not how to program in Python.