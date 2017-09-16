"""
 PyBark: A wrapper for the Bark Partner API
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
import requests

def woof(BARK_TOKEN, message):
	'''
	preconditions:
		@param BARK_TOKEN is a valid Bark Partner API Token
		@param message is something the Bark Partner API will find meaningful
	postconditons:
		If the preconditions are met it will return the Bark Patner API's appraisal of @param message
		Otherwise it returns the HTTP Status Code of the request
	'''
	url = "https://partner.bark.us/api/v1/messages"
	headers = {"Content-Type" : "application/json; charset=utf-8",
				"X-Token-Auth" : BARK_TOKEN}
	data = {"message" : message}
	request = requests.post(url, json=data, headers=headers)

	if request.status_code == 200:
		return request.text
	else:
		return request.status_code
