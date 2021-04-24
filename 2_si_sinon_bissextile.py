# Programme testant si une année est bissextile

# Demande de l'année au clavier
annee =  input("Saisissez votre année ...")  # attente de la saisie
print("type de annee", type(annee))
annee = int(annee)

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
    print(f"{annee} est bissextile")
else:
    print(f"{annee} n'est pas bissextile")
