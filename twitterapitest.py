from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key="dMHU9UCytSzUPO9OdFH0OuQo5"
consumer_secret="Jfj6qOPi6kp3GK11LIDoxnZQeNBK8kNyQvsTrOnHcRcTPxJiCj"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="13332732-fetvSVLHreuBMi9tnDmag8trw2W85hRylYUNS1EyP"
access_token_secret="mzfopDLGvNxUC1ScD65tBcoK4RBIeLHXdlUqXq3vs6oIG"

class StdOutListener(StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['basketball'])