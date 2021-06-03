
# range = plage

a = range(5)
print("a =", a)

a = range(2, 10)
print("a =", a)

a = range(2, 10, 2)
print("a =", a)

a = range(0.1, 1, 0.2)
print("a =", a)

for b in a:
    print(b)

points = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]

# Calculer la moyenne des y (moyenne de la profondeur)

for point in points:
    print(point)

for ind in range(5):
    print(points[ind])

moyenne = (2 + 5 + 8 + 11 + 14)/5
print(moyenne)

# Créer une/des fonctions pour incrémenter de 1 chaque coordonnées
# toutes les secondes
# et calculer la moyenne
