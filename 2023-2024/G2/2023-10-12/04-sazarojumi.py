"""
if apgalvojums:
    kods, kurš
    strādā, ja
    apgalvojums ir True
elif cits apgalvojums: # elif var nebūt, bet var būt arī vairāki
    kods, kurš
    strādā, ja
    cits apgalvojums ir True
else:
    kods, kurš
    strādā, ja
    apgalvojums ir False
"""
parole = "123"
lietotaja_parole = input("Raksti savu paroli!")
if parole == lietotaja_parole:
    print("Pieslēgšanās veiksmīga")
elif lietotaja_parole == "":
    print("Nekas netika uzrakstīts")
else:
    print("Nepareizi!")
