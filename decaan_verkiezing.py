from verkiezing import Kandidaat, Stem, Kiezer

class DecaanKandidaat(Kandidaat):
    def __init__(self, naam, opleiding):
        super().__init__(naam)
        self.opleiding = opleiding

    def __str__(self):
        return f"{self.naam} ({self.opleiding})"
    
class DecaanStem(Stem):
    def __init__(self, kandidaat, opleiding):
        super().__init__(kandidaat)
        self.opleiding = opleiding

    def __str__(self):
        return f"Stem op {self.kandidaat} ({self.opleiding})"
    
class DecaanKiezer(Kiezer):
    def __init__(self, naam, opleiding):
        super().__init__(naam)
        self.opleiding = opleiding

    def stem(self, kandidaat):
        if kandidaat.opleiding == self.opleiding:
            stem = DecaanStem(kandidaat, self.opleiding)
            kandidaat.geef_stem(stem)
            print(f"{self.naam} heeft gestemd op {kandidaat} ({self.opleiding})")
        else:
            print(f"{self.naam} kan niet stemmen op {kandidaat} ({kandidaat.opleiding})")

# Lijst van kandidaten
kandidaten = [
    DecaanKandidaat("Lies", "Toegepaste Informatica"),
    DecaanKandidaat("Tom", "Rechten")
]

# Lijst van kiezers
kiezers = [
    DecaanKiezer("Sanne", "Toegepaste Informatica"),
    DecaanKiezer("Joris", "Rechten"),
    DecaanKiezer("Luca", "Biologie")
]

# Laat kiezers stemmen
for kiezer in kiezers:
    for kandidaat in kandidaten:
        kiezer.stem(kandidaat)

# Toon resultaat
for kandidaat in kandidaten:
    print(f"{kandidaat} kreeg {len(kandidaat.stemmen)} stemmen.")
