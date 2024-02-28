# Authors : Jacob Ardelean, Pongs Phimnualsri, Yu-shiuan Lin

def get_square_numbers_between(first, last):
    """
    Create and return a list of all the square numbers between (and including) first and last.

    Args:
    first (int): The starting number.
    last (int): The ending number.

    Returns:
    list: A list containing all square numbers between first and last.
    """
    # Initialize an empty list to store square numbers
    square_numbers = []

    # Iterate through numbers from 'first' to 'last'
    for num in range(first, last + 1):
        # Check if the number is a perfect square
        if int(num ** 0.5) ** 2 == num:
            # If it is, append it to the list
            square_numbers.append(num)

    # Return the list of square numbers
    return square_numbers


def process_user_input():
    """
    Repeatedly asks the user to enter numbers until they type 0 (zero) to quit.
    Calculates and prints statistics of entered numbers.
    """
    # Initialize an empty list to store entered numbers
    numbers = []

    # Loop indefinitely until user enters 0 to quit
    while True:
        try:
            # Prompt the user to enter a number
            user_input = int(input("Enter a number or 0 to quit: "))

            # If user enters 0, break out of the loop
            if user_input == 0:
                break

            # Add the entered number to the list
            numbers.append(user_input)

        # Handle the case when user enters non-integer input
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    # If no numbers were entered, print a message and return
    if not numbers:
        print("No numbers entered.")
        return

    # Calculate total, maximum, minimum, and average of the entered numbers
    total = 0
    max_number = numbers[0]
    min_number = numbers[0]

    for number in numbers:
        total += number
        if number > max_number:
            max_number = number
        if number < min_number:
            min_number = number

    average = total / len(numbers)

    # Print the statistics
    print("\nStatistics:")
    print("Total numbers entered:", len(numbers))
    print("Sum of numbers:", total)
    print("Average of numbers:", average)
    print("Maximum number:", max_number)
    print("Minimum number:", min_number)


def main():
    """
    Main function to call other functions.
    """
    # Print square numbers between specified ranges
    print("Square numbers between 30 and 222:", get_square_numbers_between(30, 222))
    print("Square numbers between 500 and 611:", get_square_numbers_between(500, 611))

    # Call the function to process user input
    process_user_input()


if __name__ == "__main__":
    main()  # Call the main function if the script is executed directly