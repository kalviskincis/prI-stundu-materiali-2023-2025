import json

with open("pasutijums.json", "r", encoding="utf-8") as datne:
    dati = datne.read()

dati_vardnica = json.loads(dati)
print(dati_vardnica)

for nr in range(1, 30):
    url = f"https://www.riimc.lv/olympiad/{nr}/apply"
    print(url)