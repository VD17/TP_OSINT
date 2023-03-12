from tools.urlscan import UrlScan
from tools.dnscan import dnscan
from tools.shodan import shodan_search
from tools.theharvester import run_theharvester

import os
import sys
import theHarvester
import requests
import json




def menu():
    while True:
        print("Quel outils voulez-vous utilser ? \n ")
        
        print("1. Dnscan") 
        
        print("2. Shodan") 
        
        print("3. TheHarvester")  
        
        print("4. urlscan")  
        
        print("0. à bientot :) ")
        

        choice = input("Enter your choice: ")
        if choice == "0":
            break
            
        elif choice == "1":
            domain = input("Insérez un nom de domaine cible: (ex : kali.org) ")
            filename_suffix = input("Insérez un nom de fichier dans lequel votre résultat vas être enregistré : \n ")
            dnscan(domain, filename_suffix)
            print(f"Résultats enregistrés dans dnscan_{filename_suffix}.txt")

            
        elif choice == "2":
            domain = input("Insérez une IP cible (ex : 127.0.0.1) : ")
            api_key = input("Insérez votre clé API shodan.io (Rendez-vous à : ' https://shodan.io/ ' pour en récupé une : \n ")
            filename_suffix = input("Insérez un nom de fichier dans lequel votre résultat vas être enregistré : \n ")
            shodan_search(domain, api_key, filename_suffix)
            
        elif choice == "3":     
            domain = input('Insérez le domaine cible : (ex : kali.org) ')
            navigator = input ('Avec quel navigateur ? (Vous pouvez utiliser les navigateurs connus tels que : google, bing ect ... si non utilisez ''all'' pour utiliser tous les navigateurs) : ')
            output = run_theharvester(domain, navigator)
            filename = f'{domain}.txt'
            with open(filename, 'w') as f:
                f.write(output)
            print(f'Résultats enregsirés dans {filename}')
    
        elif choice == "4":
            domain_name = input("Insérez le nom de domaine ciblé (ex : kali.org) : ")
            api = input("Insérez votre clé API urlscan.io (Rendez-vous à : ' https://urlscan.io/ ' pour en récupérer une ) : ")
            filename_suffix = input("Entrez le nom du fichier de sortie : ")
            UrlScan(domain_name, api, filename_suffix)

            
            
        else:
            print("Veuillez choisir entre les options qui vous sont proposées (0, 1, 2, 3 et 4)")

if __name__ == '__main__':

    menu()

