
"""
Sensibilisation aux valeurs en mémoire(RAM), appelées par
    - un numéro dans la RAM
    - un pointeur, un lien
"""
a = 73
b = a
print(b)
a = 1
print(b)

a = [0, 1]
b = a
print("a =", a, "b =", b)

a[0] = "toto"
print("a =", a, "b =", b)

a[0] = "toto"
print("a =", a, "b =", b)

# Création de liste pour les articulations du squelette
# #l = [[0]*3]*18
# #l[17][0] = 0.123
# #print(l)

# Ah mais là c'est bon !
# #a = 1
# #m = [a]*3
# #m[2] = 2
# #print(m)

# ## Copie de liste
# #l = [1, 2, 3]
# #print("type(l) =",type(l), "l =", l)
# ## la copie pointe vers d'autres valeurs en mémoire
# #t = l.copy()

"""faire essai en terminal"""
