"""
if patiess apgalvojums:
    darbības, kuras
    notiek, ja
    ir True
elif cits patiess apgalvojums: # elif nav obligāti, bet tie var būt daudzi
    darbības, kuras
    notiek, ja
    ir True
else:
    darbības, ja
    ir False
"""
parole = "123"
lietotaja_parole = input("Lai pieslēgtos, raksti paroli: ")
if parole == lietotaja_parole:
    print("Pieslēgšanās veiksmīga")
elif lietotaja_parole == "":
    print("Nekas netika ierakstīts")
else:
    print("Nepareiza parole!")

    
