lista skripti:

config_reader - fajl koji ce otvarati konfiguracije.txt
i  na osnovu tih konfiguracija izvrsavati skriptu koja ce sacuvati sve u config.json
taj fajl ce se nalaziti uvek na'C:/test_config.txt'

plst_reader je skripta koja otvara plst_proba.txt sa putanje koja je podesena u config fajlu
zatim  cita artikle i puni fajlove voce.json i povrce.json
na osnovu WGNU broja
WGNU 2 je voce a WGNU 3 je povrce


json_sorter  je skripta koja otvara json fajlove voce i povrce
sortira plu od najnizeg ka najvisem i upisuje u voce_91 i povrce_91.json
ako nema dovoljno artikala onda dodaje 99990 prazan artikal

create_fuco pravi xml fajl od sortiranih 91 voca i povrca

test connection

send fuco file

