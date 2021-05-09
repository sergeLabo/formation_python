""" Introduction aux dictionnaires

dictionnaire = ensemble d'éléments

les éléments sont un couple clé: valeur = { clé: valeur }

{ clé: valeur , clé: valeur, clé: valeur .... }

un dictionnaire n'est pas ordonné
"""

dico = {
        2: "première valeur",
        1: ("localhost", 8888)
        }
print("mon premier dict", dico)

""" Les virgules permettent toujours d'aller à la ligne """

# Ajout d'un item
dico[3] = "toto"
dico[2] = None
print("un dict plus grand", dico)

"""Parcours d'un dictionnaire"""
for key, value in dico.items():
    print("key", key, "value", value)

config = {  "network":  {
                        "ip": "127.0.0.1",
                        "port": 8003
                        },
            "image":    {
                        "width": 1280,
                        "height": 720,
                        "mode": "gray"
                        }
            }

print("\nconfig pas pretty:", config)

import pprint
pp = pprint.PrettyPrinter(indent=4)
print("\n\nDictionnaire imprimé avec pprint:\n")
pp.pprint(config)
