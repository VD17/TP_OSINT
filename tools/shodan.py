import json
from pprint import pprint

import requests
from shodan import Shodan


def shodan_search(domain, api_key): 
    api = Shodan(api_key)
    result = api.host(domain)
    
    pprint(result)
    
    org = result['org']
    dom = result['domains']
    ip = result['ip']
    ports = result['ports']
    local = result['city']
    
    print(f"\n Résultat essentiels :\n organsation : {organisation} \n domaine : {dom}   \n ip : {ip} \n ports : {ports} \n Localication : {local} \n")
