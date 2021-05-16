ma_var = 1
ma_var_1 = 3.14159

ma_var = "bien"

def essai():
    pass

liste = [2.71828, abs(-9), essai, 0, 1]

print("liste[2]", liste[2])
print("liste[-2]", liste[-2])

liste.append(14)
liste.extend(("127.0.0.1", 8000))

print()
print("liste", liste)

print()
for item in liste:
    print(item)

print()
for i in range(len(liste)):
    print(liste[i])

print()
for item in liste:
    i = liste.index(item)
    print(liste[i])

dico = {"nom": "CAMUS", "prénom": "ALBERT", "profession": "auteur à succès"}

print()
for key, val in dico.items():
    print("clé", key, "valeur", val)
