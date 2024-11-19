import requests
from tabulate import tabulate

try:
    atbilde = requests.get("https://zenquotes.io/api/quotes")
    if atbilde.status_code == 200:
        dati = atbilde.json()
        # print(dati)
        # TIKAI Citāta autors un pats citāts.
        tabula = []
        for katrs in dati:
            rinda = [katrs["a"], katrs["q"]]
            tabula.append(rinda)
            #print(katrs["a"], katrs["q"])
        print(tabulate(tabula))

    else:
        print(f"Neizdevās. Atbilde {atbilde.status_code}.")
except ConnectionError:
    print("Tīkla kļūda.")

