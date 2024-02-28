# author: jason wilder

def process_student_failure():
    pass


def get_letter_grade(percent):
    """
    > 100: E
    < 0: E
    80 - 100: A
    65-79: B
    50-64: C
    0-49: F
    :param percent: the percent to determine its letter grade
    :return: the letter grade (rules above)
    """
    percent = float(percent)

    if percent > 100:
        print("too high")
        print("error")
        return "E"
    elif percent < 0:
        process_student_failure()
        return "E"
    elif percent >= 80:
        return "A"
    elif percent >= 65:
        return "B"
    elif percent >= 50:
        return "C"
    else:  # must be 0 - 49
        return "F"


print(get_letter_grade(78))
