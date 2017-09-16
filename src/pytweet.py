import twitter_config
import analysis

import tweepy

consumer_key = twitter_config.CONSUMER_KEY
consumer_secret = twitter_config.CONSUMER_SECRET
access_token = twitter_config.ACCESS_TOKEN
access_token_secret = twitter_config.ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


def get_tweets():
    api.user_timeline(user_id)

def reply_to(tweet):
    '''
    replies to the given tweet with a sad meme and a message along te lines of "don't bully"
    '''
    pass

tweets = get_tweets()
for tweet in tweets:
    if analysis.check_message(tweet.text):
        reply_to(tweet)
