ma_var = 1
ma_var_1 = 3.14159

ma_var = "essai"

def essai():
    pass

# list
liste = [2.71828, abs(-9), essai, 0, 1]
#           0        1       2    3  4
print("liste[2]", liste[2])
print("liste[-2]", liste[-2])

# assignation
liste[0] = -1.0

liste.append(14)
liste.extend(["127.0.0.1", 8000])

print("\n-----------------------------------------1")
print("liste", liste)

print("\n-----------------------------------------2")
for item in liste:
    print(item)

print("\n-----------------------------------------3")
for i in range(len(liste)):
    print(liste[i])

print("\n-----------------------------------------4")
for item in liste:
    i = liste.index(item)
    print(liste[i])

# dict
dico = {"nom": "CAMUS", "prénom": "ALBERT", "profession": "auteur à succès"}

print("\n-----------------------------------------5")
for key, val in dico.items():
    print("clé", key, "valeur", val)

k = [x for x in dico.keys()]
k = sorted(k)
print(dico.keys())
print(k)

if "labomedia" in dico:
    print("vive")

if "labomedia" in liste:
    print("les")

if "labomedia" not in liste:
    print("open ateliers")

if ma_var is not None:
    print("de la ")

if ma_var:
    # ma_var is not si ma_var = [] ou {} ou "" ou () ou 0 ou 0.0
    if not ma_var:
        print("labomedia")

tuple_ = tuple(liste)
# #tuple_[0] = 0
tuple_ = (0, 9, essai, 0, 1, 14, '127.0.0.1', 8000)

def somme(a, b):
    """Fait la somme de a et b,
    retourne la somme si a et b sont entiers
    None sinon
    """
    if isinstance(a, int) and isinstance(b, int):
        return a + b

print(somme(1, 1))
print(somme(1.0, 1))
somme(a=1, b=2)
somme(1, b=2)
#somme(a=1, 2)
