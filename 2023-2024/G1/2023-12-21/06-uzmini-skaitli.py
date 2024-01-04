# Pārveido programmu, lai uzminamais skaitlis tiktu genģenerēts no nejauša intervāla, piemēram, no 1 līdz 100
# Jāpapildina programmas kods, lai mainīgais cik_reizes pēc katra minējuma palielinas par 1. Beidzot spēli, jāparāda, cik reizēs uzminēts
# Papildini programmu, lai minēšanas reižu skaits būtu ierobežots. To nevis izdomā, bet aprēķini, lietotojot math moduli. Formula ir math.log(lidzCikMinet, 2), bet šo rezultātu jānoapaļu uz augšu.
import random

skaitlis = random.randrange(1, 101)
jamin = True
cik_reizes = 0

while jamin:
    minejums = int(input("Mēģini uzminēt!"))
    cik_reizes += 1
    if minejums == skaitlis:
        jamin = False
        print(cik_reizes)
    elif minejums > skaitlis:
        print("Par lielu")
    elif minejums < skaitlis:
        print("Par mazu")
    else:
        print("Kaut kas nav kārtībā")
