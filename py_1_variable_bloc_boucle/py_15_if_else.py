# # py_15_if_else.py

# Changer la valeur de a

a = -8

if a < 0:
    print("bingo")
    print("")
    print("tu as gagné")
    print("")
    if a < -5:
        print("2 ème niveau d'indentation")
else:
    print("tu as perdu")
    print(type("tu as perdu"))

print("je fais autre chose")
