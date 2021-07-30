# # py_82.py

# Sans class
# dictionnaire
contact = { "manu": { "name": "manu",     "tel": "01 02 03 "},
            "bj":   { "name": "benj", "adresse": "labomedia" } }

contact["serge"] = {"hobby", "python"}

for key, val in contact.items():
    print("qui:", key, ", data", val)
print("\n\n")

# Object
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
# #print("Mon nom est:", c.name) # c'est fait exprès


# Object dans un dict
# emmanuel = Contact("Emmanuel")
# jean = Contact("Jean")

# Objects dans une liste
# mes_contacts = [emmanuel, jean]

# Objects dans un dictionnaire
# mon_carnet = {  "emmanuel": emmanuel,
                # "jean":     jean}

# print("mon_carnet", mon_carnet)

# Plus structuré
# copains = ["Emmanuel", "Jean"]
# mon_carnet = {}
# for copain in copains:
    # mon_carnet[copain] = Contact(copain)
# print("mon_carnet", mon_carnet)

# print(mon_carnet["Jean"])

# mon_carnet['Emmanuel'].set_phone("djembé")

# print("Le numéro de Emmanuel est", mon_carnet['Emmanuel'].get_phone())
