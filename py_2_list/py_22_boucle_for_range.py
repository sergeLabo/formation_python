# # py_22_boucle_for_range.py

""" Parcours de liste """

liste = [1, 2, 3, 4, 5, 5, 6, 7, 21.3]
#        0  1  2  3  4  5  6  7  8

# print(len(liste))
# print(liste[10])

"""Parcours"""

# for item in liste:
    # print(item)

# for entier in range(5):
    # print(entier)

# for entier in range(5, 10, 2):
    # print("ttt", entier)

# for i in range(len(liste)):
    # print(liste[i])

for i, item in enumerate(liste):
    print("enumerate", i, item)


""" Liste de listes """
points = [  [12.3, 45],
            [-0.123, 81.74],
            [2.3, 7.45],
            [-0.012, -56.145],
            [2, 1]]

print(points[0][0])
print(points[0][1])

# for point in points:
    # print("Un point =", point, "avec coordonnées du point:", point[0], point[1])

"""Excercices"""
# faire idem print précédent avec i in range()

# # Faire avec for point in points: avec
points = [  [12.3, 45],
            None,
            [-0.123, 81.74],
            [2.3, 7.45],
            [-0.012, -56.145],
            None,
            [2, 1]
        ]
