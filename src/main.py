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
    # process dms and add to bully list
    # check tweets
    # process tweets
    # reply to tweets
    #save the bully list
    try:
        f = open("bullies", mode='w')
        f.write(json.dumps(bullies))
    except:
        pass
