import os
import requests
from pprint import pprint
from dotenv import load_dotenv
load_dotenv()

FOOTBALL_API_KEY = os.getenv("FOOTBALL_API_KEY")
URI = 'https://api.football-data.org/v4/matches'
HEADERS = { 'X-Auth-Token': FOOTBALL_API_KEY }

response = requests.get(URI, headers=HEADERS)
for match in response.json()['matches']:
	pprint(match)