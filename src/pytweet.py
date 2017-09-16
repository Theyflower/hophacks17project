import twitter_config, analysis

import tweepy

consumer_key = twitter_config.CONSUMER_KEY
consumer_secret = twitter_config.CONSUMER_SECRET
access_token = twitter_config.ACCESS_TOKEN
access_token_secret = twitter_config.ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def get_tweets(bullies):
    '''
    preconditions:
        @param bullies is an iterable containing the twitter ids (numeric) of bullies
    postconditions:
        returns an iterable containing tweets not previously injested by the bot made by the bullies
        it should include only replies to tweets made by other users and retweets of tweets made by other users
    '''
    tweets = api.user_timeline('BlakeJoynes8')
    return tweets

def reply_to(tweet):
    '''
    replies to the given tweet with a sad meme and a message along te lines of "don't bully"
    '''
    pass

tweets = getTweets()
for tweet in tweets:
    if analysis.check_message(tweet.text):
        reply_to(tweet)
