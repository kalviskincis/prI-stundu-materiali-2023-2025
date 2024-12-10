import requests

try:
    atbilde = requests.get("https://r6vsk.lv/api/cenas.json")
    if atbilde.status_code == 200:
        dati_json = atbilde.json()
        mani_dati = dati_json["result"]["records"]
        # pieturu_skaits = len(mani_dati)
        # print(pieturu_skaits)
        
        cenas = []
        for katrs in mani_dati:
            cenas.append(katrs["price"])
            
        dargaka = max(cenas)
        print(dargaka)
        videja = sum(cenas) / len(cenas)
        print(videja)
        

    else:
        print(f"Neizdevās. Kods {atbilde.status_code}.")
except ConnectionError:
    print("Iespējams nestrādā tīkls.")