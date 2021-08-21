# replit_main

# # py_33_multiples_fonctions.py


def is_bissex(annee):
    """Calcule si une année est bissextile ou pas.
    Retourne True ou False.
    """

    if annee % 400 == 0:
        bissex = True
    elif annee % 100 == 0:
        bissex = False
    elif annee % 4 == 0:
        bissex = True
    else:
        bissex = False

    return bissex

def main():
    annees = [21123, 5454]
    for annee in annees:
        b = is_bissex(annee)
        print(b)

main()
