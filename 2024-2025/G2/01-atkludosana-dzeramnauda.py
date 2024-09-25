def main():
    eiro = cena_uz_float(input("Cik maksāja maltīte? "))
    procenti = procenti_uz_float(input("Cik procentus vēlies atstāt dzeramnaudā? "))
    atstat = eiro * procenti
    print(f"Atstāj ${atstat:.2f}")

def cena_uz_float(e):
    eiro = float(e.strip("$"))
    return eiro

def procenti_uz_float(p):
    procenti = float(p.strip("%"))/100
    return procenti

main()