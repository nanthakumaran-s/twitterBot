import os

def getKeys():
    keys = {}
    keys['consumer_key'] = os.getenv('twitter_consumer_key')
    keys['consumer_secret'] = os.getenv('twitter_consumer_secret')
    keys['bearer_token'] = os.getenv('twitter_bearer_token')
    keys['access_token'] = os.getenv('twitter_access_token')
    keys['access_token_secret'] = os.getenv('twitter_access_token_secret')
    keys['openai_key'] = os.getenv('openai_secret_key')
    return keys