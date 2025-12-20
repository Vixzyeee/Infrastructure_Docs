# Bitwise Operators

Bitwise operators operate on **individual bits** of integer values.

They are commonly used in:
- low-level programming
- flags and masks
- permissions
- performance-critical code
- protocol and network-related logic

This file focuses on **bitwise operator semantics**, not binary arithmetic theory.

---

## Bitwise AND (`&`)

### Description
Performs a bitwise AND operation between two integers.

### Syntax
```python
a & b
```

**Example:**
```python
print(6 & 3)
```

**Output:**
```text
2
```

### Explanation
```text
6  -> 110
3  -> 011
---------
&     010  -> 2
```

**Notes:**
- Result bit is `1` only if both bits are `1`
- Commonly used for masking bits

---

## Bitwise OR (`|`)

### Description
Performs a bitwise OR operation between two integers.

### Syntax
```python
a | b
```

**Example:**
```python
print(6 | 3)
```

**Output:**
```text
7
```

### Explanation
```text
6  -> 110
3  -> 011
---------
|     111  -> 7
```

**Notes:**
- Result bit is `1` if either bit is `1`
- Often used to combine flags

---

## Bitwise XOR (`^`)

### Description
Performs a bitwise exclusive OR operation.

### Syntax
```python
a ^ b
```

**Example:**
```python
print(6 ^ 3)
```

**Output:**
```text
5
```

### Explanation
```text
6  -> 110
3  -> 011
---------
^     101  -> 5
```

**Notes:**
- Result bit is `1` only if bits differ
- Commonly used for toggling flags

---

## Bitwise NOT (`~`)

### Description
Inverts all bits of an integer.

### Syntax
```python
~a
```

**Example:**
```python
print(~5)
```

**Output:**
```text
-6
```

### Explanation
```text
~x == -(x + 1)
```

**Notes:**
- Python integers are of unlimited size
- Bitwise NOT uses two’s complement logic
- This often surprises people expecting a simple bit flip
- Bit width is not fixed; results differ from languages with fixed-width integers

---

## Bitwise Left Shift (`<<`)

### Description
Shifts bits to the left by a specified number of positions.

### Syntax
```python
a << n
```

**Example:**
```python
print(3 << 2)
```

**Output:**
```text
12
```

### Explanation
```text
3  -> 0011
<< 2
---------
      1100 -> 12
```

**Notes:**
- Equivalent to multiplying by `2 ** n`
- New bits on the right are filled with zeros

---

## Bitwise Right Shift (`>>`)

### Description
Shifts bits to the right by a specified number of positions.

### Syntax
```python
a >> n
```

**Example:**
```python
print(12 >> 2)
```

**Output:**
```text
3
```

### Explanation
```text
12 -> 1100
>> 2
---------
      0011 -> 3
```

**Notes:**
- Equivalent to floor division by `2 ** n` for non-negative integers
- Uses arithmetic shift for negative values

---

## Common Use Case: Bit Masks

**Example:**
```python
READ  = 0b001
WRITE = 0b010
EXEC  = 0b100

permissions = READ | WRITE

print(permissions & READ)
print(permissions & EXEC)
```

**Output:**
```text
1
0
```

**Notes:**
- Flags are combined using `|`
- Flags are tested using `&`
- This pattern is common in system-level code

---

## Bitwise vs Logical Operators

### Important Distinction
```python
a & b      # bitwise
a and b    # logical
```

**Notes:**
- Bitwise operators work on integer bits
- Logical operators work on truthiness
- Confusing these operators causes subtle bugs

---

## Summary
- Bitwise operators manipulate individual bits of integers
- Python integers have unlimited precision
- Shift operators correspond to powers of two
- Bitwise NOT follows two’s complement semantics
- Bitwise operators are distinct from logical operators

This file defines **core bitwise operator semantics** in Python expressions.