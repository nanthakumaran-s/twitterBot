import os

def handler(event, context):
    print(os.getenv("twitter_api_key"))