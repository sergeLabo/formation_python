
""" Introduction aux class, appelée POO programation orientée objet

Présentation des scripts mnist

Une class permet de créer des objets.
Un objet est un machin:    une voiture, un moteur, une fleur,
                            un amour, un modèle d'IA, un encodeur_decodeur ....

Un objet a des méthodes et des attributs
    - une méthode est une fonction propre (c'est le self !!!)  à l'objet
    - un attribut est une variable qui appartient à cet objet

"""


class Subliminale:
    pass

s = Subliminale()
print(f"Le type de s = Subliminale() est {type(s)}")
print("dir(s)", dir(s))

class Minimale:
    print("Un objet Minimale créé !")


m = Minimale()
print("m", m)


class MyTest:
    def my_test(self):  # propre à l'objet
        """Pourquoi self?"""
        print("Premier test")


class Bicycle:
    """Un vélo"""

    def __init__(self, color, kind):
        """C'est le constructeur"""

        self.color = color
        self.kind = kind
        a = self.pierre_soulages()
        print("pierre soulages =", a)

    def pierre_soulages(self):
        self.color = "noir"


def pierre_soulages(new_color):
    return new_color

c = pierre_soulages("rose")
print(c)

b = Bicycle("rouge", "vtt")
print(f"la couleur de mon velo rouge est {b.color}")
print(f"il est du type {b.kind}")


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

copains = ["Emmanuel", "Jean"]
mon_carnet = {}
for copain in copains:
    mon_carnet[copain] = Contact(copain)
mon_carnet['Emmanuel'].set_phone("djembé")

print(f"Le numéro de Emmanuel est {mon_carnet['Emmanuel'].get_phone()}")
