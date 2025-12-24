> This file documents predicted behavior and mental models.  
> Code snippets are intentionally not executed.  
> Running the corresponding `.py` files will execute all cases sequentially.

# Answers – 01-basics

---

## if_else.py – Case 1: Basic `if` statement

### Question  
DO NOT RUN.

```python
x = 10

if x > 5:
    print("x is greater than 5")

print("End of Case 1")
```

### Predicted Output
```text
x is greater than 5
End of Case 1
```

### Answer

**Output:**
```text
x is greater than 5
End of Case 1
```

The expression `x > 5` evaluates to the boolean object `True`, so the `if` block is executed.  
After the `if` block finishes, execution continues normally.

### Sequence of Events (Mental Model)

1. The object `10` is created and the name `x` is bound to it
2. The expression `x > 5` is evaluated
3. The comparison produces a boolean object `True`
4. The `if` statement checks the truth value of that boolean
5. Because the condition is `True`, the indented block is executed
6. Execution continues after the `if` block
7. `"End of Case 1"` is printed unconditionally

## Conclusion

An `if` statement in Python:
- evaluates a **boolean expression**
- executes its block **only if the expression is truthy**
- does **not** interrupt normal execution flow

Control flow is determined by **condition evaluation**, not by variable type or syntax alone.

---

## if_else.py – Case 2: `if–else` branching

### Question
DO NOT RUN.

```python
x = 3

if x > 5:
    print("x is greater than 5")
else:
    print("x is less than or equal to 5")

print("End of Case 2")
```

### Predicted Output
```text
x is less than or equal to 5
End of Case 2
```

### Answer

**Output:**
```text
x is less than or equal to 5
End of Case 2
```

The condition `x > 5` evaluates to `False`, so the `if` block is skipped and the `else` block is executed instead.  
Execution then continues normally after the conditional structure.

### Sequence of Events (Mental Model)

1. The object `3` is created and the name `x` is bound to it
2. The expression `x > 5` is evaluated
3. The comparison produces the boolean object `False`
4. The `if` statement checks the truth value of the condition
5. Because the condition is `False`, the `if` block is skipped
6. The `else` block is executed
7. Execution continues after the `if–else` structure
8. `"End of Case 2"` is printed unconditionally

## Conclusion

An `if–else` statement in Python:
- evaluates **one condition**
- executes **exactly one branch**
- guarantees a fallback path when the condition is false

Only one branch is ever executed.  
There is no “partial execution” and no re-evaluation after a branch is chosen.

---

## if_else.py – Case 3: if–elif–else chain

### Question 
DO NOT RUN.

```python
score = 75

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
else:
    print("Grade D")

print("End of Case 3")
```

### Predicted Output
```text
Grade C
End of Case 3
```

### Answer

**Output:**
```text
Grade C
End of Case 3
```

The conditions are evaluated **top to bottom**.  
The first condition that evaluates to `True` determines the executed branch.
All remaining branches are skipped.

### Sequence of Events (Mental Model)

1. The object `75` is created and the name `score` is bound to it
2. The expression `score >= 90` is evaluated → `False`
3. The expression `score >= 80` is evaluated → `False`
4. The expression `score >= 70` is evaluated → `True`
5. The corresponding `elif` block is executed
6. All remaining branches (`else`) are skipped
7. Execution continues after the `if–elif–else` chain
8. `"End of Case 3"` is printed unconditionally

## Conclusion

An `if–elif–else` chain in Python:
- evaluates conditions **sequentially**
- executes **only the first truthy branch**
- skips all remaining branches once a match is found

**Order matters**.
A broader condition placed earlier can make later branches unreachable.

---

## if_else.py – Case 4: Order matters in conditions

### Question 
DO NOT RUN.

```python
value = 10

if value > 0:
    print("Positive number")
# The elif branch is never reached due to condition order
elif value > 5:
    print("Greater than 5")

print("End of Case 4")
```

### Predicted Output
```text
Positive number
End of Case 4
```

### Answer

**Output:**
```text
Positive number
End of Case 4
```

