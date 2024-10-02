def main():
    eiro = cena_uz_float(input("Cik maksāja maltīte? "))
    procenti = procenti_uz_float(input("Cik procentus vēlies atstāt dzeramnaudā? "))
    try:
        atstat = eiro * procenti
        print(f"Atstāj €{atstat:.2f}")
    except TypeError:
        print("Nevarēju veikt aprēķinus. Nepareizi dati.")

def cena_uz_float(e):
    try:
        eiro = float(e.strip("€"))
        return eiro
    except ValueError:
        print("Netika ievadīta korekta vērtība.")

def procenti_uz_float(p):
    try:
        procenti = float(p.strip("%"))/100
        return procenti
    except ValueError:
        print("Netika ievadīta korekta vērtība.")

if __name__ == "main":
   main()