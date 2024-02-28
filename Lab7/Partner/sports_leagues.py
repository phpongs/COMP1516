# author: Thomas Brock, Pongs Phimnualsri, Yu-shiuan Lin


# key then value - must use upper case for keys
sports_leagues = {"NFL": "National Football League (American Football)",
                  "MLB": "Major League Baseball (Baseball)",
                  "NBA": "National Basketball Association (Basketball)",
                  "EPL": "Premier League (Association Football)",
                  "NHL": "National Hockey League (Ice Hockey)",
                  "MLS": "Major League Soccer (Association Football)",
                  "IPL": "Indian Premier League (Twenty20 Cricket)",
                  "AFL": "Australian Football League (Australian Rules Football)",
                  "NRL": "National Rugby League (Rugby League Football)",
                  "CFL": "Canadian F`ootball League (Canadian Football)"}


def delete_league():
    """
    Delete the inputted league from the dictionary, if it exists.
    :print: the league has been removed or it does not exist.
    """
    global sports_leagues
    # Choose the league to delete
    # if it exists (ignore case), remove the league
    # otherwise print there is no league
    # use QUIT or EXIT to leave the loop
    while True:
        league_key = input("Enter the league abbreviation to be deleted: ")
        if league_key.upper() in sports_leagues:
            league_deleted = sports_leagues.pop(league_key.upper())
            print(f"The {league_deleted} has been removed.")
        elif league_key.upper() == "QUIT" or league_key.upper() == "EXIT":
            return
        else:
            print(f"There is no league named {league_key}.")


def add_league():
    """
    Takes user's input and adds the key to the sports_leagues dictionary.
    If the input(key) already exists, prints an error message for the user.
    :return: add the key to the dictionary
    """
    global sports_leagues
    # Choose the league key to add - 3 characters
    # if it is not 3 characters - restart
    # if it matches another key (ignore case) - restart
    # enter the league description
    # use QUIT or EXIT to leave the loop
    while True:
        add_key = input("Enter the three character abbreviation for the new league: ")
        add_key = add_key.upper()
        if add_key == "QUIT" or add_key == "EXIT":
            break
        elif len(add_key) != 3:
            print("The key must be exactly 3 characters. Please re-enter the key")
            continue
        elif add_key in sports_leagues:
            print(f"{add_key} is already listed as the {sports_leagues[add_key]}")
        else:
            add_value = input("Enter the description for the new league: ")
            sports_leagues[add_key] = add_value  # add the inputted key: value to the sports_leagues dictionary
            return


def get_abbreviations():
    """
    Creates and returns a list of all sports_leagues keys.
    :return: list of sports_leagues keys
    """
    abbreviation_list = list(sports_leagues.keys())
    abbreviation_list = sorted(abbreviation_list)
    return abbreviation_list


def get_league_descriptions():
    """
    Creates and returns a tuple of all sports_leagues values.
    :return: tuple of sports_leagues values
    """
    league_values = tuple(sports_leagues.values())
    league_values = sorted(league_values)
    return league_values


def get_league_abbreviations_and_descriptions():
    """
    Creates and returns a set of all sports_leagues keys and values.
    :return: set of sports_leagues keys and values
    """
    return set(sports_leagues.items())


# end of file
