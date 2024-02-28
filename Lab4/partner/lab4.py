# author: Pongsatorn Phimnualsri, Thomas

import login


def main():
    """
    Prompt the user to enter their first name, last name, and BCIT ID
    - Create the default password by passing those values to the generate_password () function, and display the result.
    - Call the change_password() function to prompt the user to change the default password.
    - Display the password generated by the change_password() function.
    :return: None
    :rtype: None
    """
    first_name = input("enter your first name: ")
    last_name = input("enter your last name: ")
    bcit_id = input("enter your BCIT ID: ")

    # Generate default password
    pw = login.generate_password(first_name, last_name, bcit_id)
    print(f"Your generated password is: {pw}")

    # Change password
    pw = login.change_password()
    print(f"Password changed! your new password is: {pw}")


if __name__ == "__main__":
    main()