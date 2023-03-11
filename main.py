from tools.urlscan import UrlScan
#from tools.dnsscan import dnsScan
#from tools.shodan import shodan

import os
import sys
#import shodan
import theHarvester
import requests
import json





def menu():
    while True:
        print("Quel outils d'OSINT voulez-vous utilser ?:")
        
        print("1. DNS Scan")
        
        print("2. Shodan")
        
        print("3. TheHarvester")
        
        print("4. urlscan.io")
        
        print("0. Exit")
        

        choice = input("Enter your choice: ")
        if choice == "0":
            break
            
        elif choice == "1":
            domaine = input("Enter the target domain: ")
            dnsScan(domaine)
            
        elif choice == "2":
            ip = input("Enter the Shodan query: ")
            cle_api = input("Enter your Shodan API key: ")
            shodan(ip, cle_api)
            
        elif choice == "3":
            query = input("Enter the search query: ")
            target = input("Enter the target domain: ")
            theHarvester.run(query, target)
            
        elif choice == "4":
            domain_name = input("Insérez le nom de domaine ciblé: ")
            api = input("Insérez votre clé API urlscan.io (Rendez-vous à : ' https://urlscan.io/ ' pour en récupérer une ) : ")
            UrlScan(domain_name, api)
            
        else:
            print("Invalid choice")

if __name__ == '__main__':

    menu()

