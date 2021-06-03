
"""
Des méthodes souvent appelées par les autres scripts,
regroupées dans une class MyTools
"""


import os
import subprocess
from pathlib import Path
from json import dumps, loads

print(f"Le dossier courant est {os.getcwd()}")

class MyTools:

    def get_all_files_list(self, directory, extentions):
        """ Lit le dossier et tous les sous-dosssiers.
        Retourne la liste de tous les fichiers avec les extentions de
        la liste extentions.
        """

        file_list = []
        for path, subdirs, files in os.walk(directory):
            for name in files:
                for extention in extentions:
                    if name.endswith(extention):
                        file_list.append(str(Path(path, name)))
        return file_list

    def read_file(self, file_name):
        """ Retourne les datas lues dans le fichier avec son chemin/nom
        Retourne None si fichier inexistant ou impossible à lire .
        """

        try:
            with open(file_name) as f:
                data = f.read()
            f.close()
        except:
            data = None
            print("Fichier inexistant ou impossible à lire:", file_name)

        return data

    def write_data_in_file(self, data, fichier, mode="w"):
        """
        Ecrit data dans le fichier.
        Mode 'w' écrit un string dans le fichier
        Mode 'wb' écrit des bytes dans le fichier
        w écrase
        a ajoute
        """
        with open(fichier, mode) as fd:
            fd.write(data)
        fd.close()

    def write_json(self, data, fichier):
        """Ecrit le json dans le fichier"""

        write_data_in_file(self, dumps(data), fichier, mode="w")

    def get_json_file(self, fichier):
        """ Retourne le json décodé des datas lues
        dans le fichier avec son chemin/nom.
        """
        return loads(read_file(fichier))

    def create_directory(self, directory):
        """Crée le répertoire avec le chemin absolu, ou relatif"""

        try:
            # mode=0o777 est par défaut
            Path(directory).mkdir(mode=0o777, parents=False)
            print("Création du répertoire: {}".format(directory))
        except FileExistsError as e:
            print("Le répertoire {} existe.".format(directory))
        except PermissionError as e:
            print("Problème de droits avec le répertoire {}".format(directory))
        except:
            print("Erreur avec {}".format(directory))
            os._exit(0)

    def run_command_system(self, command):
        """
        Excécute la command shell.
        command = liste
        """
        p = subprocess.Popen(command,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
        output, errors = p.communicate()

        return output.decode('utf-8')


def test_run_command_system():

    mt = MyTools()

    # ls du dossier courant
    print("\n\nls:")
    print(mt.run_command_system('ls'))

def test_get_all_files_list():
    """Recherche des py et txt dans pymultilame/pymultilame/"""

    mt = MyTools()
    d = "./"

    print("\nListe des py dans", d)
    l = mt.get_all_files_list(d, [".py"])
    for f in l:
        print(f)

    print("\nListe des ini dans", d)
    l = mt.get_all_files_list(d, [".ini"])
    for f in l:
        print(f)


if __name__ == "__main__":

    test_get_all_files_list()

    test_run_command_system()
