import requests

import config

def api_search(q=None, ds=None, fg=None, sort=None, max_=None, offset=None,):
    '''
    Wrapper for the USDA Food Composition Databases Search api.
    If no values are given for a parameter and it defaults to none then that
    parameter will not be sent to the API.

    For information about what each of the parameters are please consult this handy table!
    Name	Required	Default	Description
    api_key	y	n/a	Must be a data.gov registered API key
    q	n	""	Search terms
    ds	n	""	Data source. Must be either 'Branded Food Products' or 'Standard Reference'
    fg	n	""	Food group ID
    sort	n	r	Sort the results by food name (n) or by search relevance (r)
    max	n	50	maximum rows to return
    offset	n	0	beginning row in the result set to begin
    format1	n	JSON 	results format: json or xml

    For full documentation on this API please check this link: https://ndb.nal.usda.gov/ndb/doc/apilist/API-SEARCH.md

    Returns the json data as a string.
    '''
    url = "https://api.nal.usda.gov/ndb/search/?"
    data = {"api_key": config.usda_api_key,
            "q": q,
            "ds": ds,
            "fg": fg,
            "sort": sort,
            "max": max_, #named like this because python has builtin func "max"
            "offset": offset,
            "format": "json"#named like this because python has builtin func "max"
    }
    params = "&".join(["{}={}".format(key,data[key]) for key in data.keys() if data[key] != None])
    url = "{}{}&".format(url,params)
    print("CHECKING URL",url)
    request = requests.get(url)
    return request.text
