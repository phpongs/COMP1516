# authors: Thomas Brock and Pong Phimnualsri

import login

# function list
def main():
    """
    Prompts user to enter their first name, last name, and BCIT ID.
    Creates the default password and prompts user to change their password.
    :return: display new password
    """
    # Generates default password
    login.generate_password()
    # Changes password
    login.change_password()


if __name__ == "__main__":
    main()
