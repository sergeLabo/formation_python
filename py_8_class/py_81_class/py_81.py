# # py_81.py

#### Class intro

### Construire une  class
class Subliminale:
    pass

s = Subliminale()
print(f"Le type de s = Subliminale() est {type(s)}")
print("dir(s)", dir(s))
print("\n\n")

class Minimale:
    print("Un objet Minimale créé !")


m = Minimale()
print("m", m)
print("\n\n")



class MyTest:

    def my_test(self):  # propre à l'objet
        """Pourquoi self?"""
        print("Premier test")


mt = MyTest()
mt.my_test()
# Que contient un objet ?
print(dir(mt))
