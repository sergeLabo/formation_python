

class Contact:

    def __init__(self, name):
        # self.name = name
        self.phone = None

    def set_phone(self, phone):
        self.phone = phone

    def get_phone(self):
        return self.phone

c = Contact("toto")
print("Le numéro de toto est :", c.get_phone())
print("Mon nom est:", c.name)

# copains = ["Emmanuel", "Jean"]
# mon_carnet = {}
# for copain in copains:
    # mon_carnet[copain] = Contact(copain)
# print("mon_carnet", mon_carnet)

# print(mon_carnet["Jean"])

# mon_carnet['Emmanuel'].set_phone("djembé")

# print("Le numéro de Emmanuel est", mon_carnet['Emmanuel'].get_phone())
