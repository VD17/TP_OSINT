from pprint import pprint

import requests


def dnscan(domain):

    pprint(requests.get(f"https://networkcalc.com/api/dns/lookup/{domain}").json())
