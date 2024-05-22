import json


def open_plst():
    json_config_path = 'config.json'

    with open(json_config_path, 'r') as json_file:
        data = json.load(json_file)
        plst_path = data["PutanjaDoPlst_txt"]
        # print(plst_path)
    file_path = plst_path
    json_output_path_2 = 'voce.json'
    json_output_path_3 = 'povrce.json'
    # with open('plst_proba.txt', 'r') as c:
    #     kategorije_c = load(c)

    article_length = data["Max_duzina_za_novi_red"]  # Dužina svakog artikla u karakterima

    data_voce = {}
    data_povrce = {}

    with open(file_path, 'r') as file:
        while True:
            chunk = file.read(article_length)
            if not chunk:
                break  # Prekida petlju ako nema više sadržaja za čitanje

            # Izdvajanje podataka iz trenutnog dela
            plu = chunk[data["PluPocetak"]:data["PluPocetak"] + data["PluDuzina"]]
            naziv = chunk[data["NazivPocetak"]:data["NazivPocetak"] + data["NazivDuzina"]].strip()
            odeljenje = chunk[data["OdeljenjePocetak"]:data["OdeljenjePocetak"] + data["OdeljenjeDuzina"]]
            wgnu = chunk[data["WGNU"]:data["WGNU"] + data["WgnuDuzina"]]

            try:
                if wgnu == "2":
                    data_voce[plu] = {
                        "naziv": naziv,
                        "odeljenje": odeljenje,
                        "wgnu": wgnu
                    }
                    # Čuvanje izmenjenog sadržaja u JSON fajl
                    with open(json_output_path_2, 'w') as json_file:
                        json.dump(data_voce, json_file, indent=4, ensure_ascii=False)
                elif wgnu == "3":
                    data_povrce[plu] = {
                        "naziv": naziv,
                        "odeljenje": odeljenje,
                        "wgnu": wgnu
                    }
                    # Čuvanje izmenjenog sadržaja u JSON fajl
                    with open(json_output_path_3, 'w') as json_file:
                        json.dump(data_povrce, json_file, indent=4, ensure_ascii=False)
                else:
                    continue
            except Exception as e:
                print(e)


open_plst()
