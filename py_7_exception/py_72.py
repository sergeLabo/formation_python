# replit_main

# # py_72.py

#### Try dangeureux

from time import sleep

print("Exemple de try dangereux ...")

try:
    print("Je ne veux plus que ça plante !")
    erreur = 1 / 0
except:
    pass

print("Ca tourne ...")
sleep(10)
for i in range(100):
    print("\n\nBoum! la centrale de Tchernobyl a explosé ... ")
    sleep(1)
