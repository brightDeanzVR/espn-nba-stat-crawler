import pandas as pd
import requests
from bs4 import BeautifulSoup

def get_player_list(soup, player_name):
	ps = pd.read_html('{}{}'.format(player_id_url,player_name))
	
	rs = soup.select("a[href*=\/nba\/player\/_\/id\/]")

	pnames = []
	pids = []
	c = 1
	#extract ids
	for r in rs:

		pnames.append(r.text)
		print('{}. {}'.format(c,r.text))
		pids.append(str(r).split('/')[7])
		c = c+1


	index = int(input('Select player: '))
	index = index - 1
	stats = pd.read_html('{}{}'.format(player_stats_url, pids[index]))
	reb = stats[0]["REB"]
	ast = stats[0]["AST"]
	pts = stats[0]["PTS"]
	return pids[index],pnames[index],reb,ast,pts

def get_player_stats(soup):
	link = soup.find(property="og:url")
	pid = str(link).split('/')[7]
	stats = pd.read_html('{}{}'.format(player_stats_url, pid))
	reb = stats[0]["REB"]
	ast = stats[0]["AST"]
	pts = stats[0]["PTS"]
	return pid,reb,ast,pts

player_id_url = 'https://www.espn.com/nba/players/_/search/'
player_stats_url = 'https://www.espn.com/nba/player/gamelog/_/id/'


def crawl():
	player_name = input('Enter player name: ')

	html = requests.get('{}{}'.format(player_id_url, player_name)).text
	soup = BeautifulSoup(html, 'html.parser')
	link = soup.find(property="og:url")
	if link == None :
		player_id,player_name,rebounds,assists,points = get_player_list(soup, player_name)
		print('Showing results for {} with id {}...'.format(player_name, player_id))
		print(rebounds)
		print(assists)
		print(points)

	else: 
		get_player_stats(soup)
		player_id,rebounds,assists,points = get_player_stats(soup)
		print('Showing results for {} with id {}...'.format(player_name, player_id))
		print(rebounds)
		print(assists)
		print(points)

if __name__ == '__main__':
	crawl()














