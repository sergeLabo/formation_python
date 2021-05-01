
"""
    Programmation impérative, le paradigme originel et le plus courant
        Programmation structurée, visant à structurer les programmes impératifs
            pour en supprimer les instructions goto
        Programmation procédurale, à comparer à la programmation fonctionnelle
    Programmation orientée objet
"""

def is_bissex(annee):
    """Calcule si une année est bissextile ou pas.
    Retourne True ou False
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
