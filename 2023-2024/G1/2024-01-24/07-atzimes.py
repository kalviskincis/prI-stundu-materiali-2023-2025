atzimes = []

ievade = True
while ievade:
    atz = int(input("Raksti atzīmi no 1 līdz 10. 0 lai pārtrauktu."))
    if 1 <= atz <= 10:
        atzimes.append(atz)
    elif atz == 0:
        ievade = False
    else:
        print("Neatbilst nosacījumiem.")

print(atzimes)
labaka = max(atzimes)
zemaka = min(atzimes)
skaits = len(atzimes)
videja = sum(atzimes) / skaits
print(labaka, zemaka, skaits, videja)

for katra in atzimes:
    print(katra)
    if katra < 4:
        print("Vērtējums nepietiekams!")