import requests
from tabulate import tabulate

try:
    atbilde = requests.get("https://zenquotes.io/api/quotes")
    if atbilde.status_code == 200:
        dati_json = atbilde.json()
        # print(dati_json)
        # PARĀDĪT CITĀTA AUTORU UN TEKSTU
        #tabula = []
        for viens in dati_json:
            print(viens["a"], viens["q"])
            #rinda = [viens["a"], viens["q"]]
            #tabula.append(rinda)
        #print(tabulate(tabula))

    else:
        print(f"Neizdevās. Kods {atbilde.status_code}.")
except ConnectionError:
    print("Iespējams nestrādā tīkls.")