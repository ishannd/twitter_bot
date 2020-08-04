import tweepy
from creds import api_key,api_secretkey,Access_token,Access_tokensecret

auth = tweepy.OAuthHandler(consumer_key=api_key,consumer_secret=api_secretkey)

auth.set_access_token(key=Access_token,secret=Access_tokensecret)

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

