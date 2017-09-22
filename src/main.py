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
import time


if __name__ == "__main__":
    #load saved bully list
    bullies_updated = True
    try:
        f = open("bullies", mode='r')
        print("opened bullies file successfully")
        bullies = json.loads(f.read())
    except Exception as err:
        print(err)
        print("Error loading bullies, if there are no bullies this is to be expected.")
        bullies = {}
    print("beginning bullies is",bullies)

    while(True):
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

        #sometimes create a stream
        if (bullies_updated):
            bsl = pytweet.BullyStreamListener()
            bsl.stream()

            #save the bully list
            try:
                f = open("bullies", mode='w')
                f.write(json.dumps(bullies))
            except:
                pass

        time.sleep(5 * 60)
