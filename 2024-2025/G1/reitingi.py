class Dziesma:
    def __init__(self, nosaukums, reitings):
        self.nosaukums = nosaukums
        self.reitings = reitings

    def atjaunot_reitingu(self, jauns_reitings):
        # NEEEEEEEEEEEE input
        self.reitings = jauns_reitings

dz = Dziesma("Zvaniņš skan", 5)
# jauns_reitings = int(input("Kāds tagad r.?"))
dz.atjaunot_reitingu(3)

