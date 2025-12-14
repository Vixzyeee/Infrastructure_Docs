# Linux Learning Roadmap

This roadmap defines a structured journey for learning Linux
from first principles to practical, real-world system operation.

The roadmap is designed to build strong fundamentals before
progressing into automation, troubleshooting, and DevOps-oriented usage.

---

## 00 - Introduction
Goal: Build a correct mental model of Linux.

Topics:
- What Linux is (kernel vs operating system)
- Linux vs Unix
- High-level Linux system architecture

---

## 01 - Environment
Goal: Understand the system you are working on.

Topics:
- Installing Linux (VM, dual-boot, cloud VM)
- Linux filesystem hierarchy (`/`, `/etc`, `/var`, `/home`, etc.)
- Terminal setup and basic shell usage

---

## 02 - Navigation and Files
Goal: Become comfortable moving around and manipulating files.

Topics:
- Directory navigation (`pwd`, `ls`, `cd`, `tree`)
- File creation and removal (`touch`, `mkdir`, `rm`)
- File copying and moving (`cp`, `mv`)
- Globbing and basic path patterns

---

## 03 - File Viewing and Editing
Goal: Read and edit files efficiently.

Topics:
- Viewing files (`cat`, `less`, `head`, `tail`)
- Text editors (`nano`, basic `vim`)
- Understanding file encoding and line endings

---

## 04 - Permissions and Ownership
Goal: Understand Linux access control.

Topics:
- Permission bits and modes
- `chmod`, `chown`, `umask`
- User vs group vs others
- `sudo` and privilege escalation

---

## 05 - Search and Text Processing
Goal: Work efficiently with text and logs.

Topics:
- Searching files and directories (`find`, `locate`)
- Text searching (`grep`)
- Pipelines and redirection
- Introductory `awk` and `sed`

---

## 06 - Processes and System Monitoring
Goal: Understand how Linux runs programs.

Topics:
- Process lifecycle
- `ps`, `top`, `htop`
- Job control (`bg`, `fg`, `jobs`)
- Signals and process termination (`kill`)
- Basic system monitoring

---

## 07 - Package Management
Goal: Install and manage software correctly.

Topics:
- Package managers (`apt`, `dnf`, `yum`)
- Repositories and package sources
- `dpkg` basics
- System updates and upgrades

---

## 08 - Networking
Goal: Understand networking from the Linux perspective.

Topics:
- Network interfaces and IP addressing
- `ip` command
- Connectivity testing (`ping`, `traceroute`)
- DNS basics
- HTTP tools (`curl`, `wget`)

---

## 09 - Storage and Disk Management
Goal: Understand how Linux handles disks and filesystems.

Topics:
- Block devices (`lsblk`)
- Disk usage (`df`, `du`)
- Mounting and unmounting filesystems
- `/etc/fstab`
- Common filesystem types

---

## 10 - Users and Groups
Goal: Manage multi-user systems.

Topics:
- User and group management
- Passwords and authentication
- `su` vs `sudo`
- User environment basics

---

## 11 - Shell and Bash
Goal: Use the shell as a real tool, not just a command runner.

Topics:
- Shell basics
- Environment variables
- Aliases
- Bash scripting fundamentals
- Control flow in scripts

---

## 12 - Logging and Services
Goal: Understand how Linux services run and log information.

Topics:
- System logging
- `journalctl`
- `systemctl`
- Service lifecycle
- Boot process overview

---

## 13 - Security Basics
Goal: Apply basic system security practices.

Topics:
- Linux security concepts
- Firewall basics
- `ufw`
- SSH fundamentals
- SSH key-based authentication
- Intro to intrusion prevention

---

## 14 - Automation and Scheduling
Goal: Automate routine tasks.

Topics:
- `cron`
- `at`
- Automation concepts
- Real-world scheduling examples

---

## 15 - Troubleshooting
Goal: Diagnose and fix system issues.

Topics:
- Reading and understanding logs
- Disk space issues
- Service failures
- Network troubleshooting
- Recovery mode basics

---

## 16 - Linux for DevOps
Goal: Apply Linux knowledge in modern infrastructure.

Topics:
- Linux in cloud environments
- Linux for containers
- Linux in CI/CD pipelines
- Operational best practices

---

## Labs
Goal: Reinforce concepts through hands-on practice.

- Navigation labs
- Permission labs
- Process and monitoring labs
- Networking labs
- Troubleshooting labs
