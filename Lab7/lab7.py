# author: Thomas Brock, Yu-shiuan Lin, Pongs Phimnualsri

# dict of sports leagues
sports_leagues = {
    "NFL": "National Football Leagues (American football)",
    "MLB": "Major League Baseball (Baseball)",
    "NBA": "National Basketball Association (Basketball)",
    "EPL": "Premier League (Association football)",
    "NHL": "National Hockey League (Ice hockey)",
    "MLS": "Major League Soccer (Association football)",
    "IPL": "Indian Premier League (Twenty20 cricket)",
    "AFL": "Australian Football League (Australian rules football)",
    "NRL": "National Rugby League (Rugby league football)",
    "CFL": "Canadian Football League (Canadian football)"
}


def delete_league():
    """
    delete a league from the sports_leagues dict based on its abbreviation.
    :return: nothing
    """
    global sports_leagues
    while True:
        league_abbr = input("Enter league abbreviation you want to delete: ").upper()
        if league_abbr == "EXIT":
            print("Exit the delete program.")
            break
        elif league_abbr in sports_leagues:
            league_name = sports_leagues.pop(league_abbr)
            print(f"The {league_name} has been removed.")
        else:
            print(f"There is no league named {league_abbr}.")


def add_league():
    """
    adds a new league to the sports_leagues dict.
    :return: nothing
    """
    global sports_leagues
    while True:
        league_abbr = input("Enter the new league's abbreviation: ").upper()
        if league_abbr == "EXIT":
            print("Exit the add program.")
            break
        elif league_abbr in sports_leagues:
            print(f"{league_abbr} is already listed as the {sports_leagues[league_abbr]}")
        else:
            league_name = input("Enter the full name of the new league: ")
            sports_leagues[league_abbr] = league_name
            print(f"{league_abbr} added as the {league_name}")


def get_abbreviation():
    """
    return a list of all sports_leagues keys.
    """
    return list(sports_leagues.keys())


def get_league_description():
    """
    return a tuple of all sports_leagues values.
    """
    return tuple(sports_leagues.values())


def get_league_abbreviations_and_descriptions():
    """
    return a set of all sports_leagues keys and values.
    """
    return set(sports_leagues.items())
