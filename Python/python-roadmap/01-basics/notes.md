# Answers – 01-basics

---

## variables.py – Case 1: Variable rebinding

### Question  
DO NOT RUN.

```python
a = 10
b = a
a = a + 5

print(a)
print(b)
```

### Predicted Output
```text
15
10
```

### Answer

**Output:**
```text
15
10
```

`b` does not change because the name `b` still points to the object `10`.

### Sequence of Events (Mental Model)

1. Object `10` is created, and the name `a` is bound to it
2. The name `b` is bound to the same object
3. The expression `a + 5` creates a new object `15`
4. The name `a` is rebound to the object `15`
5. The name `b` still points to the object `10`

## Conclusion
Assignment in Python changes the **name** → **object** relationship, not the object itself.

---

## variables.py – Case 2: Deleting a name vs deleting an object

### Question
DO NOT RUN.

```python
x = 100
y = x

del x

print(y)
```

### Predicted Output
```text
100
```

### Answer

**Output:**
```text
100
```

`del x` removes the name `x`, not the object it was pointing to.

### Sequence of Events (Mental Model)

1. Object `100` is created, and the name `x` is bound to it
2. The name `y` is bound to the same object
3. The name `x` is deleted
4. The object `100` is still alive because it is still referenced by `y`
5. `print(y)` is still valid

## Conclusion
`del` removes a **name**, not an **object**.

---

## variables.py – Case 3: Expression rebinding

### Question 
DO NOT RUN.

```python
x = 1
y = x
x = x + 1

print(x)
print(y)
```

### Predicted Output
```text
2
1
```

### Answer

**Output:**
```text
2
1
```

`y` does not change because `x + 1` creates a new object, and assignment only rebinds the name `x`; the name `y` still points to the original object `1`.

### Sequence of Events (Mental Model)

1. Object `1` is created, and the name `x` is bound to it
2. The name `y` is bound to the same object `1`
3. The expression `x + 1` creates a new object `2`
4. The name `x` is rebound to the object `2`
5. The name `y` still points to the object `1`

## Conclusion
An expression like `x + 1` creates a new object; assignment rebinds the name.  
No object is modified in place.

---

## variables.py – Case 4: String concatenation vs f-string

### Question 
DO NOT RUN.

```python
name = "Alice"
age = 20

message_concat = "Name: " + name + ", Age: " + str(age)
message_fstring = f"Name: {name}, Age: {age}"

print(message_concat)
print(message_fstring)
```

### Predicted Output
```text
Name: Alice, Age: 20
Name: Alice, Age: 20
```

### Answer

**Output:**
```text
Name: Alice, Age: 20
Name: Alice, Age: 20
```

String concatenation (`+`) requires all operands to be strings

### Sequence of Events (Mental Model)

1. Variables `name` and `age` are bound to objects
2. Concatenation creates a new string object
3. `str(age)` explicitly converts an integer to a string
4. f-string evaluates expressions and builds the final string

## Conclusion
f-strings are the preferred way to format strings in modern Python.

---

## data_types.py – Case 1: Type belongs to the object

### Question 
DO NOT RUN.

```python
x = 10
print(type(x))

x = "10"
print(type(x))
```

### Predicted Output
```text
<class 'int'>
<class 'str'>
```

### Answer

**Output:**
```text
<class 'int'>
<class 'str'>
```

The type does not belong to the name `x`; assignment rebinds `x` to a new object with a different type.

### Sequence of Events (Mental Model)

1. Object `10` of type `int` is created, name `x` is bound to it
2. The type is a property of the object, not the name
3. A new object `"10"` of type `str` is created
4. Name `x` is rebound to the new object

## Conclusion
The type in Python belongs to the object; assignment rebinds the name to a different object.

---

## data_types.py – Case 2: Immutability and rebinding

### Question 
DO NOT RUN.

```python
x = 10
print(id(x))

x = x + 1
print(id(x))
```

