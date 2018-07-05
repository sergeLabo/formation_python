# Programme testant si une année est bissextile

# Demande de l'année au clavier
annee =  input("Saisissez votre année ...")  # attente de la saisie

# Si saisie n'est pas un entier
annee = int(annee)

# Pour éviter d'avoir une erreur de variable non définie
# Si bissextile, bissex = True
bissex = False

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
            
if bissex:
    print("{} est bissextile".format(annee))
else:
    print("{} n'est pas bissextile".format(annee))

# Autre solution
print("Solution avec des elif")

# j'écrase la valeur du 1er calcul
bissex = False

if annee % 400 == 0:
    bissex = True
elif annee % 100 == 0:
    bissex = False
elif annee % 4 == 0:
    bissex = True
else:
    bissex = False

if bissex:
    print("{} est bissextile".format(annee))
else:
    print("{} n'est pas bissextile".format(annee))  
