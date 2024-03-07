import json

with open("pasutijums.json", "r", encoding="utf-8") as datne:
    dati = datne.read()

dati_vardnica = json.loads(dati)
print(dati_vardnica)

for numurs in range(1, 29):
    nr = f"https://www.riimc.lv/olympiad/{numurs}/apply"
    print(nr)
