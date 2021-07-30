# # py_82.py


class Bicyclette:
    """Un vélo"""

    def __init__(self, color, genre):

        # self.color = color
        self.col = color

        self.genre = genre

        self.pierre_soulages()

    def pierre_soulages(self):
        self.col += " foncé"

    def je_roule_avec_mon_velo

def pierre_soulages(color):
    return color + " clair"


ma_bicyclette = Bicyclette("rouge", "vtt")
print(f"la couleur de mon velo rouge est {ma_bicyclette.col}")
print(f"il est du type {ma_bicyclette.genre}")

# c = pierre_soulages("rose")
# print("pierre_soulages(rose) =", c)

# ma_bicyclette.pierre_soulages()
# print("la couleur de mon velo rouge est", ma_bicyclette.col)
