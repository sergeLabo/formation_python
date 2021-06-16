# # py_34_return_predefinie.py

"""
Fonctionnement et importance du return
et quelques fonctions prédéfines.
"""

def test(a):
    if a < 0:
        print("a < 0")
        return 1
    else:
        print("a > 0")
        return 0
    print("fin")

test(1)
test(-1)

# Fonctions prédéfinies
# print( abs(-20),
       # max(2, 50),
       # int(str(1)),
       # type(int(str(1))),
       # dir(1))
