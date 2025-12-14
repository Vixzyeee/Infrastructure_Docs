# Test Structure

This document describes a simple and practical test structure for Python projects.

## Basic Rules

- Tests should be separated from application code
- One test file per module
- Test names should describe behavior, not implementation

## Example Structure

```text
project/
├── app/
│   ├── calculator.py
│   └── user.py
└── tests/
    ├── test_calculator.py
    └── test_user.py
