import json

with open("pasutijums.json", "r", encoding="utf-8") as datne:
    dati = datne.read()

dati_vardnica = json.loads(dati)
print(dati_vardnica)
