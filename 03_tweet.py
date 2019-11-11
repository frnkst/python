# Tweet from the command line
# Usage: python3 03_tweet.py "I love python #everyday_python"

from twitter import *
import configparser
import sys

config = configparser.ConfigParser()
config.read('twitter-oauth.ini')
oauth = config['oauth']

t = Twitter(auth=OAuth(
    oauth['token'],
    oauth['token_secret'],
    oauth['consumer_key'],
    oauth['consumer_secret'],
))
t.statuses.update(status=sys.argv[1])
