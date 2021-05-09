
""" Fonctions: Pourquoi créer des fonctions ?

    Pour éviter les répétitions, sources d'erreurs, surtout si une modifications
        de ces répétitions est nécessaire.
    Pour structurer le projet.
    Tester séparément des bouts de code, quand il marche,
        on est  sûr que l'erreur ne vient pas de cette fonction.
    Travailler à plusieurs.
    Ces bouts de code peuvent être dans des fichiers différents, ce qui est
        important quand le code est très long.
    Pour éviter les problèmes avec les variables globales.
    Pour pouvoir réutiliser des bouts de codes.
"""

def multiplie(a, b):
    resp = a * b
    return resp

def ajoute(a, b):
    resp = a + b
    return resp

m = multiplie(2, 2)
print("2 x 2 font", m)

a = ajoute(1, 1)
print("1 + 1 peuvent faire", 1 + a)

# Calculer en utilisant les 2 fonctions
# r = (2 + 4) * (4.5 + 6)

"""
Définition:

a et b sont des arguments
les noms des arguments sont à votre convenance
les arguments peuvent avoir des valeurs par défaut
si une fonction est appelée avec un nom d'argument,
les suivants doivent aussi être appelés avec leur nom

Une fonction sans return retourne None

La philosophie du codeur:

    Une fonction fait une chose.
"""

""" Exemple sans return """

from datetime import datetime

def quelle_heure_est_il():
    print(datetime.now())

print("il est", quelle_heure_est_il())
quelle_heure_est_il()

"""Arguments"""

def my_add(a=1, b=1, c=0, d=0):
    """Ajoute jusqu'à 4 nombres.
    Retourne la somme.
    """
    quelle_heure_est_il()
    resp = a + b + c + d
    return resp

# #a = my_add(1, 2, 3, 4)
# #a_faux = my_add(1, b=2, 3, 4)

# #b = my_add(a=1, b=2, c=3, d=4)
# #print(b)

# #d = my_add(1, 2)
# #print(d)
# #e = my_add(1)
# #print(e)

# ## Trouver une fonction avec des noms d'arguments abscons
def monthy_python(plus, moins):
    resp = plus * moins
    return resp
