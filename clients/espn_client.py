'''
espn_client is the series of functions required to pull ESPN api data for current players and their performance stats,
collating them by team
'''

# todo mock manager in populate_dataset to read from a local testing dataset

_SEASON_PLAYER_STATS_URL = "sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/{YEAR}/athletes/{ATHLETE_ID}/eventlog"
_SEASON_PLAYERS_ON_TEAM_URL = "sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/{YEAR}/teams/{TEAM_ID}"
_TEAMS_URL = "https://site.api.espn.com/apis/site/v2/sports/football/nfl/teams"

class espn_client:
    def __init__(self):
        return # todo

    def populate_dataset(self):
        '''
        calls underlying data to create a full csv loaded into a pandas dataframe
        for up-to-date data; avoids duplicated calls by initializing from stored csv, if present,
        and deleting out-of-date data
        '''
        return # todo

    def __get_locally_stored_data(self):
        return # todo

    def __get_team_data(self):
        return # todo

    def __get_players_on_all_teams_data(self, teamIds: list[str]):
        return # todo

    def __get_player_season_stats(self, playerId: str):
        return # todo
