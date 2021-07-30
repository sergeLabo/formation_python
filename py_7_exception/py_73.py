# # py_73.py

#### Exemple propre

import os
from pathlib import Path


def create_directory(directory):
    """Crée le répertoire avec le chemin absolu, ou relatif"""
    try:
        # mode=0o777 est par défaut
        Path(directory).mkdir(mode=0o777, parents=False)
        print("Création du répertoire: {}".format(directory))
    except FileExistsError as e:
        print(e)
        print("Le répertoire {} existe.".format(directory))
    except PermissionError as e:
        print(e)
        print("Problème de droits avec le répertoire {}".format(directory))
    except:
        print("Erreur avec {}".format(directory))
        os._exit(0)

create_directory("test")

ici = os.getcwd()
# #print("ce script est:", ici)
create_directory(ici + "/test")

# #un_string = "toto %s %f"
a = 1
un_string = "toto_" + str(a) + "_fin"
print(un_string)
un_string = "toto_{}_fin".format(a)
print(un_string)
b = 0
# #un_string = "toto_{1}_fin{0}".format(b, a)
# #print(un_string)

un_string = f"toto_{a}_fin"
print(un_string)
