z1_sv = 100
z2_sv = 100

z1_pi = 1.05
z2_pi = 1.04

z1_merkis = z1_sv * 1.25

nedelas = 0
while z1_sv < z1_merkis: # b) while z1_sv < z2_sv * 1.10
    z1_sv = z1_sv * z1_pi # b) šis pats arī 2. žurkai
    print(z1_sv)
    nedelas += 1
print(f"Nepieciešamas {nedelas} nedēļas.")

#
krasa1 = {"R": 0.1, "G": 0.2, "B": 0.7}

def noteikt(krasa):
    vertibas = krasa.values()
    summa = sum(vertibas)
    if summa == 1:
        return True
    else:
        return False

    # return summa == 1

atbilde = noteikt(krasa1)
print(atbilde)