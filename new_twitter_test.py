from twitter import *
# from fb import *
from bs4 import BeautifulSoup


import re
import urllib.request

# FB_ACCESS_TOKEN = "..."

ACCESS_TOKEN="..."
ACCESS_SECRET="..."
CONSUMER_KEY="..."
CONSUMER_SECRET="..."


t = Twitter(auth=OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET))
links = []
tweets = t.statuses.user_timeline(screen_name="rkahne")
reg_ex_compiler = re.compile(r'https?:\S+[^\u2026]')

for tweet in range(len(tweets)):
	try:
		url = reg_ex_compiler.search(tweets[tweet]['text'].encode("utf-8").decode('unicode-escape')).group()
		get = urllib.request.urlopen(url)
		html = get.read()
		soup = BeautifulSoup(html, 'html.parser')
		links.append(soup.find_all('title')[0])
	except:
		pass

for _ in range(len(links)):
	try:
		print("{}. {}".format(_,links[_]))
	except:
		pass


