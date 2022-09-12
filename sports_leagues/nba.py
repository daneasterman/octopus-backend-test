import os
import requests
from collections import defaultdict
from pprint import pprint

def get_nba():
	BASE_URI = "https://www.balldontlie.io/api/v1/games"
	SEASON = 2020
	# Total Regular Season Games:
	MAX_RESULTS = 82
	FULL_NBA_URI = f"{BASE_URI}?seasons[]={SEASON}&per_page={MAX_RESULTS}"
	
	response = requests.get(FULL_NBA_URI).json()
	matches_dict = defaultdict(list)
	for match in response['data']:
		match = {
			"home_team": {
				"full_name": match["home_team"]["full_name"],
				"score": match["home_team_score"]
			},
			"away_team": {
				"full_name": match["visitor_team"]["full_name"],
				"score": match["visitor_team_score"]
			},
			"date": match["date"]
		}
		matches_dict["nba_matches"].append(match)
	return matches_dict

# get_nba()

