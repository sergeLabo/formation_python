# replit_main ok

# # py_31_fonction_bissextile.py

"""
Créer une fonction qui retourne
    True si bissextile
    False sinon

Utiliser la fonction avec une liste de date
"""

if annee % 400 == 0:
    bissex = True
elif annee % 100 == 0:
    bissex = False
elif annee % 4 == 0:
    bissex = True
else:
    bissex = False
