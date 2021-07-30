# # py_83.py

# Notation d'élèves


def get_moyenne(notes):
    total = 0
    for note in notes:
        total += note
    moyenne = total/len(notes)
    return moyenne

def get_level(moyenne):
    if moyenne <= 4:
        level = "E"
    elif 4 < moyenne <= 8:
        level = "D"
    elif 8 < moyenne < 12:
        level = "C"
    else:
        level = "A"
    return level

eleves = {"toto": [8, 10, 12],
          "tata": [0, 3, 18, 15]}

m = get_moyenne(eleves["toto"])
print(m)

"""
Créer une class GetMoyenneLevel
"""
