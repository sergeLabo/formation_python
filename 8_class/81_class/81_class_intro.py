

### Construire une  class
class Subliminale:
    pass

s = Subliminale()
print(f"Le type de s = Subliminale() est {type(s)}")
print("dir(s)", dir(s))
print("\n\n")

class Minimale:
    print("Un objet Minimale créé !")


m = Minimale()
print("m", m)
print("\n\n")



class MyTest:
    def my_test(self):  # propre à l'objet
        """Pourquoi self?"""
        print("Premier test")
print("\n\n")


class Bicycle:
    """Un vélo"""

    def __init__(self, color, kind):
        """C'est le constructeur"""

        # self.color = color
        self.col = color

        self.kind = kind

        # a = self.pierre_soulages()
        # print("pierre soulages =", a)

    def pierre_soulages(self):
        self.col = "noir"


def pierre_soulages(new_color):
    return new_color


my_bicycle = Bicycle("rouge", "vtt")
print(f"la couleur de mon velo rouge est {my_bicycle.col}")
print(f"il est du type {my_bicycle.kind}")

# my_bicycle.pierre_soulages()
# print("la couleur de mon velo rouge est", my_bicycle.col")

# c = pierre_soulages("rose")
# print("pierre_soulages(new_color):", c)



class Contact:

    def __init__(self, name):
        self.name = name
        self.phone = None

    def set_phone(self, phone):
        self.phone = phone

    def get_phone(self):
        return self.phone

c = Contact("toto")
print(f"Le numéro de toto est {c.get_phone()}")

# copains = ["Emmanuel", "Jean"]
# mon_carnet = {}
# for copain in copains:
    # mon_carnet[copain] = Contact(copain)
# print("mon_carnet", mon_carnet)

# print(mon_carnet["Jean"])

# mon_carnet['Emmanuel'].set_phone("djembé")

# print("Le numéro de Emmanuel est", mon_carnet['Emmanuel'].get_phone())
