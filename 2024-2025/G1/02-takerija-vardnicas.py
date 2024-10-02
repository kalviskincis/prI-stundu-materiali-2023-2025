edienkarte = {"Baja Taco": 4.00,
"Burrito": 7.50,
"Bowl": 8.50,
"Nachos": 11.00,
"Quesadilla": 8.50,
"Super Burrito": 8.50,
"Super Quesadilla": 9.50,
"Taco": 3.00,
"Tortilla Salad": 8.00
}

def atkartojums():
    print(edienkarte["Taco"]) # piekļūst konkrētai vērtībai
    edienkarte["Taco"] = 2.50 # mainām vai piešķiram vērtību
    print(edienkarte["Taco"])
    edienkarte["Ķirbju zupa"] = 5
    print(edienkarte)
    izvele = input("Ko vēlies ēst?")
    print(edienkarte[izvele])


def pasutijums():
    summa = 0
    while True:
        try:
            izvele = input("Ko vēlies ēst?").title()
            summa += edienkarte[izvele]
            print(summa)
        except EOFError:
            break
        except KeyError:
            continue

pasutijums()

