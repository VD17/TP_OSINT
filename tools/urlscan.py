import requests
import json

def scanUrl(domain_name):
    headers = {'API-Key': 'a35b2b44-d442-4b92-8ddf-f43b42365030', 'Content-Type': 'application/json'}
    data = {"url": f"{domain_name}", "visibility": "public"}
    answer = requests.post('https://urlscan.io/api/v1/scan/', headers=headers, data=json.dumps(data))
    print(answer)
    a = answer.json()
    print(a["result"])
