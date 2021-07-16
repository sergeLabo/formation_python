# # py_82.py

#### Jeu du pi

from pi import pi as pipi

# Toutes les variables globales en majuscule
PI = 3.14159

# Ce pi est une variable globale
pi = pipi()

def print_pi(pi):
    """pi est une variable locale"""
    print(pi)

def print_PI():
    print(PI)

def print_PI():
    global PI
    print(PI)

def print_a(a):
    print(a)

print_pi(3)
print_PI()
print_a(3)
print_pi(PI)
print_pi(pi)

# Renommer intelligement les objets