Although `value > 5` is also `True`, it is **never evaluated** because the first condition already matches.  
Once a truthy branch is executed, the remaining branches in the chain are skipped.

### Sequence of Events (Mental Model)

1. The object `10` is created and the name `value` is bound to it
2. The expression `value > 0` is evaluated → `True`
3. The corresponding `if` block is executed
4. The `elif` condition is not evaluated at all
5. Execution continues after the `if–elif` structure
6. `"End of Case 4"` is printed unconditionally

## Conclusion

In an `if–elif` chain:
- conditions are evaluated **in order**
- evaluation **stops at the first truthy condition**
- later conditions may be **logically true but unreachable**

Correct syntax does not guarantee correct logic.  
Condition order is part of program behavior.

---

## if_else.py – Case 5: Nested `if` statements

### Question 
DO NOT RUN.

```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Allowed to enter")
    else:
        print("ID required")
else:
    print("Underage")

print("End of Case 5")
```

### Predicted Output
```text
Allowed to enter
End of Case 5
```

### Answer

**Output:**
```text
Allowed to enter
End of Case 5
```

The outer condition checks the age requirement first.  
Only if that condition is satisfied does the inner `if` statement get evaluated.

### Sequence of Events (Mental Model)

1. The object `20` is created and the name `age` is bound to it
2. The object `True` is created and the name `has_id` is bound to it
3. The expression `age >= 18` is evaluated → `True`
4. Execution enters the outer `if` block
5. The expression `has_id` is evaluated → `True`
6. The inner `if` block is executed
7. All corresponding `else` branches are skipped
8. Execution continues after the nested structure
9. `"End of Case 5"` is printed unconditionally

## Conclusion

Nested `if` statements in Python:
- represent **dependent conditions**
- evaluate inner conditions **only if outer conditions pass**
- create a **hierarchical control flow**, not a flat one

Nesting expresses dependency, not sequence.
Overuse of nesting often signals logic that can be flattened or refactored.

---

## if_else.py – Case 6: Boolean expressions (`and`, `or`)

### Question 
DO NOT RUN.

```python
age = 25
is_member = True

if age >= 18 and is_member:
    print("Adult member")
else:
    print("Access denied")

print("End of Case 6")
```

### Predicted Output
```text
Adult member
End of Case 6
```

### Answer

**Output:**
```text
Adult member
End of Case 6
```

The condition uses a boolean expression combining two sub-conditions with `and`.  
The entire expression evaluates to `True` only if **both** operands are truthy.

### Sequence of Events (Mental Model)

1. The object `25` is created and the name `age` is bound to it
2. The object `True` is created and the name `is_member` is bound to it
3. The expression `age >= 18` is evaluated → `True`
4. The expression `is_member` is evaluated → `True`
5. The boolean expression `True and True` evaluates to `True`
6. The `if` block is executed
7. The `else` block is skipped
8. Execution continues after the conditional
9. `"End of Case 6"` is printed unconditionally

## Conclusion

Boolean expressions in Python:
- combine multiple conditions into **a single logical test**
- reduce the need for nested `if` statements
- evaluate left to right with **short-circuit behavior**

Logical operators express intent more clearly than deep nesting when conditions are related.

---

## if_else.py – Case 7: Comparison operators

### Question 
DO NOT RUN.

```python
a = 5
b = 10

if a == b:
    print("a equals b")
else:
    print("a does not equal b")

if a != b:
    print("a is not equal to b")

print("End of Case 7")
```

### Predicted Output
```text
a does not equal b
a is not equal to b
End of Case 7
```

### Answer

**Output:**
```text
a does not equal b
a is not equal to b
End of Case 7
```

The first comparison checks equality using `==`.
Because `a` and `b` refer to different numeric values, the condition evaluates to `False`.
The second comparison uses `!=`, which evaluates to `True` for unequal values.

### Sequence of Events (Mental Model)

1. The object `5` is created and the name `a` is bound to it
2. The object `10` is created and the name `b` is bound to it
3. The expression `a == b` is evaluated → `False`
4. The `else` branch of the first conditional is executed
5. The expression `a != b` is evaluated → `True`
6. The corresponding `if` block is executed
7. Execution continues after both conditionals
8. `"End of Case 7"` is printed unconditionally

