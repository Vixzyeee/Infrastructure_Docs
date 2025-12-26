# Simple Login Decision

This mini project belongs to the **02-control-flow** section.

It is a simple command-line program that checks a username and password against predefined credentials and prints whether the login attempt is successful or not.

---

## Scope

This project intentionally uses only:

- `input()`
- `print()`
- comparison operators
- `if / elif / else`

---

## Program Behavior

The program:

1. Displays a title
2. Asks the user to enter:
   - username  
   - password  
3. Compares both values with stored correct credentials
4. Prints the login result

---

## Login Rules

The program follows these rules:

- if both username and password are correct → login successful  
- if only the username is wrong → show username incorrect message  
- if only the password is wrong → show password incorrect message  
- if both are wrong → show both incorrect message  

Only one message is printed per execution.

---

## Credentials

The correct credentials are stored directly in the program source code, for example:

- username: `admin`  
- password: `12345`  

You may change these values inside the program if needed.

---

## Input Validation

The program assumes normal text input.

There is no exception handling, password masking, or security features.  
This is intentional at this learning stage.

---

## Restrictions

This project does **NOT** use:

- loops
- functions
- lists, tuples, or dictionaries
- modules or imports
- exception handling

---

## Learning Goals

- practice conditional branching
- combine multiple conditions with logical operators
- distinguish between multiple failure cases
- understand simple decision logic for authentication scenarios

---

## Notes

This project focuses on control flow, not real authentication security.
It is for learning purposes only.
