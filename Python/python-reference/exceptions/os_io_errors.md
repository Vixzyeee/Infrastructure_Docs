# OS & I/O Errors (Operating System Failures)

This document covers **operating system and I/O related exceptions**.

These exceptions occur when Python interacts with the **file system, processes, or network resources**, and the operating system reports a failure.

They are runtime errors and inherit from `OSError`.

---

## Overview

OS and I/O errors usually indicate:
- Missing or invalid file paths
- Permission issues
- Invalid directories
- Resource exhaustion
- Network or connection failures

These errors are **environment-dependent** and must always be handled defensively.

---

## `OSError`

### Description
Base class for all operating system related errors.

**Example:**
```python
import os
os.listdir("/nonexistent")
```

**Error:**
```text
FileNotFoundError: [Errno 2] No such file or directory
```

**Notes:**
- Rarely raised directly
- Most OS-level errors are raised as subclasses

**Rule:**
Catch subclasses instead of `OSError` whenever possible.

---

## `FileNotFoundError`

### Description
Raised when a file or directory does not exist.

**Example:**
```python
open("missing.txt")
```

**Error:**
```text
FileNotFoundError: [Errno 2] No such file or directory
```

**Notes:**
- Very common in production
- Often caused by wrong paths or missing deployments

**Rule:**
Never assume files exist.

---

## `FileExistsError`

### Description
Raised when attempting to create a file or directory that already exists.

**Example:**
```python
import os
os.mkdir("data")
```

**Error:**
```text
FileExistsError: [Errno 17] File exists
```

**Notes:**
- Common when running scripts repeatedly

**Rule:**
Check existence or use idempotent operations.

---

## `PermissionError`

### Description
Raised when the process lacks sufficient permissions.

**Example:**
```python
open("/root/secret.txt")
```

**Error:**
```text
PermissionError: [Errno 13] Permission denied
```

**Notes:**
- Common on Linux servers
- Often appears after deployment

**Rule:**
Design for least privilege.

---

## `IsADirectoryError`

### Description
Raised when a directory is used where a file is expected.

**Example:**
```python
open("/etc")
```

**Error:**
```text
IsADirectoryError: [Errno 21] Is a directory
```

**Notes:**
- Caused by incorrect path assumptions

**Rule:**
Validate path types explicitly.

---

## `NotADirectoryError`

### Description
Raised when a file is used where a directory is expected.

**Example:**
```python
import os
os.listdir("file.txt")
```

**Error:**
```text
NotADirectoryError: [Errno 20] Not a directory
```

**Notes:**
- Often appears in config-driven systems

**Rule:**
Never assume paths are directories.

---

## `TimeoutError`

### Description
Raised when an operation exceeds the allowed time limit.

**Example:**
```python
import socket

socket.setdefaulttimeout(0.001)
s = socket.socket()
s.connect(("example.com", 80))
```

**Error:**
```text
TimeoutError: timed out
```

**Notes:**
- Error messages may vary by OS or library
- Common in networking and I/O

**Rule:**
Timeouts are expected. Handle them.

---

## `ConnectionError`

### Description
Base class for connection-related errors.

**Example:**
```python
raise ConnectionError("Connection failed")
```

**Error:**
```text
ConnectionError: Connection failed
```

**Notes:**
- Rarely raised directly
- Used for grouping connection failures

**Rule:**
Catch subclasses for specific handling.

---

## `ConnectionRefusedError`

### Description
Raised when a connection attempt is explicitly refused.

**Example:**
```python
import socket

s = socket.socket()
s.connect(("localhost", 1))
```

**Error:**
```text
ConnectionRefusedError: [Errno 111] Connection refused
```

**Notes:**
- Service is not running or port is closed

**Rule:**
Retrying blindly will not fix this.

---

## `ConnectionResetError`

### Description
Raised when an established connection is forcibly closed.

**Example:**
```python
raise ConnectionResetError("Connection reset")
```

**Error:**
```text
ConnectionResetError: Connection reset
```

**Notes:**
- Often caused by remote crashes or network drops

**Rule:**
Design retry logic carefully.

---

## `ConnectionAbortedError`

### Description
Raised when a connection is aborted locally.

**Example:**
```python
raise ConnectionAbortedError("Connection aborted")
```

**Error:**
```text
ConnectionAbortedError: Connection aborted
```

**Notes:**
- May indicate improper socket handling

**Rule:**
Investigate connection lifecycle.

## Common Patterns & Mistakes

**❌ Assuming the Environment Is Stable**
```python
open("config.yaml")
```

**✅ Defensive I/O Handling**
```python
try:
    open("config.yaml")
except FileNotFoundError:
    handle_missing_file()
except PermissionError:
    handle_permission_issue()
```

---

## Summary
- OS and I/O errors depend heavily on the environment
- `OSError` is the base class
- Always catch specific subclasses
- Files, permissions, and networks fail frequently
- Defensive programming is mandatory

If your code only works on your machine, it is not production-ready.