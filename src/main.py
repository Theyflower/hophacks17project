#!/usr/bin/env python
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
import pytweet
import analysis

import json
if __name__ == "__main__":
    #load saved bully list
    try:
        f = open("bullies", mode='r')
        print("opened bullies file successfully")
        bullies = json.loads(f.read())
    except Exception as err:
        print(err)
        print("Error loading bullies, if there are no bullies this is to be expected.")
        bullies = {}
    print("beginning bullies is",bullies)
    # get dms
    dms = pytweet.get_dms()

    # process dms and add to bully list
    print("analysing dms")
    for dm in dms:
        handles = analysis.find_handle(dm['text'])
        for handle in handles:
            tid = pytweet.get_id_from_handle(handle)
            if tid != None and tid not in bullies.keys():
                bullies[tid] = pytweet.get_latest_tweet(tid)
    print("done processing dms, here are the bullies:",bullies)

    # get tweets
    tweets = []
    for bully in bullies.keys():
        print("getting tweets from bully id",bully)
        tweets = tweets + pytweet.get_tweets(bully, bullies[bully])


    # process and reply to abusive tweets
    print("processing tweets, replying to tweets detected as abusive")

    for tweet in tweets:
        if analysis.check_message(tweet['text']):
            print("abusive tweet:",tweet['text'])
            print("replying to tweet with id of",tweet['id'])
            pytweet.reply_to(tweet)
        else:
            print("acceptable tweet:",tweet['text'])


    #save the bully list
    try:
        f = open("bullies", mode='w')
        f.write(json.dumps(bullies))
    except:
        pass
    print("Done!")
