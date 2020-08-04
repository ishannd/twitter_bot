import tweepy
from creds import api_key,api_secretkey,Access_token,Access_tokensecret
from os import environ
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)

auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)

api = tweepy.API(auth)

user = api.me()

search = "python"

numberofTweets = int("100000")

phrase = "Hi, I am a bot.\n you used the word python in your tweet hence I'm here."

for tweet in tweepy.Cursor(api.search,search).items(numberofTweets):
    try:
        tweet.retweet()
        tweet.favorite()
        print("retweeted and favourited")
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

