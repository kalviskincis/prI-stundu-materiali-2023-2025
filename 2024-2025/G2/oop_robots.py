class Robots:
    def __init__ (self, vards, baterija, jauns = True, darba_reizes = 0, uzlades_reizes = 0):
        self.vards = vards
        self.baterija = baterija
        self.jauns = jauns
        self.darba_reizes = darba_reizes
        self.uzlades_reizes = uzlades_reizes
        print(f"Robots {self.vards} ir izveidots.")

    def uzlade(self, laiks):
        self.uzlades_reizes += 1
        if self.baterija + laiks > 100:
            self.baterija = 100
        else:
            self.baterija += laiks
        print(f"Robots {self.vards} uzlādēts līdz {self.baterija}%.")
        
    def strada(self, laiks):
        if laiks > self.baterija:
            print("Nestrādāšu, nepietiek baterija.")
        else:
            self.baterija -= laiks
            self.jauns = False
            self.darba_reizes += 1
            print(f"Robots {self.vards} strādāja {laiks} minūtes.")

    def info(self):
        print(f"Vārds: {self.vards}, uzlāde: {self.baterija}%.")
        print(f"Ir jauns {self.jauns}, strādājis {self.darba_reizes}, uzlādēts {self.uzlades_reizes}.")



r1 = Robots("Kafijmeistars", 60)
r1.uzlade(30)
r1.strada(50)
r1.info()

print()

r2 = Robots("Zeķu savācējs", 90)
r2.info()
r2.strada(1)
r2.uzlade(41)
r2.info()
r2.strada(10)
r2.uzlade(11)
r2.strada(10)
r2.uzlade(5)
r2.strada(20)
r2.info()

