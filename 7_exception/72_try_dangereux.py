from time import sleep

print("Exemple de try dangereux ...")

try:
    print("Je ne veux plus que ça plante !")
    erreur = 1 / 0
except:
    pass

print("Génial, c'est passé comme une fleur ...")
sleep(10)
print("\n\nGénial, la centrale de Tchernobyl a explosé ... "*10)
print("\n\nFin du try dangereux.")
print("erreur", erreur)
