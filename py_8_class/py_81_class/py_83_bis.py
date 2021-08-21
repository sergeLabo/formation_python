# replit_main

# # py_83.py

# Notation d'élèves

class GetMoyenneLevel:

    def __init__(self, notes):

        self.notes = notes

    def get_moyenne(self):
        total = 0
        for note in self.notes:
            total += note
        self.moyenne = total/len(self.notes)

    def get_level(self):
        if  self.moyenne <= 4:
            self.level = "E"
        elif 4 < self.moyenne <= 8:
            self.level = "D"
        elif 8 < self.moyenne < 12:
            self.level = "C"
        else:
            self.level = "A"


eleves = {"toto": [8, 10, 12],
          "tata": [0, 3, 18, 15]}

"""
Mettre la class GetMoyenneLevel dans un fichier dans ce dossier,
puis faire un import

Ensuite, mettre le fichier dans un sous-dossier, et faire l'import
"""
