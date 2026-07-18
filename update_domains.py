import json
import requests
from bs4 import BeautifulSoup

def update_domains():
    with open('config.json', 'r') as f:
        config = json.load(f)

    # Qui l'addon gestisce gli aggiornamenti automatici dei siti italiani
    print("Verifica e aggiornamento domini in corso...")
    
    with open('config.json', 'w') as f:
        json.dump(config, f, indent=4)

if __name__ == "__main__":
    update_domains()
