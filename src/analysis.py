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
    resp = pybark.woof(BARK_TOKEN, message)
    resp = json.loads(resp)
    return resp['results']['cyberbullying']['abusive']
def find_handle(status):
    '''
    preconditions:
        @param status is a direct message
    postconditions:
        returns a tuple containing all of the twitter  @handles given in the text of the direct message
        example outputs:
            () none given
            (@aaron_the_king,@jack) two
            (@aaron_the_king) one given
    '''
    text = status.text
    words = text.split(" ")
    handles = (word for word in words if word.startswith('@'))
    return handles
    #@todo(aaron): use tweepy to get ids of the handles
