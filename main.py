import os
import sys
import subprocess

def importDnsrecon():
    try:
        import dnsrecon
    except ImportError:
        os.system("sudo apt install dnsrecon")
        importDnsrecon()

def importShodan():
    try:
        import shodan
    except ImportError:
        os.system("sudo pip install shodan")
        importShodan()

def importTheHarvester():
    try:
        import theHarvester
    except ImportError:
        os.system("sudo apt install theharvester")
        importTheHarvester()

def importUrlScan():
    try:
        import urlscan
    except ImportError:
        os.system("sudo apt-get install urlscan")  # Only for Linux kernels
        importUrlScan()

def verifImport():
    importDnsrecon()
    importShodan()
    importTheHarvester()
    importUrlScan()
    print("imports ok")

"""
    /!\demande clé API shodan/!\ 
"""
#verifImport()

def menu():
    while True:
        print("Quel outil d'OSINT voulez-vous utiliser ?:")
        print("1. DNSrecon")
        print("2. Shodan")
        print("3. TheHarvester")
        print("4. urlscan.io")
        print("0. Exit")

        choice = input("Enter your choice: ")
        if choice == "0":
            break
        elif choice == "1":
            target = input("Enter the target domain: ")
            subprocess.call(["dnsrecon", "-d", target])
        elif choice == "2":
            query = input("Enter the Shodan query: ")
            api_key = input("Enter your Shodan API key: ")
            subprocess.call(["shodan", "-k", api_key, "search", query])
        elif choice == "3":
            query = input("Enter the search query: ")
            target = input("Enter the target domain: ")
            subprocess.call(["theHarvester", "-d", target, "-b", query])
        elif choice == "4":
            target = input("Enter the target URL: ")
            api_key = input("Enter your urlscan.io API key: ")
            subprocess.call(["urlscan", "-k", api_key, "-u", target])
        else:
            print("Invalid choice")

if __name__ == '__main__':
    verifImport()
    menu()

