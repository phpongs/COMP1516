# author: Thomas Brock and Pongsatorn Phimnualsri

def generate_password(first_name, last_name, bcit_id):
    """
    Generates a computer generated password based on three inputs.
    The password is generated as follows:
    - Get the first three letters from a properly-formatted first name;
    if the first name length is less than three characters then the entire name will be used (e.g. Tig).
    - Get the first three characters from a properly-formatted last name;
    if the last name length is less than three characters then the entire last name will be used (e.g. Woo).
    - Get the last three characters of the BCIT ID
    ; if the BCIT ID length is less than three characters then the entire ID will be used (e.g. 123).
    - Concatenate the characters generated from the above instructions as follows:
    (Characters from the first name + characters from the last name + characters from BCIT ID) (e.g. TigWoo123)
    :param first_name: First name
    :param last_name: Last name
    :param bcit_id: BCIT ID
    :return: Generated password by concatenate the above method
    """
    first_name = str.capitalize(first_name)
    last_name = str.capitalize(last_name)
    bcit_id = str(bcit_id)

    # Password use the first 3 characters of each input
    password = first_name[0:3].capitalize() + last_name[0:3].capitalize() + bcit_id[-3:].upper()
    return password


def has_upper(password):
    """
    Determines if the new password has at least one uppercase character.
    :param password: New Password input by user
    :return: If meets requirement return True, If not meets requirement return False
    """
    i = 0
    while i < len(password):
        if password[i].isupper():
            return True
        i += 1
    return False


def has_lower(password):
    """
    Determines if the new password has at least one lowercase character.
    :param password: New Password input by user
    :return: If meets requirement return True, If not meets requirement return False
    """
    i = 0
    while i < len(password):
        if password[i].islower():
            return True
        i += 1
    return False


def has_digit(password):
    """
    Determines if the new password has at least one numeric character.
    :param password: New Password input by user
    :return: If meets requirement return True, If not meets requirement return False
    """
    i = 0
    while i < len(password):
        if password[i].isdigit():
            return True
        i += 1
    return False


def change_password():
    """
    Repeatedly (i.e. in a loop) prompt the user to enter a new password.
    If the password meets the specifications, the loop terminates and the password is returned
    ; otherwise a message including the password specifications and a request to enter another password
    will be displayed and the user will be prompted to enter another password.
    :return: New Password if every requirement is pass
    """
    while True:
        password = input("Enter a new password: ")

        # check length

        
        if len(password) < 7:
            print("Password must be at least 7 characters long.")
            continue

        # check for an uppercase character
        elif not has_upper(password):
            print("Password must contain at least one uppercase character.")

        #  check for a lowercase character
        elif not has_lower(password):
            print("Password must contain at least one lowercase character.")

        # check for a numeric character
        elif not has_digit(password):
            print("Password must contain at least one digit.")

        else:
            return password

# This ends the file
