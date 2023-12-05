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
        if summa >= 50:
            piegades_maksa = 0
        else:
            piegades_maksa = 15
        
        summa = summa + piegades_maksa

    if summa > 100:
        summa = summa * 0.95
        # summa = summa - summa * 0.05
    
    return summa 

print(pasuti_tkreklus(100, "ZIME", False))