import json
import os
import sys


# Funkcija za čitanje konfiguracija iz Konfiguracije.txt
def read_txt_config(txt_file):
    config = {}
    try:
        with open(txt_file, 'r') as file:
            for line in file:
                if ':' in line:
                    key, value = line.strip().split(':', 1)
                    key = key.strip().strip('"')
                    value = value.strip().strip('"')
                    # Provera i konvertovanje vrednosti u odgovarajući tip
                    if key in ["PluPocetak", "PluDuzina", "WGNU", "NazivPocetak", "NazivDuzina", "OdeljenjePocetak",
                               "OdeljenjeDuzina", "CenaPocetak", "CenaDuzina", "Max_duzina_za_novi_red", "BrojVaga"]:
                        value = int(value)
                    config[key] = value
    except Exception as e:
        print(f"Greska prilikom citanja config_txt fajla {txt_file}: {e}")
        print(f"Mozda je negde postavljeno u config.txt slovo a ocekuje se broj!")
        sys.exit(1)
    return config


# Funkcija za čitanje postojećih konfiguracija iz config.json
def read_json_config(json_file):
    try:
        if os.path.exists(json_file):
            with open(json_file, 'r') as file:
                return json.load(file)
    except Exception as e:
        print(f"Greska prilikom citanja config.json fajla u samoj aplikaciji {json_file}: {e}")
        sys.exit(1)
    return {}


# Funkcija za pisanje konfiguracija u config.json
def write_config_to_json(config, json_file):
    try:
        with open(json_file, 'w') as file:
            json.dump(config, file, indent=4)
    except Exception as e:
        print(f"Greska prilikom upisivanja konfiguracija iz config.txt u config.json {json_file}: {e}")
        sys.exit(1)


# Glavna funkcija
def update_config():
    try:
        # Definišite putanje do txt i json fajlova
        txt_file = 'Konfiguracije.txt'
        json_file = 'config.json'

        # Čitanje novih konfiguracija iz txt fajla
        new_config = read_txt_config(txt_file)

        # Čitanje postojećih konfiguracija iz json fajla
        existing_config = read_json_config(json_file)

        # Ažuriranje postojećih konfiguracija sa novim vrednostima
        existing_config.update(new_config)

        # Pisanje ažuriranih konfiguracija u json fajl
        write_config_to_json(existing_config, json_file)

        print(f"Ucitane konfiguracije u fajl: {json_file}")

    except Exception as e:
        print(f"Greska prilikom update config.json fajla: {e}")
        sys.exit(1)
