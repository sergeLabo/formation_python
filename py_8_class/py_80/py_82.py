# replit_main

# # py_82.py

#### Jeu du retour_de_mauvaise_blague

from pi import return_mauvaise_blague

# Toutes les variables globales en majuscule
PI = 3.14159

# Ce retour_de_mauvaise_blague est une variable globale
retour_de_mauvaise_blague = return_mauvaise_blague()

def print_retour_de_mauvaise_blague(retour_de_mauvaise_blague):
    """retour_de_mauvaise_blague est une variable locale"""
    print(retour_de_mauvaise_blague)

def print_PI():
    print(PI)

def print_PI():
    global PI
    print(PI)

def print_a(a):
    print(a)

print_retour_de_mauvaise_blague(3)
print_PI()
print_a(3)
print_retour_de_mauvaise_blague(PI)
print_retour_de_mauvaise_blague(retour_de_mauvaise_blague)

# Renommer intelligement les objets
