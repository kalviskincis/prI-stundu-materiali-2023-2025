class Robots:

    def __init__ (self, vards, baterija, jauns=True, uzlades_reizes=0, darba_reizes=0):
        self.vards = vards
        self.baterija = baterija
        self.jauns = jauns
        self.uzlades_reizes = uzlades_reizes
        self.darba_reizes = darba_reizes
        print(f"Robots {self.vards} ir izveidots.")

    def uzlade(self, laiks):
        self.uzlades_reizes += 1
        if self.baterija + laiks > 100:
            self.baterija = 100
        else:
            self.baterija += laiks
        print(f"Robots {self.vards} uzlādēts līdz {self.baterija}.")

    def strada(self, laiks):
        if self.baterija - laiks >= 0:
            self.baterija -= laiks
            self.darba_reizes += 1
            self.jauns = False
            print(f"Robots pastrādāja {laiks} minūtes.")
        else:
            print(f"Nepietiek jaudas")      

    def statuss(self):
        print(f"Robots {self.vards}, uzlādes līmenis {self.baterija}%.")
        print(f"Jauns {self.jauns}, strādājis {self.darba_reizes}.")




r1 = Robots("Putekļusūcējs", 75)
r1.uzlade(45)
r1.strada(15)
r1.statuss()

print()

r2 = Robots("Logu mazgātājs", 0)
r2.strada(10)
r2.strada(20)
r2.statuss()
r2.uzlade(20)
r2.statuss()

print()

r3 = Robots("Zeķu savācējs", 10, False, 120, 200)
r3.statuss()
