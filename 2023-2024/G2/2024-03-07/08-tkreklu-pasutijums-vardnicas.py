import json
import uuid

visiPasutijumi = []
apdrukasVeidi = {'TEKSTS': 5, 'ZIME': 7, 'FOTO': 20}

try:
    with open("pasutijums.json", "r", encoding="utf-8") as datne:
        dati = datne.read()

    visiPasutijumi = json.loads(dati)
except:
    pass

vards = input("Tavs vārds?")
veids = input('Kādu apdrukas veidu vēlies?').upper()
skaits = int(input('Cik kreklus vēlies pasūtīt?'))

if veids in apdrukasVeidi:
    pasutijums = {}
    numurs = str(uuid.uuid4())
    cena = apdrukasVeidi[veids]
    summa = cena * skaits
    print(f"Izvēlētais veids ir {veids}, skaits {skaits}, kopā jamaksā {summa}.")
    pasutijums["Numurs"] = numurs
    pasutijums["Vārds"] = vards
    pasutijums["Veids"] = veids
    pasutijums["Skaits"] = skaits
    pasutijums["Summa"] = summa

    visiPasutijumi.append(pasutijums)

    # pasutijums = {"Vārds": vards, "Veids": veids, "Skaits": skaits, "Summa": summa}

    dati = json.dumps(visiPasutijumi, ensure_ascii=False)

    nosaukums = f"pasutijums.json"
    with open(nosaukums, "w", encoding="utf-8") as datne:
        datne.write(dati)



# Turpini programmu, lai tā pārbauda, vai lietotāja izvēlētais apdrukas veids eksistē. Ja jā, aprēķina un parāda pasūtījuma kopsummu.