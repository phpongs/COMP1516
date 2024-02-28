# authors: Thomas Brock and Pong Phimnualsri

def generate_password():
    """
    Generates a computer generated password based on three inputs.
    :return: password based on three variable inputs
    """

    # Variable Inputs, use the first 3 characters of each input
    first_name = input("What is your first name?:\n")
    last_name = input("What is your last name?:\n")
    bcit_id = str(input("What is your BCIT ID#?:\nStart with the letter A\n"))

    password = first_name[:3].capitalize() + last_name[:3].capitalize() + bcit_id[-3:].upper()
    print("Your login is ", password)


def has_upper(new_password):
    """
    Determines if the new password has at least one uppercase character.
    :param new_password: New inputted password
    :return: True/False
    """
    i = 0
    while i < len(new_password):
        if new_password[i].isupper():
            return True
        i += 1
    return False


def has_lower(new_password):
    """
    Determines if the new password has at least one lowercase character.
    :param new_password: New inputted password
    :return: True/False
    """
    i = 0
    while i < len(new_password):
        if new_password[i].islower():
            return True
        i += 1
    return False


def has_digit(new_password):
    """
    Determines if the new password has at least one numeric character.
    :param new_password: New inputted password
    :return: True/False
    """
    i = 0
    while i < len(new_password):
        if new_password[i].isdigit():
            return True
        i += 1
    return False


def change_password():
    """
    Requires the user to change the default password to a new password. The program ends when the password is accepted.
    :return: Re-enter password until accepted. Print and return new password.
    """
    while True:
        new_password = str(input("Enter a new password:\n"))

        # check length
        if len(new_password) < 7:
            print("Password must be at least 7 characters long and contain one uppercase character, "
                  "one lower case character, and one number")
            continue

        # check for an uppercase character
        elif not has_upper(new_password):
            print("Password must be at least 7 characters long and contain one uppercase character, "
                  "one lower case character, and one number")

        # check for a lowercase character
        elif not has_lower(new_password):
            print("Password must be at least 7 characters long and contain one uppercase character, "
                  "one lower case character, and one number")

        # check for a numeric character
        elif not has_digit(new_password):
            print("Password must be at least 7 characters long and contain one uppercase character, "
                  "one lower case character, and one number")

        else:
            print("Your password is " + new_password)
            return new_password


# This ends the file
