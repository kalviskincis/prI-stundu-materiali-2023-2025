import random

def metiens():
    k1 = random.randrange(1, 7)
    k2 = random.randrange(1, 7)
    k3 = random.randrange(1, 7)
    metiena_summa = k1 + k2 + k3
    return metiena_summa

def spele():
    summa = 0
    while summa < 25:
        input("Met!")
        met = metiens()
        if met == 10:
            summa += 5
        elif met > 10:
            summa += 1
        else:
            summa -= 1
        print(f"Metiena summa {met}, līdz šim saņemti {summa} punkti.")
        if summa <= 0:
            print("Zaudējums.")
            break
    if summa >= 25:
        print(f"Uzvara ar {summa} punktiem.")

spele()
