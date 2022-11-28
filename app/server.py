import json

from flask import Flask, jsonify, redirect, url_for
from app.espn_scraper import crawl_rest
from app.espn_scraper_rest import multiple_players, get_player_list, get_bases
from models.player import Player


app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('status'))


@app.route('/status')
def status():
    return jsonify({'status': 'server is running'})


@app.route('/nba/<player_name>/multiple')
def player_count(player_name):
    b, soup = multiple_players(player_name=player_name)
    global_soup = soup
    return b


@app.route('/nba/player/<player_name>', methods=['GET'])
def get_players(player_name):
    html, soup = get_bases(player_name)
    players = get_player_list(soup=soup, player_name=player_name)
    json_data = json.dumps(players, default=lambda p: p.__dict__)
    return jsonify(json.loads(json_data))


global_soup = ''

app.run(port=8000)
