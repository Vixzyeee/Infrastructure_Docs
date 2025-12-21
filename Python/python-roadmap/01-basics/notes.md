# Answers – 01-basics

---

## variables.py – Question 1: Variable rebinding

### Question  
DO NOT RUN.

```python
a = 10
b = a
a = a + 5
print(b)
```

### Predicted Output
```text
10
```

### Answer

**Output:**
```text
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

## variables.py – Question 2: Deleting a name vs deleting an object

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

## variables.py – Question 3: Expression rebinding

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

## XXX.py – Question X: XXX XXX

### Question 
DO NOT RUN.

```python
XXXX
```

### Predicted Output
```text
XXX
```

### Answer

**Output:**
```text
XX
```

XXXX

### Sequence of Events (Mental Model)

1. XXXXX
2. XXXXX
3. XXXXX
4. XXXXX
5. XXXXX

## Conclusion
XXXXXXXXXXXXXXX

---

## XXX.py – Question X: XXX XXX

### Question 
DO NOT RUN.

```python
XXXX
```

### Predicted Output
```text
XXX
```

### Answer

**Output:**
```text
XX
```

XXXX

### Sequence of Events (Mental Model)

1. XXXXX
2. XXXXX
3. XXXXX
4. XXXXX
5. XXXXX

## Conclusion
XXXXXXXXXXXXXXX

---

## XXX.py – Question X: XXX XXX

### Question 
DO NOT RUN.

```python
XXXX
```

### Predicted Output
```text
XXX
```

### Answer

**Output:**
```text
XX
```

XXXX

### Sequence of Events (Mental Model)

1. XXXXX
2. XXXXX
3. XXXXX
4. XXXXX
5. XXXXX

## Conclusion
XXXXXXXXXXXXXXX

---

## XXX.py – Question X: XXX XXX

### Question 
DO NOT RUN.

```python
XXXX
```

### Predicted Output
```text
XXX
```

### Answer

**Output:**
```text
XX
```

XXXX

### Sequence of Events (Mental Model)

1. XXXXX
2. XXXXX
3. XXXXX
4. XXXXX
5. XXXXX

## Conclusion
XXXXXXXXXXXXXXX