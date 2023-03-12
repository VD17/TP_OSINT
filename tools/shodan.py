import json
from pprint import pprint

import requests
from shodan import Shodan


def shodan_search(domain, api_key): 
    api = Shodan(api_key)
    result = api.host(domain)
    
    pprint(result)
    
    dom = result['domains']
    ip = result['ip']
    local = result['city']
    
    print(f"\n Résultat essentiels : \n domaine : {dom}   \n ip : {ip} \n Localication : {local} \n")
