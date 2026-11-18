"""JSON storage functions for student records."""

import json
from pathlib import Path
from student import Student

DATA_FILE = Path(__file__).parent / "data" / "students.json"


def load_students():
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            records = json.load(file)
        if not isinstance(records, list):
            raise ValueError("The data file must contain a list of students.")
    except json.JSONDecodeError:
        print("Warning: students.json is damaged or empty. Starting with no records.")
        return []
    except (KeyError, TypeError, ValueError) as error:
        print(f"Warning: student data could not be loaded: {error}")
        return []
    else:
        return [Student.from_dict(record) for record in records]


def save_students(students):
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    temporary_file = DATA_FILE.with_suffix(".tmp")
    try:
        with temporary_file.open("w", encoding="utf-8") as file:
            json.dump([student.to_dict() for student in students], file, indent=4)
    except OSError:
        print("Could not save student records. Please check folder permissions.")
        raise
    else:
        temporary_file.replace(DATA_FILE)
    finally:
        # Remove an unfinished temporary file if saving did not complete.
        if temporary_file.exists():
            temporary_file.unlink()
