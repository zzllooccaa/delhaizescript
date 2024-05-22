from config_reader import update_config
from plst_reader import open_plst
from json_sorter import sorting
import datetime
import time
import json

print("Delhaize script started")
print("Time :  ", datetime.datetime.now())

# Konfiguracije
print("Korak 1")
print("Setovanje konfiguracija")
print("Citanje konfiguracije")
update_config()


#Otvaranje plst fajla
print("Korak 2")
print("Citanje plst_proba.txt")
open_plst()
print("Napunjeni fajlovi voce.json i povrce.json")


#sortiranje fajlova
print("Korak 3")
print("Sortiranje json fajlova po plu broju")
sorting()




print("Delhaize script ended")
print("Time :  ", datetime.datetime.now())
time.sleep(60)

