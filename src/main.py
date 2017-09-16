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
        f = open("bullies", allmode='r')
        bullies = json.load(f.read())
    except:
        bullies = []

    # get dms
    dms = pytweet.get_dms()

    # process dms and add to bully list
    for dm in dms:
        handles = analysis.find_handle(dm)
        for handle in handles:
            tid = pytweet.get_id_from_handle(handle)
            if tid != None:
                bullies.add(tid)

    # get tweets
    tweets = []
    for bully in bullies:
        tweets = tweets + get_tweets(bully)

    # process tweets
    reply_to_these = []
    for tweet in tweets:
        if check_message(tweet.text):
            reply_to_these.append(tweet)

    # reply to tweets
    for tweet in reply_to_these:
        pytweet.reply_to(tweet)

    #save the bully list
    try:
        f = open("bullies", mode='w')
        f.write(json.dumps(bullies))
    except:
        pass