## Conclusion

Comparison operators in Python:
- compare **values**, not names
- always produce a boolean result
- are commonly used as control-flow conditions

Equality (`==`) and inequality (`!=`) are logical opposites, but each comparison is evaluated independently.

---

## if_else.py – Case 8: Chained comparisons

### Question 
DO NOT RUN.

```python
x = 7

if 5 < x < 10:
    print("x is between 5 and 10")

print("End of Case 8")
```

### Predicted Output
```text
x is between 5 and 10
End of Case 8
```

### Answer

**Output:**
```text
x is between 5 and 10
End of Case 8
```

The chained comparison `5 < x < 10` is evaluated as a single logical expression.  
Python checks both comparisons while evaluating `x` only once.

### Sequence of Events (Mental Model)

1. The object `7` is created and the name `x` is bound to it
2. The expression `5 < x < 10` is evaluated
3. Python interprets this as `(5 < x) and (x < 10)`
4. The comparison `5 < x` is evaluated → `True`
5. The comparison `x < 10` is evaluated → `True`
6. The combined expression evaluates to `True`
7. The `if` block is executed
8. Execution continues after the conditional
9. `"End of Case 8"` is printed unconditionally

## Conclusion

Chained comparisons in Python:
- are evaluated **left to right**
- reuse the middle operand without re-evaluating it
- are equivalent to combining comparisons with `and`

Chained comparisons improve readability and reduce redundancy when checking ranges.

---

## if_else.py – Case 9: Using `not`

### Question
DO NOT RUN.

```python
is_logged_in = False

if not is_logged_in:
    print("User is not logged in")

print("End of Case 9")
```

### Predicted Output
```text
User is not logged in
End of Case 9
```

### Answer

**Output:**
```text
User is not logged in
End of Case 9
```

The `not` operator inverts the truth value of the expression that follows it.
Because `is_logged_in` is `False`, applying `not` results in `True`.

### Sequence of Events (Mental Model)

1. The object `False` is created and the name `is_logged_in` is bound to it
2. The expression `is_logged_in` is evaluated → `False`
3. The `not` operator inverts the truth value → `True`
4. The `if` statement checks the resulting boolean
5. The condition is truthy, so the `if` block is executed
6. Execution continues after the conditional
7. `"End of Case 9"` is printed unconditionally

## Conclusion

The `not` operator in Python:  
- does **not** change the underlying value
- only inverts the **truth value** of an expression
- is commonly used to express negative conditions clearly

`not` operates on **evaluation results**, not on variables themselves.

---

## if_else.py – Case 10: Implicit `else` (no `else` block)

### Question
DO NOT RUN.

```python
temperature = 30

if temperature > 25:
    print("Hot day")

print("End of Case 10")
```

### Predicted Output
```text
Hot day
End of Case 10
```

### Answer

**Output:**
```text
Hot day
End of Case 10
```

The `if` statement has no `else` block.  
When the condition evaluates to `True`, the `if` block is executed.  
If the condition were `False`, nothing would be executed for this conditional.

### Sequence of Events (Mental Model)

1. The object `30` is created and the name `temperature` is bound to it
2. The expression `temperature > 25` is evaluated → `True`
3. The `if` block is executed
4. There is no `else` branch to consider
5. Execution continues after the conditional
6. `"End of Case 10"` is printed unconditionally

## Conclusion

An `if` statement in Python:
- does **not** require an `else` block
- executes its body **only when the condition is truthy**
- performs **no action** when the condition is false and no `else` is provided

No output is still valid behavior.  
Silence is not an error.

---

## if_else.py – Case 11: Multiple independent `if` statements

### Question
DO NOT RUN.

```python
number = 15

if number > 0:
    print("Positive")

if number % 3 == 0:
    print("Divisible by 3")

print("End of Case 11")
```

### Predicted Output
```text
Positive
Divisible by 3
End of Case 11
```

### Answer

**Output:**
```text
Positive
Divisible by 3
End of Case 11
```

