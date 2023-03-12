import requests

#Cette fonction effectue une recherche DNS pour un nom de domaine donné et enregistre les résultats dans un fichier texte.
#La première partie du nom du fichier est détérminé par le paramètre 'filename_suffix'
def dnscan(domain, filename_suffix):
    #Envoyer une requête GET à l'API DNS de networkcalc.com pour le nom de domaine doné.
    response = requests.get(f"https://networkcalc.com/api/dns/lookup/{domain}").text
    #Ouvrir un fichieren mode écriture et enregistre la réponse de la requête.
    with open(f"dnscan_{filename_suffix}.txt", 'w') as f:
        f.write(response)
    #Afficher un message pour indiquer que le fichier a été créé avec succès.
    print(f"Le fichier dnscan_{filename_suffix}.txt a été créé avec succès.")
