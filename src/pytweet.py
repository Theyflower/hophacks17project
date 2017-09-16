"""
 AntiBullyBot: A twitter bot to fight bullying.
    Copyright (C) 2017  The AntiBullyBot Team

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
import twitter_config

import tweepy

consumer_key = twitter_config.CONSUMER_KEY
consumer_secret = twitter_config.CONSUMER_SECRET
access_token = twitter_config.ACCESS_TOKEN
access_token_secret = twitter_config.ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth,parser=tweepy.parsers.JSONParser())


def get_tweets(bully):
    '''
    preconditions:
        @param bully is the twitter id of a bully
    postconditions:
        returns a tuple of tweepy status objects consisting of undigested tweets made by the user specified in bully
    '''
    return api.user_timeline(user_id=bully)


def reply_to(status):
    '''
    preconditions:
        @param status is a tweepy status object
    postconditions:
        replies to status with a tweet containing an anti-bullying slogan and a sad meme
    '''
    tweet_id = status.id #this variable contains the id of the tweepy status object
    api.update_status("don't be a bully",in_reply_to_status_id=status_id)

def get_id_from_handle(handle):
    '''
    preconditions:
        @param handle is a string of a twitter users
    postconditons:
        returns the numerical twitter id associated with that handle
    '''
    user = api.get_user(screen_name=handle)
    return user.id

def get_dms():
    try:
        f = open("latest_dm", mode='r')
        latest_dm = int(f.read())
    except:
        latest_dm = 0

    dms = api.direct_messages(since_id=latest_dm)
    if len(dms) > 0:
        latest_dm = dms[0]["id"]

    try:
        f = open("latest_dm", mode="w")
        f.write(str(latest_dm))
    except:
        pass

    return dms