Each `if` statement is evaluated **independently**.  
There is no relationship between them unless explicitly created using `elif` or `else`.

### Sequence of Events (Mental Model)

1. The object `15` is created and the name `number` is bound to it
2. The expression `number > 0` is evaluated → `True`
3. The first `if` block is executed
4. The expression `number % 3 == 0` is evaluated → `True`
5. The second `if` block is executed
6. Execution continues after both conditionals
7. `"End of Case 11"` is printed unconditionally

## Conclusion

Multiple `if` statements in Python:
- are evaluated **independently**
- may all execute if their conditions are true
- do **not** exclude each other by default

Exclusivity only exists when explicitly expressed using `elif` or `else`.  
Separate `if` statements mean separate decisions.

---

## if_else.py – Case 12: `if–elif` vs multiple `if`

### Question
DO NOT RUN.

```python
value = 10

print("if–elif result:")
if value > 5:
    print("Greater than 5")
elif value > 8:
    print("Greater than 8")

print("multiple if result:")
if value > 5:
    print("Also greater than 5")
if value > 8:
    print("Also greater than 8")

print("End of Case 12")
```

### Predicted Output
```text
if–elif result:
Greater than 5
multiple if result:
Also greater than 5
Also greater than 8
End of Case 12
```

### Answer

**Output:**
```text
if–elif result:
Greater than 5
multiple if result:
Also greater than 5
Also greater than 8
End of Case 12
```

The two blocks look similar but behave **very differently**.  
The difference is **exclusivity**.

### Sequence of Events (Mental Model)

**`if–elif` block:**
1. The object `10` is created and the name `value` is bound to it
2. The expression `value > 5` is evaluated → `True`
3. The corresponding `if` block is executed
4. The `elif` condition is **not evaluated at all**
5. Execution continues after the `if–elif` structure

**Multiple `if` block:**
6. The expression `value > 5` is evaluated → `True`
7. The first `if` block is executed
8. The expression `value > 8` is evaluated → `True`
9. The second `if` block is executed
10. Execution continues after both conditionals
11. `"End of Case 12"` is printed unconditionally

## Conclusion

`if–elif` and multiple `if` statements are **not interchangeable**.
- `if–elif`:
  - enforces **exclusivity**
  - stops evaluation after the first truthy condition
- multiple `if`:
  - evaluates **all conditions**
  - may execute **multiple blocks**

Choosing between them is a **logic decision**, not a style preference.

---

## if_else.py – Case 13: Membership test (`in`)

### Question
DO NOT RUN.

```python
role = "admin"

if role in ("admin", "moderator"):
    print("Access granted")
else:
    print("Access denied")

print("End of Case 13")
```

### Predicted Output
```text
Access granted
End of Case 13
```

### Answer

**Output:**
```text
Access granted
End of Case 13
```

The `in` operator checks whether a value is a **member of a container**.  
Because `"admin"` exists inside the tuple `("admin", "moderator")`, the condition evaluates to `True`.

### Sequence of Events (Mental Model)

1. The string object `"admin"` is created and the name `role` is bound to it
2. A tuple object `("admin", "moderator")` is created
3. The expression `role in ("admin", "moderator")` is evaluated
4. Python checks membership by comparing `role` against each element
5. A match is found → the expression evaluates to `True`
6. The `if` block is executed
7. The `else` block is skipped
8. Execution continues after the conditional
9. `"End of Case 13"` is printed unconditionally

## Conclusion

The `in` operator in Python:
- tests **membership**, not equality with the container
- returns a boolean result
- is commonly used for access checks and category validation

Membership expresses **belonging**, not comparison.  
`in` answers “is this one of them?”, not “is this equal to them?”.

---

## if_else.py – Case 14: Identity vs equality (`is` vs `==`)

### Question
DO NOT RUN.

```python
a = None

if a is None:
    print("a is None")

print("End of Case 14")
```

### Predicted Output
```text
a is None
End of Case 14
```

### Answer

**Output:**
```text
a is None
End of Case 14
```

The `is` operator checks **object identity**, not value equality.  
`None` is a singleton object in Python, so identity comparison is the correct and intended check.

