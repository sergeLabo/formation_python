
liste = [1, 2, 3, 4, 5]
#        0  1  2  3  4
# On compte à partir de zéro
liste[1] = 2
liste[0] = 1

suite = [5, 6, 7, 21.3, "oh!", [3.21, 1478000]]
liste.extend(suite)
liste.append(3.14159)
print(f"la liste a {len(liste)} éléments")
part = liste[3:6]
print(part)

# Faire des slices
