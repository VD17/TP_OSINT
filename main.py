from tools.urlscan import UrlScan
#from tools.dnscan import dnsScan
from tools.shodan import shodan_search

import os
import sys
#import shodan
import theHarvester
import requests
import json





def menu():
    while True:
        print("Quel outils voulez-vous utilser ? \n ")
        
        print("1. Dnscan") # URGENT : A CORRIGER !!!!
        
        print("2. Shodan") # URGENT : A CORRIGER !!!!
        
        print("3. TheHarvester")
        
        print("4. urlscan")  # FONCTIONNEL 
        
        print("0. à bientot :) ")
        

        choice = input("Enter your choice: ")
        if choice == "0":
            break
            
        elif choice == "1": #NE FONCTIONNES PAS A CORRIGER
            domaine = input("Enter the target domain: ")
            dnscan(dns)
            
            
        elif choice == "2":
            domain = input("Insérez une IP cible : ") #NE FONCTIONNES PAS A CORRIGER
            api_key = input("Insérez votre clé API shodan.io (Rendez-vous à : ' https://shodan.io/ ' pour en récupérer une ) : \n ")
            shodan_search(domain, api_key)
            
        elif choice == "3":
            query = input("A IMPLÉMNETER  ")
            target = input("A IMPLEMENTER ")
            theHarvester.run(query, target)
            
        elif choice == "4":
            domain_name = input("Insérez le nom de domaine ciblé: ")
            api = input("Insérez votre clé API urlscan.io (Rendez-vous à : ' https://urlscan.io/ ' pour en récupérer une ) : ")
            UrlScan(domain_name, api)
            
        else:
            print("Invalid choice")

if __name__ == '__main__':

    menu()

