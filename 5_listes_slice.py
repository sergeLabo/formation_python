
# dans https://www.python.org/shell

liste = [1, 2, 3, 4, 5]
#        0  1  2  3  4
# On compte à partir de zéro
liste[1] = 2
liste[0] = 1

suite = [5, 6, 7, 21.3, "oh!", [3.21, 1478000]]
liste.extend(suite)
liste.append(3.14159)
print(f"la liste a {len(liste)} éléments")

liste = [1, 2, 3, 4, 5, 5, 6, 7, 21.3, 'oh!', [3.21, 1478000], 3.14159]
# Faire des slices dans l'interpréteur
part = liste[3:6]
print(part)
# liste[-1]
# liste[-3]
# liste[3:-2]
