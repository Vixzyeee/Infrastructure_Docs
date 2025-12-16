# Import Keywords

## What is this?
Import keywords are used to include modules or objects
from other modules into the current Python file.

---

## import
**Purpose:** Import a module.

```python
import math
print(math.sqrt(16))
```

**Output:**

```text
4.0
```

**Notes:**

- Imports the entire module
- Module members are accessed using dot notation

---

## from
**Purpose:** Import specific objects from a module.

```python
from math import sqrt
print(sqrt(16))
```

**Output:**

```text
4.0
```

**Notes:**

- Imports only specified objects
- Accessed directly without module name

---

## as
**Purpose:** Assign an alias to an imported module or object.

```python
import math as m
print(m.sqrt(16))
```

**Output:**

```text
4.0
```

**Notes:**

- Used to shorten names
- Commonly used to avoid name conflicts

---
