# author: Pongsatorn Phimnualsri

from data import countries_and_capitals, countries, capitals
import project


def main():
    """
    main function of the program
    """
    print("--- Print countries and capitals in JSON format ---")
    project.print_json_countries_and_capitals()
    print("---")

    print("\n--- Print list of countries that contain 'a', 'e', 'i', 'o', 'u' at 1st 2nd and 3rd letter ---")
    for n in range(1, 4):
        for letter in ['a', 'e', 'i', 'o', 'u']:
            print(project.get_list_of_countries_whose_nth_letter_is(n, letter))
    print("---")

    print("\n--- Print list of capital cities name in funny logic, from a - z ---")
    for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
        print(project.get_funny_case_capital_cities(letter))
    print("---")

    print("\n--- Print tuple of countries with doubled letter in name ---")
    print(project.get_doubled_letter_countries())
    print("---")


if __name__ == '__main__':
    main()
