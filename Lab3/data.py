# author: Pongsatorn Phimnualsri, Alexandra Wine

'''
Create a date.py script with variables,. Also create a function named
get_day_of_the_week(month, day, year), which has three arguments: month, day,
and year. This function calculates and returns the name of the day of the week for
that month, day, and year. For example, calling the function this way would return
“Sunday”:
get_day_of_the_week(12, 25, 2022)

Implement this algorithm:
It must make use of another method that you must write:
is_leap_year(year) (see: http://en.wikipedia.org/wiki/Leap_year)
Which returns True (e.g. for 1996, 2000, 2012, 2016 etc) or false (e.g. for 1900, 2031,
etc) depending on whether the year argument is a leap year.

Here is the algorithm to determine what day of the week a given date is:
Example dates: August 16, 1989 and March 20, 1950
Step 1: Only look at the last two digits of the year and determine how many 12s fit in it
Step 2: Look at the remainder of this division:
Step 3: How many 4s fit into that remainder:
Step 4: Add the day of the month:
Step 5: Add the month code:
    Jan = 1 Feb = 4 Mar = 4
    Apr = 0 May = 2 Jun = 5
    Jul = 0 Aug = 3 Sep = 6
    Oct = 1 Nov = 4 Dec = 6
Step 6: Add all of the above numbers, then mod by 7:

This is your day of the week, as follows:
Sat = 0 Sun = 1 Mon = 2 Tue = 3 Wed = 4 Thu = 5 Fri = 6

NOTE: some dates require special offsets:
January and February dates in leap years: add 6 to step 5
Dates in the 1600s: add 6 to step 5
Dates in the 1700s: add 4 to step 5
Dates in the 1800s: add 2 to step 5
Dates in the 2000s: add 6 to step 5
Dates in the 2100s: add 4 to step 5
'''


def is_leap_year(year):
    """
    use to check if a year is a leap year
    :param year: the year to check
    :return: true if the year is leap, false if the year is not a leap year
    """
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False


def get_day_of_the_week(month, day, year):
    """
    calculate and returns the name of the day of the week for that month, day, and year
    :param month: month input by user
    :param day: day input by user
    :param year: year input by user
    :return: name of the days of the week
    """

    # step 1: only look at the last two digits of the year and determine how many 12s fit in it.
    year_two_digits = year % 100
    twelves_floor_division = year_two_digits // 12

    # step 2: look at the remainder of this division.
    twelves_remainder = year_two_digits % 12

    # step 3: how many 4s fit into that remainder.
    four_floor_division = twelves_remainder // 4

    # step 4: add the day of the month.
    day_of_month = day

    # step 5: add the month code.
    if month == 1:
        month_code = 1
    elif month == 2:
        month_code = 4
    elif month == 3:
        month_code = 4
    elif month == 4:
        month_code = 0
    elif month == 5:
        month_code = 2
    elif month == 6:
        month_code = 5
    elif month == 7:
        month_code = 0
    elif month == 8:
        month_code = 3
    elif month == 9:
        month_code = 6
    elif month == 10:
        month_code = 1
    elif month == 11:
        month_code = 4
    elif month == 12:
        month_code = 6
    else:   # Invalid month number
        print('Invalid month number')

    # special offsets for step 5
    # this 'if' use for check only January and February in the leap years
    if is_leap_year(year) and (month == 1 or month == 2):
        month_code += 6

    # this 'if' use for check the whole year
    if 1600 <= year < 1700:
        month_code += 6
    elif 1700 <= year < 1800:
        month_code += 4
    elif 1800 <= year < 1900:
        month_code += 2
    elif 2000 <= year < 2100:
        month_code += 6
    elif 2100 <= year < 2200:
        month_code += 4

    # step 6: add all of above numbers, then mod by 7
    day_of_week = (twelves_floor_division + twelves_remainder + four_floor_division + day_of_month + month_code) % 7
    if day_of_week == 0:
        return 'Saturday'
    elif day_of_week == 1:
        return 'Sunday'
    elif day_of_week == 2:
        return 'Monday'
    elif day_of_week == 3:
        return 'Tuesday'
    elif day_of_week == 4:
        return 'Wednesday'
    elif day_of_week == 5:
        return 'Thursday'
    elif day_of_week == 6:
        return 'Friday'
    else:   # Invalid Value
        print('Invalid value')


def main():
    """
    test cases
    :return: true if all above code are correct, false if there are something wrong with the code
    """
    print("Sunday" == get_day_of_the_week(12, 25, 2022))
    print("Friday" == get_day_of_the_week(8, 26, 2022))
    print("Thursday" == get_day_of_the_week(10, 5, 1972))
    print("Wednesday" == get_day_of_the_week(2, 3, 2016))
    print("Monday" == get_day_of_the_week(12, 18, 1899))


if __name__ == "__main__":
    main()
