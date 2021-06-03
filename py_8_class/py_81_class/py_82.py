

class Bicycle:
    """Un vélo"""

    def __init__(self, color, kind):
        """C'est le constructeur"""

        # self.color = color
        self.col = color

        self.kind = kind

        self.pierre_soulages()

    def pierre_soulages(self):
        self.col += " foncé"


def pierre_soulages(color):
    return color + " clair"


my_bicycle = Bicycle("rouge", "vtt")
print(f"la couleur de mon velo rouge est {my_bicycle.col}")
print(f"il est du type {my_bicycle.kind}")

# c = pierre_soulages("rose")
# print("pierre_soulages(rose) =", c)

# my_bicycle.pierre_soulages()
# print("la couleur de mon velo rouge est", my_bicycle.col)
