from verkiezing import Kandidaat, Stem, Kiezer

class RectorKandidaat(Kandidaat):
    def __init__(self, naam, faculteit):
        super().__init__(naam)
        self.faculteit = faculteit

    def __str__(self):
        return f"{self.naam} (Rector: {self.faculteit})"
    
class RectorStem(Stem):
    def __init__(self, kandidaat, faculteit):
        super().__init__(kandidaat)
        self.faculteit = faculteit

    def __str__(self):
        return f"Stem op {self.kandidaat} (Rector: {self.faculteit})"

class RectorKiezer(Kiezer):
    def __init__(self, naam, faculteit):
        super().__init__(naam)
        self.faculteit = faculteit

    def stem(self, kandidaat):
        if kandidaat.faculteit == self.faculteit:
            stem = RectorStem(kandidaat, self.faculteit)
            kandidaat.geef_stem(stem)
            print(f"{self.naam} heeft gestemd op {kandidaat} (Rector: {self.faculteit})")
        else:
            print(f"{self.naam} kan niet stemmen op {kandidaat} (andere faculteit)")

# Lijst van kandidaten
kandidaten = [
    RectorKandidaat("Jan", "Ingenieurswetenschappen"),
    RectorKandidaat("Sofie", "Geneeskunde")
]

# Lijst van kiezers
kiezers = [
    RectorKiezer("Emma", "Ingenieurswetenschappen"),
    RectorKiezer("Mohammed", "Geneeskunde"),
    RectorKiezer("Karel", "Rechten")  # mag op niemand stemmen
]

# Laat elke kiezer stemmen op alle kandidaten
for kiezer in kiezers:
    for kandidaat in kandidaten:
        kiezer.stem(kandidaat)

# Toon resultaten
for kandidaat in kandidaten:
    print(f"{kandidaat} kreeg {len(kandidaat.stemmen)} stemmen.")
