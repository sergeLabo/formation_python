# replit_main


""" Charger une configuration à partir d'un fichier *.ini """

import os
import ast
from configparser import SafeConfigParser


class MyConfig():
    """
    Charge la configuration depuis le fichier *.ini, dans un dictionnaire,
    sauve les changement de configuration,
    enregistre les changements par section, clé.
    """

    def __init__(self, ini_file):

        # Le dictionnaire avec la configuration
        self.conf = None

    def load_config(self):
        """Lit le fichier *.ini, et copie la config dans un dictionnaire."""

        parser = SafeConfigParser()
        parser.read(self.ini, encoding="utf-8")

        # Lecture de parser et copie dans un dictionnaire
        # chercher la doc sur les internets
        print("dir de parser", dir(parser))


    def save_config(self, section, key, value):
        """Sauvegarde dans le fichier *.ini  avec section, key, value.
        Uniquement int, float, str
        """
        pass




if __name__ == "__main__":

    dossier = os.getcwd()
    print("dossier", dossier)

    ma_config = MyConfig(dossier + "/config.ini")
    a = ma_config.conf
    print("conf est un dictionnaire avec tous les paramètres")
    print(a)
