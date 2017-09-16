import twitter_config, tweepy,json

consumer_key = twitter_config.CONSUMER_KEY
consumer_secret = twitter_config.CONSUMER_SECRET
access_token = twitter_config.ACCESS_TOKEN
access_token_secret = twitter_config.ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


def getTweets(user_id, since_id):
    tweets = api.user_timeline('BlakeJoynes8')
    return tweets

if __name__ == '__main__':
    getTweets()