### Sequence of Events (Mental Model)

1. The singleton object `None` exists in the runtime
2. The name `a` is bound to the object `None`
3. The expression `a is None` is evaluated
4. Python checks whether both names refer to the **same object**
5. The identity check evaluates to `True`
6. The `if` block is executed
7. Execution continues after the conditional
8. `"End of Case 14"` is printed unconditionally

## Conclusion

Identity and equality in Python are different concepts:
- `is`:
  - checks **object identity**
  - answers “are these the same object?”
- `==`:
  - checks **value equality**
  - answers “do these objects have the same value?”

`None` should always be checked using `is`, not `==`.   
Using `==` here may work accidentally, but `is` expresses the correct intent.

---

## truthy_falsy.py – Case 1: Boolean literals

### Question
DO NOT RUN.

```python
if True:
    print("This runs")

if False:
    print("This does not run")

print("End of Case 1")
```

### Predicted Output
```text
This runs
End of Case 1
```

### Answer

**Output:**
```text
This runs
End of Case 1
```

The `if` statement executes its block only when the condition evaluates to `True`.  
The second `if` condition evaluates to `False`, so its block is skipped entirely.

### Sequence of Events (Mental Model)

1. The boolean object `True` is evaluated as the condition of the first `if`
2. Because the condition is `True`, the corresponding block is executed
3. The boolean object `False` is evaluated as the condition of the second `if`
4. Because the condition is `False`, the block is skipped
5. Execution continues after both `if` statements
6. `"End of Case 1"` is printed unconditionally

## Conclusion

Boolean literals in Python:
- are valid conditions by themselves
- directly control whether an `if` block executes
- require no comparison or expression

An `if` statement does not require a comparison.  
It only requires a value with a truth value.

---

## truthy_falsy.py – Case 2: Numbers as conditions

### Question
DO NOT RUN.

```python
if 1:
    print("1 is truthy")

if 0:
    print("0 is truthy")

print("End of Case 2")
```

### Predicted Output
```text
1 is truthy
End of Case 2
```

### Answer

**Output:**
```text
1 is truthy
End of Case 2
```

In Python, numeric values have an implicit truth value.  
Any non-zero number is considered truthy, while zero is considered falsy.

### Sequence of Events (Mental Model)

1. The integer object `1` is evaluated as the condition of the first `if`
2. Because `1` is non-zero, its truth value is `True`
3. The first `if` block is executed
4. The integer object `0` is evaluated as the condition of the second `if`
5. Because `0` represents zero, its truth value is `False`
6. The second `if` block is skipped
7. Execution continues after both `if` statements
8. `"End of Case 2"` is printed unconditionally

## Conclusion

Numeric values in Python:
- have an implicit truth value
- are truthy when non-zero
- are falsy when equal to zero

Truthiness is a property of the **value**, not its type.  
Numbers do not need to be compared explicitly to control flow.

---

## truthy_falsy.py – Case 3: Strings as conditions

### Question
DO NOT RUN.

```python
if "hello":
    print("Non-empty string is truthy")

if "":
    print("Empty string is truthy")

print("End of Case 3")
```

### Predicted Output
```text
Non-empty string is truthy
End of Case 3
```

### Answer

**Output:**
```text
Non-empty string is truthy
End of Case 3
```

In Python, strings have an implicit truth value.  
A non-empty string is considered truthy, while an empty string is considered falsy.

### Sequence of Events (Mental Model)

1. The string object `"hello"` is evaluated as the condition of the first `if`
2. Because the string is non-empty, its truth value is `True`
3. The first `if` block is executed
4. The empty string `""` is evaluated as the condition of the second `if`
5. Because the string is empty, its truth value is `False`
6. The second `if` block is skipped
7. Execution continues after both `if` statements
8. `"End of Case 3"` is printed unconditionally

## Conclusion

String values in Python:
- have an implicit truth value
- are truthy when non-empty
- are falsy when empty

Truthiness reflects **content presence**, not semantic meaning.  
An empty string means “nothing”, not “false text”.

---

## truthy_falsy.py – Case 4: Lists as conditions

### Question
DO NOT RUN.

