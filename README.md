
SALE FOU

# TP_OSINT
# Made by:
 Vishal DESAI 
 Mahmoud BOUJBIRI
 3SI1
 
# Fonctionnalités

Les différentes options de menu permettent d'utiliser les outils suivants :

dnscan: effectue une recherche de noms de domaine.

shodan: recherche d'informations sur les adresses IP via l'API Shodan.

theHarvester: récupère les adresses e-mail et les domaines associés.

urlscan: récupère les informations sur le domaine via l'API urlscan.io.

# Utilisation

Clonez le dépôt sur votre machine locale.

Assurez-vous d'avoir Python 3.x installé sur votre machine.

Assurez vous d'installer theHarvester sur l'appareil en utilisant la commande suivante : "sudo apt install theharvester"

Installez les dépendances nécessaires en exécutant la commande suivante : pip install -r requirements.txt

Exécutez le fichier main.py avec la commande suivante : python3 main.py.

Suivez les instructions à l'écran pour utiliser les différents outils disponibles.


# Options de menu

Dnscan: permet de rechercher des noms de domaine à partir d'un nom de domaine cible. Permet de sauvegarder les résultats dans un fichier texte.

Shodan: permet de rechercher des informations sur les adresses IP via l'API Shodan en fournissant une adresse IP cible et une clé API Shodan. Permet également de sauvegarder les résultats dans un fichier texte.

TheHarvester: permet de récupérer des adresses e-mail et des domaines associés à partir d'un nom de domaine cible. Permet également de sauvegarder les résultats dans un fichier texte.

urlscan: permet de récupérer des informations sur un domaine via l'API urlscan.io. Permet également de sauvegarder les résultats dans un fichier texte.


# Dépendances
## Le script utilise les bibliothèques suivantes : 

requests

theHarvester

dnspython

shodan

python-whois

urlscan-api

os

sys

json

pprint

subprocess


Les bibliothèques peuvent être installées via la commande : pip install -r requirements.txt
