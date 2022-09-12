import os
from flask import Flask, jsonify
from sports_leagues.premier_league import get_premier_league

app = Flask(__name__)
env_config = os.getenv("PROD_APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)

@app.route("/api", methods=['GET'])
def api():
	matches = get_premier_league()
	return jsonify(matches)