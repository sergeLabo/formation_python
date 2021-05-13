
port = 0
ip = ""

# tuple
address = (ip, port)
# ou
address = (ip,
           port)
"""
En mathématiques, si n est un entier naturel, alors un n-uplet ou n-uple est une
collection ordonnée de n objets, appelés « composantes » ou « éléments » ou
« termes » du n-uplet.

L'utilisation du terme anglais tuple, suffixe de quin-tuple/sex-tuple/…, est
courante dans des ouvrages de programmation informatique en français.
"""

# un tuple est immuable, en EN immutable
address[0] = "chez moi"

address = ("chez moi", port)
print("address", address)

# Sans (), très souvent fait mais déconseillé
address = ip, port

# Affectation de valeurs
a, b = ip, port
c = a, b
print("type(c)", type(c))

liste = [1, 2]
liste.extend((8, 5))
print("liste", liste)
