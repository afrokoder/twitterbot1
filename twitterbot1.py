import tweepy
import time
from tokens import *


auth = tweepy.OAuthHandler(apiKey, apiKeySecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth, wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)
user = api.me()

search = '#afrodevs OR #blacktechtwitter OR #Python OR #naijadev OR #naijatech'
nrTweets = 10

for tweet in tweepy.Cursor(api.search, q=(search), lang='en').items(nrTweets):
    try:
        print('\nTweet by: @' + tweet.user.screen_name)
        tweet.retweet()
        print('retweeted tweet')
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

for tweet in tweepy.Cursor(api.search, q=(search), lang='en').items(nrTweets):
    try:
        # Add \n escape character to print() to organize tweets
        print('\nTweet by: @' + tweet.user.screen_name)
        # Retweet tweets as they are found
        tweet.favorite()
        print('Like the tweet')
        time.sleep(5)

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break
