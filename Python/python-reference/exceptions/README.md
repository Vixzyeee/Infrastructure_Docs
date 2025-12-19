# Python Exceptions & Warnings Reference

This repository is a **structured, long-term reference** for Python exceptions and warnings.

It focuses on:
- Understanding **why** exceptions exist
- Knowing **when to catch** vs **when to fail**
- Differentiating **bugs**, **environment failures**, and **control-flow signals**

This is **not a tutorial** and **not beginner material**.  
It is designed as a **technical reference** for real-world Python development.

---

## Scope

This repository documents:

- Exception hierarchy and fundamentals
- Common exception categories and their intent
- Runtime vs syntax vs logic failures
- OS, I/O, Unicode, and arithmetic errors
- Python warnings and warning control

Each file focuses on **one conceptual category**, not individual trivia.

---

## Structure Overview

```text
exceptions/
├── fundamentals.md        # BaseException, Exception, control-flow exceptions
├── logic_errors.md        # Programming mistakes (TypeError, ValueError, etc.)
├── syntax_errors.md       # Syntax, indentation, and parsing failures
├── arithmetic_errors.md   # Numeric and mathematical failures
├── os_io_errors.md        # Filesystem, OS, and network-related errors
├── runtime_errors.md      # Execution-time and system-level failures
├── unicode_errors.md      # Encoding and decoding failures
├── warnings.md            # Non-fatal runtime signals
└── README.md              # This file
```

---

## Design Principles

### 1. Conceptual Grouping
Exceptions are grouped by **cause and intent**, not alphabetically.

Why?
- Alphabetical lists are useless for reasoning
- Real systems fail by category, not by name

---

### 2. Correct Catching Philosophy
This repository emphasizes:

- Catch **specific exceptions**
- Avoid catching `BaseException`
- Let control-flow exceptions propagate
- Fail fast on unrecoverable states

---

### 3. Honest Examples
Examples are:
- Minimal
- Representative
- Not misleading

Outputs are illustrative, not guaranteed byte-for-byte across platforms.

---

### 4. Production-Oriented
Content reflects:
- Server environments
- CI/CD realities
- Long-running processes
- Defensive programming practices

No toy examples. No magic thinking.

---

## What This Repo Is NOT

- ❌ A Python crash course  
- ❌ A try/except cookbook  
- ❌ A list of errors to memorize  
- ❌ Beginner-friendly walkthrough  

If you are looking for “how to fix error X”, this is not that.

---

## Intended Audience

This repository is for:
- Backend engineers
- DevOps / SRE
- Systems programmers
- Anyone maintaining Python in production

If you care about **failure modes**, this repo is for you.

---

## Usage Recommendation

- Read `fundamentals.md` first
- Then read categories based on failure type
- Use this repo as a **reference**, not linear reading

---

## Final Note

Exceptions and warnings are **signals**, not annoyances.

If you ignore them:
- Bugs accumulate
- Systems rot
- Failures become mysterious

This repository exists to prevent that.

---