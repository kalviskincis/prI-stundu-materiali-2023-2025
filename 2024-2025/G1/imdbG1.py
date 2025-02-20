import sqlite3
# Noliec šo failu tajā pašā mapē, kur atrodas datubāzes fails!

def main():
    print("Programma ļauj apskatīt filmu datubāzi un veikt dažādas darbības ar tās ierakstiem.")
    with sqlite3.connect("imdbG1.db") as conn:
        c = conn.cursor()

    izvele(c)

def izvele(c):
    print("Izvēlies darbību:")
    while True:
        print("1. Apskatīt visu tabulu\n2. Meklēt nosaukuma fragmentu\n3. Meklēt pēc reitinga\n4. Pievienot jaunu filmu\n5. Dzēst filmu\n6. Labot filmas reitingu\n7. Beigt darbu")
        izvele = input("Tava izvēle: ")
        if izvele not in ["1", "2","3","4","5","6","7"]:
            print("Nederīga ievade")
            continue
        if izvele == "1":
            paradit_visu(c)
        elif izvele == "2":
            nosaukums = input("Ievadi nosaukuma fragmentu: ")
            meklet_nosaukumu(c, nosaukums)
        elif izvele == "3":
            reitings = input("Ievadi reitingu: ")
            meklet_reitingu(c, reitings)
        elif izvele == "4":
            pievienot(c)
        elif izvele == "5":
            dzest(c)
        elif izvele == "6":
            labot(c)
        elif izvele == "7":
            break


def paradit_visu(c):
    c.execute("SELECT * FROM imdb_top250") # izpilda vaicājumu
    atbilde = c.fetchall() # Iegūst visus vaicājuma rezultātus. Ir arī fetchone(), kurš iegūst 1. rezultātu
    for rinda in atbilde:
        print(rinda)

def meklet_nosaukumu(c, nosaukums):
    c.execute(f"SELECT * FROM imdb_top250 WHERE nosaukums LIKE \"%{nosaukums}%\"")
    atbilde = c.fetchall() 
    for rinda in atbilde:
        print(rinda)

def meklet_reitingu(c, reitings):
    c.execute(f"SELECT * FROM imdb_top250 WHERE reitings >= {reitings} ")
    atbilde = c.fetchall() 
    for rinda in atbilde:
        print(rinda)

def pievienot():
    try:
        vieta = int(input("Ievadi filmas vietu: "))
        nosaukums = input("Ievadi filmas nosaukumu: ")
        gads = int(input("Ievadi filmas izlaišanas gadu: "))
        reitings = float(input("Ievadi filmas reitingu: "))
        skaits = input("Ievadi filmas vērtētāju skaitu: ")
        ilgums = int(input("Ievadi filmas ilgumu minūtēs: "))
        ierobezojumi = input("Ievadi filmas ierobežojumus: ")
    except ValueError:
        print("Nederīga ievade")
        

def dzest(c):
    nosaukums = input("Ieraksti nosaukumu, kuru dzēst")
    c.execute(f"DELETE FROM imdb_top250 WHERE nosaukums = \"{nosaukums}\" ")

def labot():
    pass


if __name__ == "__main__":
    main()