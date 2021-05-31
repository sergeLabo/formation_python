
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
