# # py_72.py

#### Try dangeureux

from time import sleep

print("Exemple de try dangereux ...")

try:
    print("Je ne veux plus que ça plante !")
    erreur = 1 / 0
except:
    pass

print("Génial, c'est passé comme une fleur ...")
sleep(10)
for i in range(10):
    print("\n\nGénial, la centrale de Tchernobyl explose ... ")
    sleep(1)

sleep(2)
print("\n\nExplication:\n")
print("erreur", erreur)
