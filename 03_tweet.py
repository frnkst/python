# Tweet from the command line
# Usage: python3 03_tweet.py "I love python #everyday_python"

from twitter import *
import configparser
import sys

config = configparser.ConfigParser()
config.read('twitter-oauth.ini')

t = Twitter(auth=OAuth(
    config['oauth']['token'],
    config['oauth']['token_secret'],
    config['oauth']['consumer_key'],
    config['oauth']['consumer_secret'],
))
t.statuses.update(status=sys.argv[1])
