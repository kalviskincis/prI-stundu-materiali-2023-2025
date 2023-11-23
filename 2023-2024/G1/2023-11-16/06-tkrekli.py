def pasuti_tkreklus(skaits, apdruka, piegade):
    if apdruka == "TEKSTS":
        summa = skaits * 5
    elif apdruka == "ZIME":
        summa = skaits * 7
    elif apdruka == "FOTO":
        summa = skaits * 20
    else:
        print("Kļūda")

    if piegade == True:
        if summa < 50:
            summa = summa + 15 # summa += 15

    

print(pasuti_tkreklus(3, "TEKSTS", True))
