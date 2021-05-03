""" Introduction aux dictionnaires

dictionnaire = ensemble de clé: valeur = { clé: valeur }

{ clé: valeur , clé: valeur, clé: valeur .... }

un dictionnaire n'est pas ordonné
"""

dico = {
        1: "première valeur",
        2: ["localhost", 8888]
        }
print(dico)

""" Les virgules permettent toujours d'aller à la ligne """

# Ajout d'un item
dico[3] = "toto"
dico[2] = None
print(dico)

"""Parcours d'un dictionnaire"""
for key, value in dico.items():
    print(key, value)

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

import pprint
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(config)
