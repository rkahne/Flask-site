from twitter import *
# from fb import *
from bs4 import BeautifulSoup


import re
import urllib.request

# FB_ACCESS_TOKEN = ""

ACCESS_TOKEN="13332732-fetvSVLHreuBMi9tnDmag8trw2W85hRylYUNS1EyP"
ACCESS_SECRET="mzfopDLGvNxUC1ScD65tBcoK4RBIeLHXdlUqXq3vs6oIG"
CONSUMER_KEY="dMHU9UCytSzUPO9OdFH0OuQo5"
CONSUMER_SECRET="Jfj6qOPi6kp3GK11LIDoxnZQeNBK8kNyQvsTrOnHcRcTPxJiCj"

t = Twitter(auth=OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET))
links = []
tweets = t.statuses.user_timeline(screen_name="rkahne")
reg_ex_compiler = re.compile(r'\S+:\S+')

for tweet in range(len(tweets)):
	try:
		url = reg_ex_compiler.search(tweets[tweet]['text'].encode("utf-8").decode('unicode-escape')).group()
		get = urllib.request.urlopen(url)
		html = get.read()
		soup = BeautifulSoup(html, 'html.parser')
		title = soup.find_all('title')[0].encode('unicode-escape')
		title = re.sub(b'</?title>',b'',title).decode('utf-8')
		links.append((title, url))
	except:
		pass

for _ in range(len(links)):
	print("{}. {} ({})".format(_+1,links[_][0],links[_][1]))


