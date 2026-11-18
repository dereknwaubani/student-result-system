"""Functions for calculating totals, averages and grades."""

def calculate_total(scores):
    return sum(float(score) for score in scores.values())


def calculate_average(scores):
    if not scores:
        return 0.0
    return calculate_total(scores) / len(scores)


def assign_grade(average):
    # Grading scale used by this project:
    # A: 80-100, B: 70-79, C: 60-69, D: 50-59, F: below 50.
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    return "F"


def get_result(scores):
    average = calculate_average(scores)
    return {
        "total": calculate_total(scores),
        "average": average,
        "grade": assign_grade(average),
    }
