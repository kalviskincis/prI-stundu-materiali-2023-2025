atzimes = []

ievade = True

while ievade:
    atz = int(input("Raksti atzīmi: "))
    if 1 <= atz <= 10:
        atzimes.append(atz)
    else:
        break

labaka = max(atzimes)
zemaka = min(atzimes)
skaits = len(atzimes)
videja = sum(atzimes) / skaits

print(labaka, zemaka, skaits, videja)

for viena in atzimes:
    if viena >= 4:
        print(viena)
    else:
        print(f"{viena} (nepietiekams vērtējums).")
