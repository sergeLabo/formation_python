# replit_main

# # py_82_tempo_enonce.py

"""
Class utilisable pour des tempo et compteur dans Blender
"""


class Tempo:
    """
    Les tempos sont en fait des compteurs qui sont mis à jour à chaque
    frames de Blender avec update.
    Pour une tempo de n, compte bien de 0 à n-1
    """

    def __init__(self, periode=60):
        """Paramètres:
        période: la tempo est remise à zéro si periode atteind,
                    -1 = infinite loop
        pas: incrément de la tempo, par défaut=1, ne pas changer le pas
        verrou: si verrou, pas d'incrémentation.
        """

    def lock(self):
        """Verrou, je bloque"""


    def unlock(self):
        """Pas de verrou, je peux incrémenter"""


    def reset(self):
        """Remise à zéro de la tempo"""


    def update(self):
        """J'incrémente si pas de verrou. Si verrou, je ne fais rien"""


def main():
    """Créer 5 tempos
    appelées par des noms: mario wario infini mario:turbo wario:turbo
    """



if __name__ == "__main__":

    tempo = Tempo(14)

    from time import sleep

    nb = 0
    while nb < 1000:
        tempo.update()
        if nb % 28 == 0:
            tempo.lock()
        if nb % 60 == 0:
            tempo.unlock()

        print(tempo.tempo)
        nb += 1
        sleep(0.05)
