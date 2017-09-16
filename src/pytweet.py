import twitter_config, analysis, tweepy

consumer_key = twitter_config.CONSUMER_KEY
consumer_secret = twitter_config.CONSUMER_SECRET
access_token = twitter_config.ACCESS_TOKEN
access_token_secret = twitter_config.ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth,parser=tweepy.parsers.JSONParser())

def getTweets():
    tweets = api.user_timeline('BlakeJoynes8')
    return tweets

def reply_to(tweet):
    '''
    replies to the given tweet with a sad meme and a message along te lines of "don't bully"
    '''
    pass

def getDms():
    dms = api.direct_messages()
    for dm in dms:
        handle = analysis.find_handle(dm)
        print(handle)


getDms()

# tweets = getTweets()
# for tweet in tweets:
#     if analysis.check_message(tweet.text):
#         reply_to(tweet)