### Predicted Output
```text
(two different ids)
```

### Answer

**Output:**
```text
(two different ids)
```

The two `id()` values are different because `x + 1` creates a new object; the original object is not modified.

### Sequence of Events (Mental Model)

1. An object `10` of type `int` is created, and `x` is bound to it
2. `id(x)` returns the identity of that object
3. The expression `x + 1` creates a new object `11`
4. The name `x` is rebound to the new object
5. The original object `10` remains unchanged and remains unchanged and unreferenced

## Conclusion
`int` objects are immutable; operations create new objects, and assignment rebinds names instead of modifying objects in place.

---

## data_types.py – Case 3: Mutable objects (list)

### Question 
DO NOT RUN.

```python
x = [1, 2, 3]
print(id(x))

x.append(4)
print(id(x))

print(x)
```

### Predicted Output
```text
(same id)
[1, 2, 3, 4]
```

### Answer

**Output:**
```text
(same id)
[1, 2, 3, 4]
```

The `id` does not change because the list object is modified in place; no new object is created.

### Sequence of Events (Mental Model)

1. A list object `[1, 2, 3]` is created, and `x` is bound to it
2. `id(x)` returns the identity of that list object
3. The method call `append(4)` mutates the existing list object
4. No new object is created
5. The name `x` still points to the same object

## Conclusion
Mutable objects like `list` can be modified in place; method calls mutate the object without rebinding the name.

---

## data_types.py – Case 4: Shared reference (mutable object)

### Question 
DO NOT RUN.

```python
a = [1, 2]
b = a

print(id(a))
print(id(b))

b.append(3)

print(a)
print(b)
```

### Predicted Output
```text
(same id)
[1, 2, 3]
[1, 2, 3]
```

### Answer

**Output:**
```text
(same id)
[1, 2, 3]
[1, 2, 3]
```

Both `a` and `b` point to the same list object, so mutating the object through one name is visible through the other.

### Sequence of Events (Mental Model)

1. A list object `[1, 2]` is created, and `a` is bound to it
2. The name `b` is bound to the same object as `a`
3. `id(a)` and `id(b)` return the same identity
4. The method call `append(3)` mutates the shared list object
5. Both names still point to the same mutated object

## Conclusion
When multiple names reference the same mutable object, mutations via one name affect all references.

---

## print_input.py – Case 1: `input()` always returns `str`

### Question
DO NOT RUN.

```python
age = input("Enter your age: ")

print(type(age))
print(age + "1")
```

### Predicted Output
```text
<class 'str'>
<age_as_text>1
```

### Answer

**Output:**
```text
<class 'str'>
<age_as_text>1
```

Python does not infer intent.  
All type conversion is explicit.

### Sequence of Events (Mental Model)

1. User types characters via standard input
2. `input()` reads the characters as text
3. A `str` object is created
4. The name `age` is bound to that `str` object
5. The expression `age + "1"` concatenates two strings

## Conclusion
User input is text by default.  
Numeric behavior exists only after explicit conversion.

---

## print_input.py – Case 2: Explicit conversion can fail

### Question
DO NOT RUN.

```python
age = input("Enter your age: ")

age_int = int(age)

print(age_int + 1)
```

### Predicted Output

**Case A – Valid numeric input (`20`):**
```text
21
```

**Case B – Non-numeric input (`dua puluh`):**
```text
ValueError: invalid literal for int() with base 10
```

### Answer

**Output:**

Case A – valid input:
```text
21
```

Case B - invalid input:
```text
ValueError: invalid literal for int() with base 10
```

`int()` explicitly converts a string to an integer.

### Sequence of Events (Mental Model)

1. `input()` returns a `str`
2. `int()` attempts to parse the string into an integer
3. If parsing fails, a `ValueError` is raised
4. Program execution stops immediately

## Conclusion
Type conversion is explicit and **unsafe by default**.  
Invalid input causes immediate failure unless explicitly handled.