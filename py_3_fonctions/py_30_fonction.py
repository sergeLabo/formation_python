# replit_main

# # py_30_fonction.py


def multiplie(a, b):
    resp = a * b
    return resp

def ajoute(a, b):
    resp = a + b
    return resp
    print("perdu !")

m = multiplie(2, 2)
print("2 x 2 font", m)

a = ajoute(1, 1)
print("1 + 1 font", a)

# Calculer en utilisant les 2 fonctions
# r = (2 + 4) * (4.5 + 6)

"""
Définition:

a et b sont des arguments
Les noms des arguments sont à votre convenance.
Les arguments peuvent avoir des valeurs par défaut.
Si une fonction est appelée avec un nom d'argument,
les suivants doivent aussi être appelés avec leur nom

Une fonction sans return retourne None
"""

""" Exemple sans return """

# from datetime import datetime

# def quelle_heure_est_il():
    # print("maintenant =", datetime.now())

# print("il est", quelle_heure_est_il())




"""Arguments"""

def my_add(a=1, b=1, c=0, d=0):
    """Ajoute jusqu'à 4 nombres.
    Retourne la somme.
    """
    quelle_heure_est_il()
    resp = a + b + c + d
    return resp

# a = my_add(1, 2, 3, 4)
# a_faux = my_add(1, b=2, 3, 4)

# b = my_add(a=1, b=2, c=3, d=4)
# print(b)

# d = my_add(1, 2)
# print(d)
# e = my_add(1)
# print(e)

# # Trouver une fonction avec des noms d'arguments abscons
def monthy_python(plus, moins):
    resp = plus * moins
    return resp
