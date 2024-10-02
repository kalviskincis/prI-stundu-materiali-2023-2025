edienkarte = {
"Baja Taco": 4.00,
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
    print(edienkarte["Nachos"]) # parādīt konkrētas atslēgas vērtību
    edienkarte["Nachos"] = 9.50 # mainām konkrētas atslēgas vērtību
    edienkarte["Pankūkas"] = 3 # izveidojam jaunu atslēgu vērtību pāri
    print(edienkarte)
    izvele = input("Ko ēdīsi?")
    print(edienkarte[izvele])

# atkartojums()

def pasutijums():
    summa = 0
    while True:
        try:
            izvele = input("Ko ēdīsi?").title()
            summa += edienkarte[izvele]
            print(summa)
        except KeyError:
            pass
        except EOFError:
            break

pasutijums()