```python
if [1, 2, 3]:
    print("Non-empty list is truthy")

if []:
    print("Empty list is truthy")

print("End of Case 4")
```

### Predicted Output
```text
Non-empty list is truthy
End of Case 4
```

### Answer

**Output:**
```text
Non-empty list is truthy
End of Case 4
```

Lists in Python have an implicit truth value.  
A non-empty list is truthy, while an empty list is falsy.

### Sequence of Events (Mental Model)

1. The list object `[1, 2, 3]` is evaluated as the condition of the first `if`
2. Because the list contains elements, its truth value is `True`
3. The first `if` block is executed
4. The empty list `[]` is evaluated as the condition of the second `if`
5. Because the list contains no elements, its truth value is `False`
6. The second `if` block is skipped
7. Execution continues after both `if` statements
8. `"End of Case 4"` is printed unconditionally

## Conclusion

List values in Python:
- have an implicit truth value
- are truthy when non-empty
- are falsy when empty

Truthiness for collections is based on **element count**, not content type.  
An empty container represents absence, not failure.

---

## truthy_falsy.py – Case 5: `None` as condition

### Question
DO NOT RUN.

```python
value = None

if value:
    print("Value exists")
else:
    print("Value is None or falsy")

print("End of Case 5")
```

### Predicted Output
```text
Value is None or falsy
End of Case 5
```

### Answer

**Output:**
```text
Value is None or falsy
End of Case 5
```

The object `None` has a falsy truth value in Python.  
When evaluated in a conditional context, it behaves like other falsy values such as `0`, `""`, or `[]`.

### Sequence of Events (Mental Model)

1. The singleton object `None` exists in the runtime
2. The name `value` is bound to the object `None`
3. The expression `value` is evaluated as a condition
4. The truth value of `None` is `False`
5. The `if` block is skipped
6. The `else` block is executed
7. Execution continues after the conditional
8. `"End of Case 5"` is printed unconditionally

## Conclusion

`None` in Python:
- represents **absence of a value**
- has a falsy truth value
- should not be confused with `False`

Falsy does not mean boolean `False`.  
It means “evaluates to false in a conditional context”.

---

## truthy_falsy.py – Case 6: Explicit vs implicit checks

### Question
DO NOT RUN.

```python
items = []

if items:
    print("Items exist")

if items == []:
    print("Items list is empty")

print("End of Case 6")
```

### Predicted Output
```text
Items list is empty
End of Case 6
```

### Answer

**Output:**
```text
Items list is empty
End of Case 6
```

The two conditions test **different things**, even though they may appear related.  
`if items:` checks the **truth value** of the object, while `items == []` checks **value equality**.

### Sequence of Events (Mental Model)

1. An empty list object `[]` is created and the name `items` is bound to it
2. The expression `items` is evaluated as a condition
3. Because the list is empty, its truth value is `False`
4. The first `if` block is skipped
5. The expression `items == []` is evaluated
6. The comparison checks value equality → `True`
7. The second `if` block is executed
8. Execution continues after both conditionals
9. `"End of Case 6"` is printed unconditionally

## Conclusion

Implicit and explicit checks serve different purposes:
- Implicit check (`if items:`):
  - asks “does this container have elements?”
  - expresses **presence or absence**
- Explicit check (`items == []`):
  - asks “is this exactly an empty list?”
  - expresses **structural equality**

Both can be correct, but they communicate **different intent**.  
Choose based on meaning, not just outcome.

---

## truthy_falsy.py – Case 7: Function return truthiness

### Question
DO NOT RUN.

```python
def get_value():
    return ""

result = get_value()

if result:
    print("Function returned something")

print("End of Case 7")
```

### Predicted Output
```text
End of Case 7
```

### Answer

**Output:**
```text
End of Case 7
```

The function returns an empty string.  
An empty string has a falsy truth value, so the `if` block is skipped.

### Sequence of Events (Mental Model)

1. The function `get_value` is defined
2. The function is called and returns the string `""`
3. The name `result` is bound to the returned string
4. The expression `result` is evaluated as a condition
5. Because the string is empty, its truth value is `False`
6. The `if` block is skipped
7. Execution continues after the conditional
8. `"End of Case 7"` is printed unconditionally

