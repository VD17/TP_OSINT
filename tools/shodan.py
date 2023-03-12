import json
from pprint import pprint

import requests
from shodan import Shodan

def shodan_search(domain, api_key, filename_suffix):
    api = Shodan(api_key)
    result = api.host(domain)
    
    with open(f"shodan_{filename_suffix}", 'w') as f:
        json.dump(result, f, indent=4)
    
    org = result['org']
    dom = result['domains']
    ip_str = result['ip_str']
    ports = result['ports']
    local = result['city']
    
    print(f"\n Résultats essentiels : \n Organisation : {org} \n Domain(s) : {'n '.join(dom)} \n IP : {ip_str} \n Ports : {', '.join(map(str, ports))}\n Localisation : {local} \n")
