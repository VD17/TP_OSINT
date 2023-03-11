import json
from pprint import pprint

import requests
from shodan import Shodan


def Shodan(domain, api_key): 
    api = Shodan(api_key)
    result = api.host(domain)
    
    pprint(result)


# URGENT : A CORRIGER !!!!
