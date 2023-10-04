# Šī funkcija prasa lietotājam ievadīt savu vārdu un izdrukā sveicienu.
def sveiciens():
    vards = input("Kā tevi sauc?")
    print(f"Labdien, {vards}!")

# Šī funkcija prasa lietotājam ievadīt divu preču cenas, aprēķina to summu un izdrukā to.
def pirkums():
    cena1 = int(input("Cik maksā 1. prece?"))
    cena2 = int(input("Cik maksā 2. prece?"))
    summa = cena1 + cena2
    print(f"Pirkuma summa ir {summa}.")
    return summa

# Šī funkcija prasa lietotājam ievadīt atlaidi procentos, pēc tam aprēķina gala summu pēc atlaides piemērošanas un izdrukā to.
def atlaides_aprekins():
    atlaide = input("Cik % ir atlaide?").replace(",", ".").strip(" %")
    atlaide_decimal = atlaides_parveidosana(atlaide)
    summa = pirkums()
    jamaksa = summa - summa * atlaide_decimal
    print(f"Summa pēc atlaides piemērošanas {jamaksa}.")

# Šī funkcija pārveido atlaidi procentos decimālformātā.
def atlaides_parveidosana(atlaide):
    atlaide_decimal = float(atlaide)/100
    return atlaide_decimal

# sveiciens()
# pirkums()
atlaides_parveidosana()