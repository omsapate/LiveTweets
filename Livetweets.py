from tweepy import OAuthHandler, Stream
from tweepy.streaming import StreamListener
import json
import sys
import time

class LiveTweets(StreamListener):
	def on_data(self, data):
		tweet = json.loads(data)
		print(tweet)
		print()
		time.sleep(3)
	def on_error(self,status):
		print(status)
		print()

auth = []

f =open('auth','r')

for line in f:
	auth.append(line.strip())
f.close()

try:
	listener = LiveTweets()
	auth_key = OAuthHandler(auth[0],auth[1])
	auth_key.set_access_token(auth[2],auth[3])
	live_stream = Stream(auth_key,listener)
	live_stream.filter(track=[input('Enter Keyword: ')])
except KeyboardInterrupt:
	sys.exit()