import pandas as pd
import requests
from bs4 import BeautifulSoup
from models.player import Player


def extract_specified(stats, type):
    return stats[0][type].values.tolist()


def crawl(player_name):
    html = requests.get('{}{}'.format(player_id_url, player_name)).text
    soup = BeautifulSoup(html, 'html.parser')
    link = soup.find(property="og:url")


def multiple_players(player_name):
    html = requests.get('{}{}'.format(player_id_url, player_name)).text
    soup = BeautifulSoup(html, 'html.parser')
    link = soup.find(property="og:url")

    if link == None:
        return 'true', soup

    return 'false', soup


def get_bases(player_name):
    html = requests.get('{}{}'.format(player_id_url, player_name)).text
    soup = BeautifulSoup(html, 'html.parser')

    return html, soup


def get_player_list(soup, player_name):
    link = soup.find(property="og:url")
    if link == None:
        ps = pd.read_html('{}{}'.format(player_id_url, player_name))

        rs = soup.select("a[href*=\/nba\/player\/_\/id\/]")

        players = []
        pnames = []
        pids = []
        c = 1
        # extract ids
        for r in rs:
            players.append(Player(r.text, str(r).split('/')[7]))
            # pnames.append(r.text)
            #print('{}. {}'.format(c, r.text))
            # pids.append(str(r).split('/')[7])
            c = c+1

        return players

    pid = str(link).split('/')[7]

    return Player(player_name, pid)


def get_available_players(player_name):
    html = requests.get('{}{}'.format(player_id_url, player_name)).text
    soup = BeautifulSoup(html, 'html.parser')
    link = soup.find(property="og:url")


player_id_url = 'https://www.espn.com/nba/players/_/search/'
player_stats_url = 'https://www.espn.com/nba/player/gamelog/_/id/'
