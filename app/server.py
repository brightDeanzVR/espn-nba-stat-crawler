import json

from flask import Flask, jsonify, redirect, url_for

from app.espn_scraper_rest import get_player_list, get_html_elements, query_player_stats


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
    found_soup = soup
    players = get_player_list(soup=soup, player_name=player_name)
    json_data = json.dumps(players, default=lambda p: p.__dict__)
    return jsonify(json.loads(json_data))


@app.route('/nba/player/<player_id>/stats')
def get_player_stats(player_id):
    rebs, asts, pts = query_player_stats(player_id)
    json_data = json.dumps([{'Rebounds': json.dumps(rebs)}, {
                           'Assists': json.dumps(asts)}, {'Points': json.dumps(pts)}])

    return jsonify(json.loads(json_data))
