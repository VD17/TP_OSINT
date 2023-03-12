import requests
import json

def UrlScan(domain_name, api, filename_suffix):
    headers = {'API-Key': api , 'Content-Type': 'application/json'}
    data = {"url": f"{domain_name}", "visibility": "public"}
    
    answer = requests.post('https://urlscan.io/api/v1/scan/', headers=headers, data=json.dumps(data))
    
    if answer.status_code != 200:
       raise Exception(f"La requête a échoué avec le code {answer.status_code}")
    
    print("\n La requête a été exécutée avec succès : \n ", answer)
    a = answer.json()
    
    with open(f'urlscan_{filename_suffix}', 'w') as f:
        f.write(a["result"])
        
    print(f"Le lien urlscan.io a été enregistré dans le fichier {filename_suffix}")
