# Student Grade Checker

A simple terminal-based Python program that converts a student's mark into the corresponding letter grade.

## Grading Scale

| Mark Range | Grade |
|------------|-------|
| 90 - 100 | A |
| 80 - 89 | B |
| 70 - 79 | C |
| 60 - 69 | D |
| Below 60 | E |

## Features

- Accepts marks between 0 and 100.
- Calculates the corresponding grade.
- Handles invalid numeric ranges.
- Handles non-numeric input without crashing.
- Continues prompting until a valid mark is entered.
- Allows multiple marks to be checked in the same session.
- Asks for confirmation before exiting.
- Uses only standard Python with no external packages.

## Run the Program

```bash
python grade_system.py
```

Example:

```text
==================================================
             STUDENT GRADE CHECKER
==================================================

Enter your mark (0 - 100): 92

--------------------------------------------------
A mark of 92 falls under Grade A.
--------------------------------------------------

Would you like to check another mark? (Y/N): N

Thank you for using the Student Grade Checker!
```

## Requirements

- Python 3
- No external packages or frameworks required

## File

The main program is contained in:

```text
grade_system.py
```