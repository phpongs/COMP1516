# Author: Jacob Ardelean

import data  # Importing the data module


def print_json_countries_and_capitals():
	"""
	Print a JSON representation of countries and their capitals.
	:returns: function iterates through the list of countries and their capitals
	and prints a JSON object for each pair in the format.
	"""
	print("[")
	for i in range(len(data.countries_and_capitals)):
		country, capital = data.countries_and_capitals[i]
		if i < len(data.countries_and_capitals) - 1:
			print('\t{\n\t\t"country_name" : "%s",\n\t\t"capital_city" : "%s"\n\t},' % (country, capital))
		else:
			print('\t{\n\t\t"country_name" : "%s",\n\t\t"capital_city" : "%s"\n\t}' % (country, capital))
	print("]")


def get_list_of_countries_whose_nth_letter_is(n, letter):
	"""
	Gets a list of countries whose nth letter is the specified letter.
	:arg:n (int): The position of the letter in the country's name.
	letter (str): The letter to match.
	:returns:list: A list of country names.
	"""
	countries_whose_nth_letter = []
	for country in data.countries:
		if len(country) >= n and country[n - 1].lower() == letter.lower():
			countries_whose_nth_letter.append(country)
	return countries_whose_nth_letter


def get_funny_case_capital_cities(letter):
	"""
	Get a list of capital cities with a funny case involving the specified letter.
	:arg:
		letter (str): The letter to find in capital city names.
	:returns:
		list: A list of capital city names with funny casing.
	"""
	funny_capital_cities = []
	for capital in data.capitals:
		if letter.lower() in capital.lower():
			funny_city = ""
			for i in range(len(capital)):
				current_character = capital[i].lower()
				letter_lower = letter.lower()
				if current_character == letter_lower:
					funny_city += current_character
				elif (i > 0 and capital[i - 1].lower() == letter_lower) or (
						i < len(capital) - 1 and capital[i + 1].lower() == letter_lower):
					funny_city += capital[i].upper()
				else:
					funny_city += capital[i].lower()
			funny_capital_cities.append(funny_city)
	return funny_capital_cities


def get_doubled_letter_countries():
	"""
	Get a tuple of countries where a letter is doubled.
	:returns:tuple: A tuple containing country names where a letter is doubled.
	"""
	doubled_letter_with_countries = []
	for country in data.countries:
		for i in range(len(country) - 1):
			if country[i].lower() == country[i + 1].lower():
				doubled_letter_with_countries.append((country[i].lower(), country))
				break
	doubled_letter_with_countries.sort()
	double_letters_countries = []
	for i in doubled_letter_with_countries:
		double_letters_countries.append(i[1])
	return tuple(double_letters_countries)


def main():
	"""
	The main function of the script.
	"""
	print("This file should not be called.")


if __name__ == '__main__':
	main()
