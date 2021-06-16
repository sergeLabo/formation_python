# # py_17_elif_bissextile.py

print("Solution avec des elif")

annee = 1610

if annee % 400 == 0:
    bissex = True
elif annee % 100 == 0:
    bissex = False
elif annee % 4 == 0:
    bissex = True
else:
    bissex = False

if bissex:
    print(annee, "est bissextile") # Modifier avec des f-string
else:
    print(f"{annee} n'est pas bissextile")

# Ajouter des print() intermédiaires

# Dupliquer 3 fois

# Le prof: Introduction aux listes--> for in
