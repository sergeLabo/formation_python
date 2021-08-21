# replit_main

# # py_41_dictionnaire.py

""" Introduction aux dictionnaires

dictionnaire = ensemble d'éléments

les éléments sont un couple clé: valeur = { clé: valeur }

{ clé: valeur , clé: valeur, clé: valeur .... }

un dictionnaire n'est pas ordonné !
"""

dico = {
        2                : "première valeur",
        1                : ("localhost", 8888),
        "nom"            : "mon réseau",
        # [0, 1]         : "raté",
        56.45            : 1056.45,
        (127.0.0.1, 1000): "reseau 1"
        }

print("mon premier dict", dico)

""" Les virgules permettent toujours d'aller à la ligne

L'accès à un éléments se fait comme pour une liste, mais
ce n'est pas un index, la valeur est cappelée par la clé

"""

# Ajout d'un item
dico[3] = "toto"

# Mise à jour d'un item
dico[2] = None
dico["nom"] = "pierre"

print("notre dict mis à jour:", dico)

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

d = {0: 0, 1: 1}
print(d)
d[0] = 2
print("ce n'est pas l'index 0:", d[0])
d[0.5] = 2
print(d)
