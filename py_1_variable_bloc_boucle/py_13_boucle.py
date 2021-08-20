# # py_13_boucle.py

# Boucle simple
n= 0
while n < 5:
    print(n)
    n += 1


# 2 boucles imbriquées
n= 0
while n < 5:

    p = 0
    while p < 3:
        print("boucle", n, p)
        p += 1

    n += 1
