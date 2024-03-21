import json
import uuid

apdrukasVeidi = {'TEKSTS': 5, 'ZIME': 7, 'FOTO': 20}
visi_pasutijumi = []

try:
    with open("pasutijums.json", "r", encoding="utf-8") as datne:
        dati = datne.read()

    visi_pasutijumi = json.loads(dati)
except:
    pass


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

    visi_pasutijumi.append(pasutijums)

    dati = json.dumps(visi_pasutijumi, ensure_ascii=False)

    nosaukums = f"pasutijums.json"

    with open(nosaukums, "w", encoding="utf-8") as datne:
        datne.write(dati)

else:
    print("Tāda apdrukas veida nav.")