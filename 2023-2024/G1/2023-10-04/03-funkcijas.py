# Šī funkcija prasa lietotāja vārdu un sasveicinās.
def sveiciens():
    vards = input("Kā tevi sauc?").title()  # Prasa lietotāja vārdu
    print(f"Labdien, {vards}")  # Sveicina lietotāju

# Šī funkcija prasa divas cenas, aprēķina to summu un atgriež to.
def pirkums():
    a = int(input("Raksti vienu cenu"))  # Prasa pirmo cenu
    b = int(input("Raksti otru cenu"))  # Prasa otro cenu
    summa = a+b  # Aprēķina divu cenu summu
    print(f"Summa pirms atlaides {summa}")  # Izdrukā summu pirms atlaides
    return summa  # Atgriež summu

# Šī funkcija prasa atlaides apjomu procentos, aprēķina galīgo cenu, ņemot vērā atlaidi, un izdrukā to.
def atlaide():
    apjoms = input("Kāds ir atlaides apjoms %?").strip(" %")  # Prasa atlaides apjomu procentos
    apjoms_sk = atlaides_apjoms(apjoms)  # Pārveido atlaides procentu decimālformātā
    summa = pirkums()  # Iegūst divu cenu summu
    jamaksa = summa - summa * apjoms_sk  # Aprēķina galīgo cenu, ņemot vērā atlaidi
    print(f"Summa apmaksai {jamaksa}")  # Izdrukā galīgo cenu

# Šī funkcija pārveido atlaides procentu decimālformātā.
def atlaides_apjoms(apjoms):
    apjoms_sk = float(apjoms)/100  # Pārveido atlaides apjomu decimālformātā
    return apjoms_sk  # Atgriež atlaides apjomu decimālformātā

# sveiciens
# pirkums
# Izsauc funkciju, lai aprēķinātu galīgo cenu, ņemot vērā atlaidi
atlaide()