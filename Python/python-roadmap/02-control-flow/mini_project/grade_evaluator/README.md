# Grade Evaluator

This mini project belongs to the **02-control-flow** section.

It is a simple command-line program that reads an exam score and outputs the corresponding letter grade based on predefined ranges.

---

## Scope

This project intentionally uses only:

- `input()`
- `print()`
- `int()`
- `if / elif / else`

---

## Program Behavior

The program:

1. Displays a title
2. Asks the user to input an exam score (0–100)
3. Converts the input into an integer
4. Checks whether the score is valid
5. Outputs the appropriate letter grade

---

## Grading Rules

The program uses the following grading scale:

- 90–100 → A  
- 80–89 → B  
- 70–79 → C  
- 60–69 → D  
- 0–59 → F  

---

## Input Validation

The program treats the score as **invalid** when:

- it is less than 0  
- it is greater than 100  

In this case, the program prints an invalid score message.

No exception handling is used. If non-numeric input is entered, the program may crash. This is acceptable for this stage.

---

## Restrictions

This project does **NOT** use:

- loops
- functions
- lists, tuples, or dictionaries
- modules or imports
- exception handling (`try/except`)

All limitations are intentional and match the learning goals for **02-control-flow**.

---

## Learning Goals

- Practice conditional branching using `if / elif / else`
- Handle mutually exclusive conditions
- Separate valid and invalid input cases
- Strengthen understanding of comparison operators and logical expressions

---

## Notes

This project focuses on decision-making logic rather than robustness.  
The goal is clarity of control flow, not production-level validation.
