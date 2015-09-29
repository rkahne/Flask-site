from twitter import *

ACCESS_TOKEN="13332732-fetvSVLHreuBMi9tnDmag8trw2W85hRylYUNS1EyP"
ACCESS_SECRET="mzfopDLGvNxUC1ScD65tBcoK4RBIeLHXdlUqXq3vs6oIG"
CONSUMER_KEY="dMHU9UCytSzUPO9OdFH0OuQo5"
CONSUMER_SECRET="Jfj6qOPi6kp3GK11LIDoxnZQeNBK8kNyQvsTrOnHcRcTPxJiCj"

t = Twitter(auth=OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET))
to_be_printed = str(t.statuses.user_timeline(screen_name="rkahne"))
f = open("json.txt", "w")
try:
	f.write(to_be_printed)
	f.close()
except IOError:
	pass

