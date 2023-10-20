skaitlis = 50
jamin = True
cik_reizes = 0

while jamin:
    minejums = int(input("Mēģini uzminēt!"))
    cik_reizes += 1
    if minejums == skaitlis:
        print(f"Uzminēts {cik_reizes} reizēs.")
        jamin = False
    elif minejums > skaitlis:
        print("Par lielu")
    elif minejums < skaitlis:
        print("Par mazu")
    else:
        print("Kaut kas nav kārtībā")
