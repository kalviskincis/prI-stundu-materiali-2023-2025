import json
import uuid

apdrukasVeidi = {'TEKSTS': 5, 'ZIME': 7, 'FOTO': 20}

vards = input('Ieraksti savu vārdu.')
veids = input('Kādu apdrukas veidu vēlies?').upper()
skaits = int(input('Cik kreklus vēlies pasūtīt?'))

if veids in apdrukasVeidi:
    pasutijums = {}
    summa = skaits * apdrukasVeidi[veids]
    print(f"Skaits: {skaits}, veids: {veids}. Kopā jāmaksā {summa}.")
    pasutijuma_nr = str(uuid.uuid4())
    pasutijums["numurs"] = pasutijuma_nr
    pasutijums["vārds"] = vards
    pasutijums["veids"] = veids
    pasutijums["skaits"] = skaits
    pasutijums["summa"] = summa

    dati = json.dumps(pasutijums, ensure_ascii=False)

    nosaukums = f"pasutijums-{pasutijuma_nr}.json"

    with open(nosaukums, "w", encoding="utf-8") as datne:
        datne.write(dati)

else:
    print("Tāda apdrukas veida nav.")