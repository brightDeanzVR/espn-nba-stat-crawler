import pandas as pd
import requests
from bs4 import BeautifulSoup
from models.player import Player


def extract_specified(stats, type):
    return stats[0][type].values.tolist()


def query_player_stats(player_id):
    stats = pd.read_html('{}{}'.format(player_stats_url, player_id))
    reb = extract_specified(stats, 'REB')
    ast = extract_specified(stats, 'AST')
    pts = extract_specified(stats, 'PTS')
    return reb, ast, pts


def get_html_elements(player_name):
    html = requests.get('{}{}'.format(player_id_url, player_name)).text
    soup = BeautifulSoup(html, 'html.parser')

    return html, soup


def get_player_list(soup, player_name):
    link = soup.find(property="og:url")
    players = []
    if link == None:
        ps = pd.read_html('{}{}'.format(player_id_url, player_name))

        rs = soup.select("a[href*=\/nba\/player\/_\/id\/]")

        c = 1

        for r in rs:
            players.append(Player(r.text, str(r).split('/')[7]))
            c = c+1

        return players

    pid = str(link).split('/')[7]

    return players.append(Player(player_name, pid))


player_id_url = 'https://www.espn.com/nba/players/_/search/'
player_stats_url = 'https://www.espn.com/nba/player/gamelog/_/id/'
