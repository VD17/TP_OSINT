import requests


def dnscan(domain, filename):
    response = requests.get(f"https://networkcalc.com/api/dns/lookup/{domain}").text
    with open(filename, 'w') as f:
        f.write(response)
