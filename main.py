
"""
Fichier pour replit.com

dans .replit

language = "python3"
run = "python3 ./main.py"

dans tous les fichiers, ajouter

# replit_main ok
# replit_main

Commenter cette ligne dans tous les fichiers,
sauf celui que l'on souhaite excécuter

"""

import os
import subprocess
from pathlib import Path

def not_in_black(path):
    l = ['mon_env', '.git', '/irc/', 'py_9_divers', 'main.py']
    for item in l:
        if item in path:
            return False
    return True


def get_all_files_list(directory, extentions):

    file_list = []
    for path, subdirs, files in os.walk(directory):
        for name in files:
            for extention in extentions:
                if name.endswith(extention):
                    p_complet = str(Path(path, name))
                    if not_in_black(p_complet):
                        print(p_complet)
                        file_list.append(p_complet)

    return file_list

files = get_all_files_list('./', ["py"])


en_cours = "bad"
for fichier in files:
    if 'main.py' not in fichier:
        with open(fichier, "r") as file_object:
            data = file_object.read()
        file_object.close()

        lines = data.splitlines()
        for line in lines:
            if "# replit_main ok" in line:
                en_cours = fichier
                continue

print("Fichier à exécuter:", en_cours)
print("\n"*5)

if "bad" not in en_cours:
    subprocess.run(["python3", en_cours])
else:
    print("Pas de # replit_main ok")

os._exit(0)
# #"%f"
