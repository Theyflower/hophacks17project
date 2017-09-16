import twitter_config, analysis, tweepy

consumer_key = twitter_config.CONSUMER_KEY
consumer_secret = twitter_config.CONSUMER_SECRET
access_token = twitter_config.ACCESS_TOKEN
access_token_secret = twitter_config.ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth,parser=tweepy.parsers.JSONParser())

def get_tweets(bullies):
    '''
    preconditions:
        @param bullies is an iterable containing the twitter ids (numerical) of users
    postconditions:
        returns a tuple of tweepy status objects consisting of undigested tweets made by the users specified in bullies
    '''
    pass

def reply_to(status):
    '''
    preconditions:
        @param status is a tweepy status object
    postconditions:
        replies to status with a tweet containing an anti-bullying slogan and a sad meme
    '''
    tweet_id = status.id #this variable contains the id of the tweepy status object


def getDms():
    dms = api.direct_messages()

    return dms


def getLatestDm(messages):
    latest = messages[0]
    print(latest)
    # for text in latest:
    #     print(text)
    # handles = analysis.find_handle(text)
    # if handles:
    #     for handle in handles:
    #           print(handle)


dms = getDms()
getLatestDm(dms)

# tweets = getTweets()
# for tweet in tweets:
#     if analysis.check_message(tweet.text):
#         reply_to(tweet)
