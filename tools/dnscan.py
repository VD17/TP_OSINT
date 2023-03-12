import requests


def dnscan(domain, filename_suffix):
    response = requests.get(f"https://networkcalc.com/api/dns/lookup/{domain}").text
    with open(f"dnscan_{filename_suffix}.txt", 'w') as f:
        f.write(response)
    print(f"Le fichier dnscan_{filename_suffix}.txt a été créé avec succès.")
