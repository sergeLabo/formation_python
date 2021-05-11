
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

        self.periode = periode
        self.verrou = False
        self.pas = 1
        self.tempo = 0

    @property
    def get_tempo(self):
        """OBJ.get_tempo() = OBJ.tempo"""

        return self.tempo

    def lock(self):
        """Verrou, je bloque"""

        self.verrou = True

    def unlock(self):
        """Pas de verrou, je peux incrémenter"""

        self.verrou = False

    def reset(self):
        """Remise à zéro de la tempo"""

        self.tempo = 0

    def update(self):
        """J'incrémente si pas de verrou. Si verrou, je ne fais rien"""

        if not self.verrou:
            self.tempo += self.pas
            if self.periode != -1:
                if self.tempo >= self.periode:
                    self.tempo = 0
        return self.tempo


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
        if nb % 799 == 0:
            tempo.reset()
        print(tempo.tempo)
        nb += 1
        sleep(0.01)
