# author: Pongsatorn Phimnualsri

import assignment2
import re


def main():
    """
    Main function to execute following tasks
    - write a list of countries and their capitals to a specified file.
    - saves capitals information
    Returns:

    """
    assignment2.write_countries_capitals_to_file("0123456789.txt")
    assignment2.save_capitals()


if __name__ == '__main__':
    main()
