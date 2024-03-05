import json

apdrukasVeidi = {'TEKSTS': 5, 'ZIME': 7, 'FOTO': 20}

vards = input('Ieraksti savu vārdu.')
veids = input('Kādu apdrukas veidu vēlies?').upper()
skaits = int(input('Cik kreklus vēlies pasūtīt?'))

if veids in apdrukasVeidi:
    pasutijums = {}
    summa = skaits * apdrukasVeidi[veids]
    print(f"Skaits: {skaits}, veids: {veids}. Kopā jāmaksā {summa}.")
    pasutijums["vārds"] = vards
    pasutijums["veids"] = veids
    pasutijums["skaits"] = skaits
    pasutijums["summa"] = summa

    dati = json.dumps(pasutijums, ensure_ascii=False)

    with open("pasutijums.json", "w", encoding="utf-8") as datne:
        datne.write(dati)

else:
    print("Tāda apdrukas veida nav.")