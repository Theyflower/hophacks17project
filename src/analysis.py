"""
 analysis.py: A wrapper for the Bark Partner API
    Copyright (C) 2016  Aaron Thomas

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
import json

import pybark
from bark_config import BARK_TOKEN

def check_message(message):
    '''
    preconditions:
        @param message is a string
    postconditions:
        returns a boolean
            True of the message is abusive
            False if the message is not abusive
    '''
    resp = pybark.woof(BARK_TOKEN, message)
    resp = json.loads(resp)
    power_level = [resp['abusive'],resp['results']['sentiment'] in ["VERY_NEGATIVE", "NEGATIVE"]]
    bad_varname = ["profanity", "cyberbullying"]
    power_level = power_level + [resp['results'][i]['abusive'] for i in bad_varname]
    return sum(power_level) >=2

def find_handle(message):
    '''
    preconditions:
        @param message is a string
    postconditions:
        returns a tuple containing all of the twitter ids of any @handles given in the text of the direct message
        returns a tuple containing all of the twitter  @handles given in the text of the direct message
        example outputs:
            () none given
            (aaron_the_king,,@hack,@hateishate_) three given
            (@aaron_the_king,@jack) two
            (@aaron_the_king) one given
    '''
    words = message.split(" ")
    handles = (word for word in words if word.startswith('@'))
    return handles
