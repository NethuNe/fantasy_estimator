# Fantasy Point Estimator

The Fantasy point estimator sources NFL data for the last aggregated season (17 games) of production for a player based on runtime,
adjusts their average stats against estimated defensive efficacy, and outputs a CSV of player -> expected fantasy points for all offensive
players in the pulled dataset + aggregate defense.

Eventually will take into account injury reports and recency bias, but learning has to happen before that can.

player stats for each game in a given season: sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/{YEAR}/athletes/{ATHLETE_ID}/eventlog
(so can get this season & last season and drop the first n games from last season to make an 'aggregate' season; ignore post szn for now)

players on given team in given year: sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/{YEAR}/teams/{TEAM_ID}

team id / dereference info https://site.api.espn.com/apis/site/v2/sports/football/nfl/teams

first step: get team data, throw it in a id -> name map & an id -> []player, populate []player with the result of the player stats call.
can scrape player ids from the reference url in the players-on-given-team call.

there's gonna be a ton of duplicated calls, so being able to save/store data and update it based on when it was created versus now would be ideal
