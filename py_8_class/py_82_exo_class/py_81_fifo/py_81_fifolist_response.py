# # py_81_fifolist_response.py

class PileFIFO():
    """
    Pile FIFO pour faire des statistiques
    sur les dernières valeurs d'une variable.
    """
    def __init__(self, size):
        """size définit la hauteur de la pile."""

        self.queue = []
        self.size = size
        self.average = 0

    def append(self, new):
        """Ajoute pour avoir une pile constante de size valeurs."""

        # Ajout dans la liste à la fin
        self.queue.append(new)

        # Remplissage de la pile avec la première valeur au premier ajout
        while len(self.queue) < self.size:
            self.queue.append(new)

        # Suppression du plus ancien si la pile fait size + 1
        if len(self.queue) > self.size:
            self.queue.pop(0)

    def average_calcul(self):
        """Maj de la valeur moyenne de la pile."""
        somme = 0
        for i in range(len(self.queue)):
            somme += self.queue[i]
        if len(self.queue) == 0:
            self.average = 0
        else:
            self.average = somme / len(self.queue)


if __name__ == '__main__':

    pile = PileFIFO(5)

    pile.append(1)
    print(pile.queue)

    pile.append(2)
    print(pile.queue)

    pile.append({1: "test"})
    print(pile.queue)
