"""
while nosacījums:
    programmas daļa,
    kura strādā, kamēr
    nosacījums ir True
"""
slegts = True
parole = "123"
while slegts:    
    lietotaja_parole = input("Raksti savu paroli!")
    if parole == lietotaja_parole:
        print("Pieslēgšanās veiksmīga")
        slegts = False
    elif lietotaja_parole == "":
        print("Nekas netika uzrakstīts")
    else:
        print("Nepareizi!")
