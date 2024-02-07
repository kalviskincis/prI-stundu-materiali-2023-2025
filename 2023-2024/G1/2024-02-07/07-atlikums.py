nominali = [200, 100, 50, 20, 10, 5, 2, 1]

def atlikums(summa):
    while summa != 0:
        for katrs in nominali:
            skaits = 0
            while summa >= katrs:
                summa -= katrs
                skaits += 1
            print(katrs, skaits)

summa = int(input("Cik centi jāizdod?"))
atlikums(summa)