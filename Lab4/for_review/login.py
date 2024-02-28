# author: Pongsatorn Phimnualsri, Thomas

def generate_password(fname, lname, bcit_id):
    """
    Generate a password from user info
    The password is generated as follows:
    - Get the first three letters from a properly-formatted first name;
    if the first name length is less than three characters then the entire name will be used (e.g. Tig).
    - Get the first three characters from a properly-formatted last name;
    if the last name length is less than three characters then the entire last name will be used (e.g. Woo).
    - Get the last three characters of the BCIT ID
    ; if the BCIT ID length is less than three characters then the entire ID will be used (e.g. 123).
    - Concatenate the characters generated from the above instructions as follows:
    (Characters from the first name + characters from the last name + characters from BCIT ID) (e.g. TigWoo123)

    :param fname: First name
    :type fname: str
    :param lname: Last name
    :type lname: str
    :param bcit_id: BCIT ID
    :type bcit_id: srt
    :return: Generated password by concatenate the above method
    :rtype:
    """
    fname = str.capitalize(fname)
    lname = str.capitalize(lname)

    # Get first 3 letters of first name. If name less than 3 letters, get all
    if len(fname) >= 3:
        fchars = fname[0:3]
    else:
        fchars = fname

    # Get first 3 letters of last name. If name less than 3 letters, get all
    if len(lname) >= 3:
        lchars = lname[0:3]
    else:
        lchars = lname

    # Get last 3 letters of BCIT ID. If ID less than 3 letters, get all
    if len(bcit_id) >= 3:
        idchars = bcit_id[-3:]
    else:
        idchars = bcit_id

    # concatenate the characters together as a default password
    # Characters from the first name + characters from the last name + characters from BCIT ID
    password = f"{fchars}{lchars}{idchars}"
    return password


def has_7_chars(pw):
    """
    Validation if the password meets requirement
    - The password must be at least seven characters long
    :param pw: New Password input by user
    :type pw: str
    :return: If meets requirement return True, If not meets requirement return False
    :rtype: bool
    """
    if len(pw) >= 7:
        return True
    else:
        return False


def has_upper(pw):
    """
    Validation if the password meets requirement
    - The password must contain at least one uppercase character
    :param pw: New Password input by user
    :type pw: str
    :return: If meets requirement return True, If not meets requirement return False
    :rtype: bool
    """
    for char in pw:
        if char.isupper():
            return True
    return False


def has_lower(pw):
    """
    Validation if the password meets requirement
    - The password must contain at least one lowercase character
    :param pw: New Password input by user
    :type pw: str
    :return: If meets requirement return True, If not meets requirement return False
    :rtype: bool
    """
    for char in pw:
        if char.islower():
            return True
    return False


def has_digit(pw):
    """
    Validation if the password meets requirement
    - The password must contain at least one digit
    :param pw: New Password input by user
    :type pw: str
    :return: If meets requirement return True, If not meets requirement return False
    :rtype: bool
    """
    for char in pw:
        if char.isdigit():
            return True
    return False


def change_password():
    """
    Repeatedly (i.e. in a loop) prompt the user to enter a new password.
    If the password meets the specifications, the loop terminates and the password is returned
    ; otherwise a message including the password specifications and a request to enter another password
    will be displayed and the user will be prompted to enter another password.
    :return: New Password if every requirement is pass
    :rtype: str
    """
    while True:
        pw = input("Enter a new password: ")

        if has_7_chars(pw) and has_upper(pw) and has_lower(pw) and has_digit(pw):
            return pw

        if not has_7_chars(pw):
            print("Password must be at least 7 characters long.")

        if not has_upper(pw):
            print("Password must contain at least one uppercase character.")

        if not has_lower(pw):
            print("Password must contain at least one lowercase character.")

        if not has_digit(pw):
            print("Password must contain at least one digit.")
