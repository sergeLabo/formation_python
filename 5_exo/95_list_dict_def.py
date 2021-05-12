"""
Exo list dict def
"""
###### Exercise 1
config = {  "network":  {
                        "ip": "127.0.0.1",
                        "port": 8003
                        },
            "image":    {
                        "width": 1280,
                        "height": 720,
                        "mode": "gray"
                        }
            }

# Construire une liste avec les valeurs

###### Exercise 2
contact = {
            "aa": 42,
            "bb": 25,
            "cc": 36,
            "dd": 0.4,
            "ee": 83,
            "ff": 101
            }

# Trouver le plus jeune

###### Exercise 3
"""Mettre dans un dict
Itsi_bitsi_petit_bikini-Dalida.mid
"""
liste = [
        [[0, 113], True, "DRUM R-8            "],
        [[0, 3], False, "BASS S-330          "],
        [[0, 64], False, "FANTASY D-110       "],
        [[0, 79], False, "BRASS D-50          "],
        [[0, 61], False, "PIANO MKS-20        "],
        [[0, 11], False, "GUITARE PROTEUS     "],
        [[0, 7], False, "GUITARE PROTEUS     "],
        [[0, 0], False, "Mel"],
        [[8, 117], True, "tom10               "]
        ]

###### Exercise 4
"""From given list
a) Calculate the total price of the all the gadgets.
b) Calculate the average of all the gadgets.
""""
gadgets = ["Mobile", "Laptop", 100, "Camera", 310.28, "Speakers", 27.00,
            "Television", 1000, "Laptop Case", "Camera Lens"]

###### Exercise 5
"""
Imaginons qu'une requête dans une DB vous donne
   "name": "Lloyd",
   "homework": [90.0,97.0,75.0,92.0],
   "quizzes": [88.0,40.0,94.0],
   "tests": [75.0,90.0]


   "name": "Alice",
   "homework": [100.0, 92.0, 98.0, 100.0],
   "quizzes": [82.0, 83.0, 91.0],
   "tests": [89.0, 97.0]

   "name": "Tyler",
   "homework": [0.0, 87.0, 75.0, 22.0],
   "quizzes": [0.0, 75.0, 78.0],
   "tests": [100.0, 100.0]

- Créer une liste des éléves avec leur data:
- Print:
    - student's name
    - student's homework
    - student's quizzes
    - student's tests
- Write a function average that takes a list of numbers and returns the average.
- Define a function called average that has one argument, numbers.
    Inside that function, call the built-in sum() function.
- Write a function called get_average that takes a student dictionary as input
    and returns his/her weighted average.
- Define a function called get_letter_grade
    If score is 90 or above: return "A"
    Else if score is 80 or above: return "B"
    Else if score is 70 or above: return "C"
    Else if score is 60 or above: return "D"
    Otherwise: return "F"
- Finally, test your function. Print the resulting letter grade.
"""
