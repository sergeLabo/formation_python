# # py_16_si_sinon_bissextile.py
# Programme testant si une année est bissextile
# Tester avec différentes années
# Ajouter des print()

"""
Si une année n'est pas multiple de 4, elle n'est pas bissextile
Si elle est multiple de 4, on regarde si multiple de 100
    Si oui, on regarde si multiple de 400
        Si oui, elle est bissextile
        Si non, elle n'est pas bissextile
    Si non, elle est bissextile
"""

annee =  1454

if annee % 4 == 0:
    if annee % 100 == 0:
        if annee % 400 == 0:
            bissex = True
        else:
            bissex = False
    else:
        bissex = True
else:
    bissex = False

# Avec f-string, à partir de python 3.6
if bissex:
    print(f"{annee} est bissextile")
else:
    print(f"{annee} n'est pas bissextile")

# Sans f-string
# if bissex:
    # print(annee, "est bissextile")
# else:
    # print(annee, "n'est pas bissextile")
