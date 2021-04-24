
print("Solution avec des elif")

annee = 400

if annee % 400 == 0:
elif annee % 100 == 0:
    bissex = False
elif annee % 4 == 0:
    bissex = True
else:
    bissex = False

# Modifier avec des f-string
if bissex:
    print("{} est bissextile".format(annee))
else:
    print("{} n'est pas bissextile".format(annee))

# Dupliquer 3 fois
# Ajouter des print() intermédiaires
