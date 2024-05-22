import json
import os
import sys


# Funkcija za čitanje podataka iz JSON fajla
def read_json_file(json_file):
    try:
        if os.path.exists(json_file):
            with open(json_file, 'r') as file:
                return json.load(file)
    except Exception as e:
        print(f"Greska prilikom citanja fajla {json_file}: {e}")
        sys.exit(1)
    return {}


# Funkcija za pisanje podataka u JSON fajl
def write_to_json_file(data, json_file):
    try:
        with open(json_file, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Greska prilikom upisivanja u {json_file}: {e}")
        sys.exit(1)


# Funkcija za sortiranje i ograničavanje broja stavki
def process_data(data, max_items=91):
    sorted_items = sorted(data.items(), key=lambda x: int(x[0]))
    processed_data = {}

    for i, (plu, details) in enumerate(sorted_items[:max_items], start=1):
        processed_data[i] = {
            "plu": int(plu),
            "naziv": details["naziv"],
            "odeljenje": int(details["odeljenje"]),
            "wgnu": details["wgnu"]
        }

    # Dodavanje fiktivnih stavki ako ih ima manje od max_items
    for i in range(len(processed_data) + 1, max_items + 1):
        processed_data[i] = {
            "plu": 999990,
            "naziv": "Nema proizvoda",
            "odeljenje": 1,
            "wgnu": "2"  # ili "3" zavisno od fajla
        }

    return processed_data


# Glavna funkcija
def sorting():
    voce_file = 'voce.json'
    povrce_file = 'povrce.json'
    voce_output_file = 'voce_91.json'
    povrce_output_file = 'povrce_91.json'

    # Čitanje podataka iz JSON fajlova
    voce_data = read_json_file(voce_file)
    povrce_data = read_json_file(povrce_file)

    # Obrada podataka
    voce_processed_data = process_data(voce_data)
    povrce_processed_data = process_data(povrce_data)

    # Pisanje obrađenih podataka u nove JSON fajlove
    write_to_json_file(voce_processed_data, voce_output_file)
    write_to_json_file(povrce_processed_data, povrce_output_file)

    print(f"Podaci su uspešno zapisani u {voce_output_file} i {povrce_output_file}")



