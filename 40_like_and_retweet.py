# Set the 4 environment variables CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

import os
import tweepy
import logging
from random import randint
from time import sleep

USER_ID = 2715046843
SLEEP_TIME_MAX = 300

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


class LikeAndRetweetListener(tweepy.StreamListener):
  def __init__(self, api):
    self.api = api
    self.me = api.me()

  def on_status(self, tweet):
    if tweet.in_reply_to_status_id is None and tweet.user.id == USER_ID:
      sleep(randint(1, SLEEP_TIME_MAX))
      logger.info(f"Processing tweet ({tweet.id})")
      like_and_retweet(tweet)

  def on_error(self, status):
    logger.error(status)


def like_and_retweet(tweet):
  if not tweet.favorited:
    try:
      logger.info("Like!")
      tweet.favorite()
    except Exception as e:
      logger.error("Error on like", exc_info=True)
  if not tweet.retweeted:
    try:
      logger.info("Retweet!")
      tweet.retweet()
    except Exception as e:
      logger.error("Error on retweet", exc_info=True)


def create_api():
  consumer_key = os.getenv("CONSUMER_KEY")
  consumer_secret = os.getenv("CONSUMER_SECRET")
  access_token = os.getenv("ACCESS_TOKEN")
  access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)
  api = tweepy.API(auth, wait_on_rate_limit=True,
                   wait_on_rate_limit_notify=True)
  try:
    api.verify_credentials()
  except Exception as e:
    logger.error("Error creating API", exc_info=True)
    raise e
  logger.info("API created")
  return api


def main():
  api = create_api()
  tweets_listener = LikeAndRetweetListener(api)
  stream = tweepy.Stream(api.auth, tweets_listener)
  stream.filter(follow=[str(USER_ID)])


if __name__ == "__main__":
  main()
