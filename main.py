"""Main menu and user interaction for the Student Result Management System."""

from datetime import datetime
from student import Student
from storage import load_students, save_students
from results import get_result
from reports import student_report, class_report, save_text_report

SUBJECTS = [
    "English Language",
    "Mathematics",
    "Basic Science",
    "Social Studies",
    "Computer Studies",
]


def find_student(students, search_term):
    term = search_term.strip().lower()
    return next((student for student in students
                 if student.student_id.lower() == term
                 or term in student.full_name.lower()), None)


def get_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")


def get_score():
    while True:
        try:
            score = float(input("Enter score (0-100): "))
            if 0 <= score <= 100:
                return score
            print("Score must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")


def add_student(students):
    print("\n--- REGISTER NEW STUDENT ---")
    student_id = get_non_empty("Student ID: ")
    if find_student(students, student_id):
        print("A student with that ID or matching name already exists.")
        return

    full_name = get_non_empty("Full name: ")
    class_form = get_non_empty("Class/Form (e.g. JSS 1): ")
    gender = get_non_empty("Gender: ")

    while True:
        date_of_birth = get_non_empty("Date of birth (YYYY-MM-DD): ")
        try:
            datetime.strptime(date_of_birth, "%Y-%m-%d")
            break
        except ValueError:
            print("Use the date format YYYY-MM-DD.")

    students.append(Student(student_id, full_name, class_form, gender, date_of_birth))
    save_students(students)
    print("Student registered successfully.")


def view_students(students):
    print("\n--- REGISTERED STUDENTS ---")
    if not students:
        print("No students registered yet.")
        return
    print(f"{'ID':<15}{'FULL NAME':<28}{'CLASS':<12}{'AVERAGE':>9}  GRADE")
    print("-" * 75)
    for student in sorted(students, key=lambda item: item.full_name.lower()):
        result = get_result(student.scores)
        print(f"{student.student_id:<15}{student.full_name[:27]:<28}"
              f"{student.class_form:<12}{result['average']:>9.2f}  "
              f"{result['grade']}")


def search_student(students):
    term = input("Enter student ID or part of the student's name: ")
    student = find_student(students, term)
    if student:
        print(student_report(student))
    else:
        print("Student not found.")


def update_student(students):
    student = find_student(students, input("Enter student ID: "))
    if not student:
        print("Student not found.")
        return
    print("Press Enter to keep the current value.")
    for attribute, label in [
        ("full_name", "Full name"),
        ("class_form", "Class/Form"),
        ("gender", "Gender"),
        ("date_of_birth", "Date of birth (YYYY-MM-DD)"),
    ]:
        current = getattr(student, attribute)
        new_value = input(f"{label} [{current}]: ").strip()
        if new_value:
            if attribute == "date_of_birth":
                try:
                    datetime.strptime(new_value, "%Y-%m-%d")
                except ValueError:
                    print("Invalid date; keeping the previous date.")
                    continue
            setattr(student, attribute, new_value)
    save_students(students)
    print("Student information updated.")


def delete_student(students):
    student = find_student(students, input("Enter student ID: "))
    if not student:
        print("Student not found.")
        return
    confirm = input(f"Delete {student.full_name}? (y/n): ").strip().lower()
    if confirm == "y":
        students.remove(student)
        save_students(students)
        print("Student record deleted.")
    else:
        print("Deletion cancelled.")


def enter_or_update_scores(students):
    student = find_student(students, input("Enter student ID: "))
    if not student:
        print("Student not found.")
        return
    print(f"\nEntering/updating scores for {student.full_name}")
    print("Choose a subject:")
    for number, subject in enumerate(SUBJECTS, start=1):
        print(f"{number}. {subject}")
    print("6. Enter another subject")
    try:
        choice = int(input("Subject number: "))
        if 1 <= choice <= 5:
            subject = SUBJECTS[choice - 1]
        elif choice == 6:
            subject = get_non_empty("Subject name: ")
        else:
            print("Invalid subject choice.")
            return
    except ValueError:
        print("Please enter a number.")
        return

    student.record_score(subject, get_score())
    save_students(students)
    result = get_result(student.scores)
    print(f"Score saved. Current total: {result['total']:.2f}")
    print(f"Current average: {result['average']:.2f}; Grade: {result['grade']}")


def display_report_card(students):
    student = find_student(students, input("Enter student ID: "))
    if student:
        print(student_report(student))
    else:
        print("Student not found.")


def display_class_report(students):
    content = class_report(students)
    print("\n" + content)
    choice = input("Save this report to a text file? (y/n): ").strip().lower()
    if choice == "y":
        path = save_text_report(content, "class_result_summary")
        print(f"Report saved to: {path}")


def main():
    students = load_students()
    print("Welcome to NEW HORIZON STUDENT RESULT MANAGEMENT SYSTEM")

    while True:
        print("""
================ MAIN MENU ================
1. Register a new student
2. View all students
3. Search for a student
4. Update student information
5. Delete a student
6. Record or update subject scores
7. Display an individual report card
8. View class results, ranking and statistics
9. Save class report to a text file
0. Exit
============================================
""")
        choice = input("Enter your choice: ").strip()
        try:
            if choice == "1":
                add_student(students)
            elif choice == "2":
                view_students(students)
            elif choice == "3":
                search_student(students)
            elif choice == "4":
                update_student(students)
            elif choice == "5":
                delete_student(students)
            elif choice == "6":
                enter_or_update_scores(students)
            elif choice == "7":
                display_report_card(students)
            elif choice == "8":
                display_class_report(students)
            elif choice == "9":
                content = class_report(students)
                path = save_text_report(content, "class_result_summary")
                print(f"Report saved to: {path}")
            elif choice == "0":
                save_students(students)
                print("Thank you for using the system. Goodbye!")
                break
            else:
                print("Invalid choice. Select a number from 0 to 9.")
        except (OSError, TypeError, ValueError) as error:
            print(f"An error occurred: {error}")


if __name__ == "__main__":
    main()
