import requests

try:
    atbilde = requests.get("https://api.nobelprize.org/v1/prize.json")
    if atbilde.status_code == 200:
        dati_json_visi = atbilde.json()
        # print(dati_json_visi)
        dati_saraksts = dati_json_visi["prizes"]
        for viens in dati_saraksts:
            try:
                print(viens["year"], viens["category"])
                for laureats in viens["laureates"]:
                    print(laureats["firstname"])
            except KeyError:
                print(viens["year"], viens["category"], "netika piešķirta")
    else:
        print(f"Neizdevās. Kods {atbilde.status_code}.")
except ConnectionError:
    print("Iespējams nestrādā tīkls.")
