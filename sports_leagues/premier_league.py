import os
import requests
from collections import defaultdict
from pprint import pprint
from dotenv import load_dotenv
load_dotenv()

def get_premier_league():
	FOOTBALL_API_KEY = os.getenv("FOOTBALL_API_KEY")	
	HEADERS = { 'X-Auth-Token': FOOTBALL_API_KEY }
	BASE_URI = "https://api.football-data.org/v4"
	# Hardcode Premier League competition ID for now. To Do: extract ID from /matches endpoint to avoid future breaking changes.
	PREM_LEAGUE_ID = 2021
	# The API takes 2020 as start of 20/21 season.
	SEASON = 2020
	# Hardcode total number of league games for now:
	MAX_RESULTS = 38
	PREM_LEAGUE_URI = f"{BASE_URI}/competitions/{PREM_LEAGUE_ID}/matches?season={SEASON}&limit={MAX_RESULTS}"

	response = requests.get(PREM_LEAGUE_URI, headers=HEADERS).json()

	matches_dict = defaultdict(list)
	for match in response['matches']:
		match = {
			"home_team": {
				"full_name": match["homeTeam"]["name"],
				"score": match["score"]["fullTime"]["home"]
			},
			"away_team": {
				"full_name": match["awayTeam"]["name"],
				"score": match["score"]["fullTime"]["away"]
			},
			"date": match["utcDate"]
		}
		matches_dict["matches"].append({"match": match})
	pprint(matches_dict)

get_premier_league()
	