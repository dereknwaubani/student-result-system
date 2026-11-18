# New Horizon Student Result Management System

**Student:** Nwaubani Derek Chibuikem  
**Matriculation Number:** 24/SCI01/126  
**Department:** Computer Science  
**Project:** Student Result Management System  
**Language:** Python 3

## Project description

This is a menu-driven Python application designed to help a secondary school manage student information and academic results. It supports student registration, searching, updating and deletion; subject score entry; automatic total, average and grade calculation; individual report cards; class ranking and statistics; and saving reports to text files.

Student records are stored in `data/students.json`, so records remain available when the application is closed and reopened.

## Requirements

- Python 3.8 or later
- No third-party Python packages are required.

## How to run

1. Download or clone this repository.
2. Open a terminal or command prompt in the project folder.
3. Run:

   ```bash
   python main.py
   ```

   On some systems, use `python3 main.py`.

4. Select an option from the menu and follow the prompts.

## Main features

1. Register a student with ID, name, class/form, gender and date of birth.
2. View all registered students.
3. Search by student ID or name.
4. Update student information.
5. Delete a student record.
6. Record or update scores in at least five subjects.
7. Calculate totals, averages and grades automatically.
8. Display individual report cards.
9. Rank students by average and show class statistics.
10. Save class reports as text files.

## Grading scale

The project uses the following example grading scale. It can be adjusted to match the school's official grading policy.

| Average score | Grade |
|---|---|
| 80–100 | A |
| 70–79.99 | B |
| 60–69.99 | C |
| 50–59.99 | D |
| Below 50 | F |

Each subject score must be between 0 and 100.

## Project structure

```text
student_result_system/
├── main.py
├── student.py
├── results.py
├── storage.py
├── reports.py
├── data/
│   └── students.json
├── reports/
└── README.md
```

## Python concepts demonstrated

- Variables, strings, numbers and type conversion
- `if`, `elif`, `else`, `for` and `while`
- Lists and dictionaries
- Functions with parameters and return values
- Sorting with `sorted()`
- Exception handling with `try` and `except`
- JSON file reading and writing
- Modules and imports
- Object-Oriented Programming using the `Student` class
- Date validation and result-entry timestamps using `datetime`
- File and folder handling using `pathlib`

## Data and privacy

The project starts with an empty student database. Use fictional student records for demonstrations unless you have permission to use real student information. The JSON file is stored locally in the project folder.

## GitHub

Create a repository named `student-result-system`, then upload the complete project folder. Make several meaningful commits as you develop and test the application.
