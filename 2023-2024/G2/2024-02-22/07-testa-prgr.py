picas = ["Zemeņu", "Aveņu"]
picas.sort()
for viena in picas:
    print(viena)

saraksts = [10, 16, 22, 100, 120, 133]
print(saraksts)
summa = sum(saraksts[0:3]) #v1

#v2
summa = 0
for sk in saraksts:
    if sk < 100:
        summa+=sk