## Conclusion

Function return values in Python:
- are evaluated by their **truth value**, not by their origin
- can be falsy even when a function successfully returns
- should not be confused with “no return” or failure

A function can return a value and still be falsy.  
Silence does not imply absence of execution.

---

## truthy_falsy.py – Case 8: Using `not` with non-boolean values

### Question
DO NOT RUN.

```python
data = []

if not data:
    print("Data is empty")

print("End of Case 8")
```

### Predicted Output
```text
Data is empty
End of Case 8
```

### Answer

**Output:**
```text
Data is empty
End of Case 8
```

The `not` operator inverts the truth value of the expression.   
An empty list is falsy, so applying `not` makes the condition truthy.

### Sequence of Events (Mental Model)

1. An empty list object `[]` is created and the name `data` is bound to it
2. The expression `data` is evaluated → falsy
3. The `not` operator inverts the truth value → `True`
4. The `if` statement checks the resulting boolean
5. The `if` block is executed
6. Execution continues after the conditional
7. `"End of Case 8"` is printed unconditionally

## Conclusion

The `not` operator in Python:
- works on **truth values**, not data types
- can be applied to any expression with a truth value
- is commonly used to express emptiness or absence

`not x` means “x evaluates to false”, not “x is equal to False”.

---

## truthy_falsy.py – Case 9: Different falsy values

### Question
DO NOT RUN.

```python
values = [0, "", [], None, False]

for v in values:
    if v:
        print(v, "is truthy")
    else:
        print(v, "is falsy")

print("End of Case 9")
```

### Predicted Output
```text
0 is falsy
 is falsy
[] is falsy
None is falsy
False is falsy
End of Case 9
```

### Answer

**Output:**
```text
0 is falsy
 is falsy
[] is falsy
None is falsy
False is falsy
End of Case 9
```

All elements in the list evaluate to **falsy**, even though they are **different types** and represent **different meanings**.

### Sequence of Events (Mental Model)

1. A list containing multiple objects is created: `0`, `""`, `[]`, `None`, `False`
2. The `for` loop iterates over each element
3. Each element `v` is evaluated as a condition
4. Python computes the truth value of `v`
5. All values evaluate to falsy:
  - `0` → zero numeric value
  - `""` → empty string
  - `[]` → empty container
  - `None` → absence of value
  - `False` → boolean false
6. The `else` branch is executed for every iteration
7. Execution continues after the loop
8. `"End of Case 9"` is printed unconditionally

## Conclusion

Different values in Python can be **falsy for different reasons**:
- falsy does **not** mean identical
- falsy does **not** imply the same semantics
- truthiness only answers one question:
  **“Should this be treated as true in a conditional?”**

Truth value is a **control-flow concept**, not a type system.  
Never assume meaning based solely on truthiness.

---

## truthy_falsy.py – Case 10: Dangerous assumption

### Question
DO NOT RUN.

```python
user_age = 0

if user_age:
    print("Age provided")
else:
    print("Age missing")

print("End of Case 10")
```

### Predicted Output
```text
Age missing
End of Case 10
```

### Answer

**Output:**
```text
Age missing
End of Case 10
```

The condition uses an **implicit truthiness check**.  
Because `0` is a falsy value, the condition evaluates to `False`, even though `0` may be a **valid and intentional value**.

### Sequence of Events (Mental Model)

1. The integer object `0` is created and the name `user_age` is bound to it
2. The expression `user_age` is evaluated as a condition
3. Because `0` is falsy, the condition evaluates to `False`
4. The `if` block is skipped
5. The `else` block is executed
6. Execution continues after the conditional
7. `"End of Case 10"` is printed unconditionally

## Conclusion

Implicit truthiness checks can be **dangerous** when falsy values are valid data.
- `0`, `""`, and `[]` may represent **real information**
- using `if x:` can silently misclassify valid values as “missing”
- explicit checks communicate intent more safely in these cases

Truthiness answers **“should this control flow continue?”**, not **“does this value exist?”**