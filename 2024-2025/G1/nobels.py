import requests

try:
    atbilde = requests.get("https://api.nobelprize.org/v1/prize.json")
    if atbilde.status_code == 200:
        dati_json = atbilde.json()["prizes"]
        # print(dati_json)                
        for viens in dati_json:
            print(viens["year"], viens["category"])
    
    else:
        print(f"Neizdevās. Kods {atbilde.status_code}.")
except ConnectionError:
    print("Iespējams nestrādā tīkls.")
