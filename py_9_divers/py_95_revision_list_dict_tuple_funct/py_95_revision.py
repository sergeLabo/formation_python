# replit_main

# #i = 12
# #ma_var = 1
# #ma_var_1 = 3.14159

# #ma_var = "essai"

# bloc

# ## if puis while
# #while i < 3:
    # #print(i)
    # #i += 1
# #print("fin")

# #if i % 2 == 0:
    # #print("pair")
# #else:
    # #print("impair")
# #i = 3


# #if i % 3 == 0:
    # #print("multi 3")
    # #if i == 2:
        # #print("ok")
    # #elif i == 3:
        # #print("3")

# #elif i % 4 == 0:
    # #print("multi 4")


# #else:
    # #print("j'ai besoin d'un café")


# #def essai():
    # #pass


# ## list
liste = [2.71828, abs(-9), 3.14, 0, 1]
#           0        1       2    3  4
#                                -2   -1
# #print("liste[0]", liste[0])
# #print("liste[-2]", liste[-2])

# assignation
# #liste[0] = -1.0
# #print(liste)
# #liste.append(14)
# #liste.append(["127.0.0.1", 8000])
# #print(liste)

# #print("\n-----------------------------------------1")
# #print("liste", liste)

# #print("\n-----------------------------------------2")
# #for aa in liste:
    # #print(aa)

# #print("\n-----------------------------------------3")
# #for i in range(len(liste)):
    # #print(liste[i])

# #print("\n-----------------------------------------4")
# #for item in liste:
    # #i = liste.index(item)
    # #if i == 2:
        # #print(liste[i])

# #dict
name = "nom"
dico = {
            name: "CAMUS",
            "prénom": "ALBERT",
            "profession": "auteur à succès"
        }

dico1 = {
            1: "CAMUS",
            2: "ALBERT",
            3: "auteur à succès"
        }
bb = "nom"
# #print(dico[bb])


# #for key, val in dico.items():
    # #print("clé", key, "valeur", val)

# #k = [x for x in dico.keys()]
# #k = sorted(k)
# #print(dico.keys())
# #print(k)

# #if "auteur à succès" in dico:
    # #print("vive")

# #if "labomedia" in liste:
    # #print("les")

# #if "labomedia" not in liste:
    # #print("vive les open ateliers")

# #ma_var = None
# #print(type(type))
# #print("ma_var", ma_var)

# #if ma_var is not None:
    # #print("de la ")


# #if ma_var:
    # ## ma_var is not si ma_var = [] ou {} ou "" ou () ou 0 ou 0.0
    # #if not ma_var:
        # #print("labomedia")

# #tuple_ = tuple(liste)
# #print(tuple_)
# #tuple_[0] = 0
# #tuple_ = (0, 9, 3.14, 0, 1)
# #print(tuple_)

def somme(a, c, b=1):
    """Fait la somme de a et b,
    retourne la somme si a et b sont entiers
    None sinon
    """
    if isinstance(a, int) and isinstance(b, int):
        return a + b

print(somme(3, 5))

# #print(somme(1, 1))
# #print(somme(1.0, 1))
# #somme(a=1, b=2)
# #somme(1, b=2)
# #somme(a=1, 2)
