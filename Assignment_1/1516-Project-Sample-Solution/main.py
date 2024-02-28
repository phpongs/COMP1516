
from data import countries_and_capitals, countries, capitals
import project
import string


def main():
    """
    Run all functions of Assignment 1.
    :return: nothing
    """

    # Print countries and capitals to json.
    project.print_json_countries_and_capitals()

    # Create list of vowels
    vowels_list = ['a', 'e', 'i', 'o', 'u']
    # Find countries where each letter in the list is at each position from 1 to 3.
    # Loop from 1 to 3 and through each of the 5 vowels for each number (total of 15 loops).
    for n in range(1, 4):
        for letter in vowels_list:
            print(project.get_list_of_countries_whose_nth_letter_is(n, letter))

    # Create alphabet list.
    alphabet_list = list(string.ascii_lowercase)
    # Print cities with funny case letters for each letter of the alphabet list.
    for letter in alphabet_list:
        print(project.get_funny_case_capital_cities(letter))

    # Print countries with doubled letters.
    print(project.get_doubled_letter_countries())


if __name__ == '__main__':
    main()

