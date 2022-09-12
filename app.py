import os
from flask import Flask, jsonify
from sports_leagues.premier_league import get_premier_league
from sports_leagues.nba import get_nba
from pprint import pprint

app = Flask(__name__)
env_config = os.getenv("PROD_APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)

@app.route("/api", methods=['GET'])
def api():
	matches = get_premier_league()
	nba_matches = get_nba()
	# Below pprint demonstrates NBA matches also being pulled through
	# Next steps: concatenate/combine both data sets to form single api and add 40 max pagination for efficient queries.
	pprint(nba_matches)

	return jsonify(matches)