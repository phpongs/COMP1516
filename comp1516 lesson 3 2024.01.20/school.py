# author: jason wilder

def did_pass(percent):
    """
    Reports whether a percent grade passed or not
    :param percent: the grade to evaluate
    :return: True if and only if the percent >= 50; otherwise False
    """
    if percent >= 50:
        print("you passed")
        print("congratulations")
        return True
    else:
        print("you did not pass")
        print("too bad")
        return False


if not did_pass(-4):
    print("you do not graduate")
