import twitter

from pathlib import Path

home = str(Path.home())

try:
    with open('{}/twitter_keys.txt', 'r') as f:
        CONSUMER_KEY = str(f.readline())
        CONSUMER_SECRET = str(f.readline())
        ACCESS_TOKEN_KEY = str(f.readline())
        ACCESS_TOKEN_SECRET = str(f.readline())

        api = twitter.Api(consumer_key=CONSUMER_KEY,
                          consumer_secret=CONSUMER_SECRET,
                          access_token_key=ACCESS_TOKEN_KEY,
                          access_token_secret=ACCESS_TOKEN_SECRET)

except:
    api = twitter.Api()

statuses = api.getUserTimeline(user)
print([s.text for s in statuses])
