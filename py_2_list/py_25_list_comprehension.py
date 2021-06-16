# # py_25_list_comprehension.py

"""List Comprehension

Définitions de compréhension en Logique
    Ensemble des caractères propres à un concept.
"""

a = 0
if a == 0: print(a)

liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
pair = [p for p in liste if p % 2 == 0]
print(pair)

# liste = [j for j in range(10) if j %2 == 0]
# print("fin: ", liste)
