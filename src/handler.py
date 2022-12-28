import tweepy
from src.keys import getKeys
from src.content import generate

def handler(event, context):
    keys = getKeys()
    client = tweepy.Client(
        consumer_key=keys['consumer_key'],
        consumer_secret=keys['consumer_secret'],
        access_token=keys['access_token'],
        access_token_secret=keys['access_token_secret'],
    )
    tweet = generate(keys['openai_key'])
    client.create_tweet(text=tweet)
    