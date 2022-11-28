import json

from flask import Flask, jsonify, redirect, url_for

from app.espn_scraper_rest import get_player_list, get_html_elements
from models.player import Player


app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('status'))


@app.route('/status')
def status():
    return jsonify({'status': 'server is running'})


@app.route('/nba/player/<player_name>', methods=['GET'])
def get_players(player_name):
    html, soup = get_html_elements(player_name)
    players = get_player_list(soup=soup, player_name=player_name)
    json_data = json.dumps(players, default=lambda p: p.__dict__)
    return jsonify(json.loads(json_data))


app.run(port=8000)
