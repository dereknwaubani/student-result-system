"""Functions for displaying and saving student and class reports."""

from pathlib import Path
from results import get_result

REPORTS_DIR = Path(__file__).parent / "reports"


def student_report(student):
    result = get_result(student.scores)
    lines = [
        "=" * 52,
        "             NEW HORIZON SECONDARY SCHOOL",
        "                 STUDENT REPORT CARD",
        "=" * 52,
        f"Student ID:       {student.student_id}",
        f"Full Name:        {student.full_name}",
        f"Class/Form:       {student.class_form}",
        f"Gender:           {student.gender}",
        f"Date of Birth:    {student.date_of_birth}",
        "-" * 52,
        "SUBJECT RESULTS",
        "-" * 52,
    ]
    if student.scores:
        for subject, score in sorted(student.scores.items()):
            lines.append(f"{subject:<30} {score:>8.2f}")
    else:
        lines.append("No scores have been entered.")
    lines.extend([
        "-" * 52,
        f"Total Score:      {result['total']:.2f}",
        f"Average:          {result['average']:.2f}",
        f"Grade:            {result['grade']}",
        f"Result Entered:   {student.result_entered_at or 'Not yet entered'}",
        "=" * 52,
    ])
    return "\n".join(lines)


def class_report(students):
    lines = ["NEW HORIZON SECONDARY SCHOOL - CLASS RESULT SUMMARY",
             "=" * 72]
    if not students:
        return "\n".join(lines + ["No students registered yet."])

    ranked = sorted(students,
                    key=lambda item: get_result(item.scores)["average"],
                    reverse=True)
    lines.append(f"{'Rank':<6}{'Student ID':<16}{'Name':<25}{'Average':>10}  Grade")
    lines.append("-" * 72)
    averages = []
    for position, student in enumerate(ranked, start=1):
        result = get_result(student.scores)
        averages.append(result["average"])
        lines.append(
            f"{position:<6}{student.student_id:<16}"
            f"{student.full_name[:24]:<25}{result['average']:>10.2f}  "
            f"{result['grade']}"
        )
    lines.append("-" * 72)
    lines.append(f"Highest Average: {max(averages):.2f}")
    lines.append(f"Lowest Average:  {min(averages):.2f}")
    lines.append(f"Class Average:   {sum(averages) / len(averages):.2f}")
    return "\n".join(lines)


def save_text_report(content, filename):
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    safe_name = "".join(char for char in filename
                        if char.isalnum() or char in ("-", "_"))
    if not safe_name:
        safe_name = "class_report"
    path = REPORTS_DIR / f"{safe_name}.txt"
    path.write_text(content, encoding="utf-8")
    return path
