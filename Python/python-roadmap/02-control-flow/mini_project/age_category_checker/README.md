# Number Calculator

This mini project belongs to the **02-control-flow** section.

It is a simple command-line program that asks for a user’s age and determines the corresponding age category using conditional statements.

---

## Scope

This project intentionally uses only:

- variables
- `input()`
- `print()`
- explicit type conversion (`int`)
- conditional statements:
  - `if`
  - `elif`
  - `else`

---

## Restrictions

This project does **NOT** use:

- loops (`for`, `while`)
- functions
- lists, tuples, or dictionaries
- external modules or imports
- advanced validation or exception handling

Any limitations are intentional and match the learning goals of the **02-control-flow** stage.

---

## Program Behavior

The program:

1. Displays a title
2. Asks the user to input:
   - name
   - age
3. Converts the age to an integer
4. Decides the user’s age category using conditional branching
5. Prints the final result in a simple formatted output

The age categories commonly used:
- Age < 0 → Invalid age
- 0–12 → Child
- 13–17 → Teenager
- 18–59 → Adult
- 60+ → Senior

---

## Learning Goals

- Understand how `if / elif / else` control program flow
- Practice comparison operators (`<`, `>=`)
- See how branching changes program behavior
- Combine user input with decision making
- Strengthen mental model of top-to-bottom execution with conditional jumps

---

## Notes

This project focuses on **decision making**, not robustness.  
If the user enters non-numeric age input, the program may crash. That is acceptable at this stage.
