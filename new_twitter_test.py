from twitter import *
# from fb import *
from bs4 import BeautifulSoup


import re
import urllib.request

# FB_ACCESS_TOKEN = "CAACEdEose0cBAKF5J0iWFVKkmVgcdsvw3Y5g0Lu3kZAtRmaLXr0XUrXOi76zCnNRfufwdYmrl8YcNkLXYmRcb7yKPrJsZAdUWuDNmZAy7koKArRpqksMzWeEAusiZAH37Dr30Ji9Oy8So33jPVHu0hs6TlrMvvrR8NvjIEl2nLWXdQqlf8YwK7GACIZCII1EjVzS2cZAJrwCkMCfOz7o5M"

ACCESS_TOKEN="13332732-fetvSVLHreuBMi9tnDmag8trw2W85hRylYUNS1EyP"
ACCESS_SECRET="mzfopDLGvNxUC1ScD65tBcoK4RBIeLHXdlUqXq3vs6oIG"
CONSUMER_KEY="dMHU9UCytSzUPO9OdFH0OuQo5"
CONSUMER_SECRET="Jfj6qOPi6kp3GK11LIDoxnZQeNBK8kNyQvsTrOnHcRcTPxJiCj"


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


