picas = ["Garš nosaukums", "Īss"]
for viena in picas:
    print(len(viena), viena)

saraksts = [1, 2, 3, 4]
summa = sum(saraksts[1:3])

summa = 0
for sk in range(1,3):
    summa += saraksts[sk]
