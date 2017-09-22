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
import analysis
import twitter_config

import tweepy

consumer_key = twitter_config.CONSUMER_KEY
consumer_secret = twitter_config.CONSUMER_SECRET
access_token = twitter_config.ACCESS_TOKEN
access_token_secret = twitter_config.ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

rest_api = tweepy.API(auth,parser=tweepy.parsers.JSONParser())

class BullyStreamListener(tweepy.StreamListener):

    self.bullies = []

    def on_status(self, status):
        if analysis.check_message(status['text']):
            reply_to(status)

    def stream(self, bullies):
        '''
        preconditions:
            @param bullylist is a list of valid twitter ids (i.e. ints above zero)
        postconditions:
            starts a stream to the twitter api if all preconditions are met
            raises a TypeError if the preconditions are not met
        '''
        if all(i > 0 and isinstance(i,type(int())) for i in bullies):
            self.bullies = bullies
            self.filter(follow=bullies, async=True)
        raise TypeError("Expecting a list containing only ints above zero")


def reply_to(status):
    '''
    preconditions:
        @param status is a tweepy status object
    postconditions:
        replies to status with a tweet containing an anti-bullying slogan and a sad meme
    '''
    tweet_id = status['id'] #this variable contains the id of the tweepy status object
    try:
        rest_api.update_status("@{} don't be a bully".format(status['user']['screen_name']),in_reply_to_status_id=tweet_id)
    except:
        pass


def get_id_from_handle(handle):
    '''
    preconditions:
        @param handle is a string of a twitter users
    postconditons:
        returns the numerical twitter id associated with that handle
    '''
    try:
        user = rest_api.get_user(screen_name=handle)
        return user['id']
    except:
        return None


def get_dms():
    try:
        f = open("latest_dm", mode='r')
        latest_dm = int(f.read())
    except:
        latest_dm = 0

    dms = rest_api.direct_messages(since_id=latest_dm)
    if len(dms) > 0:
        latest_dm = dms[0]["id"]

    try:
        f = open("latest_dm", mode="w")
        f.write(str(latest_dm))
    except:
        pass

    return dms
