"""
Créer une class pour créer des objets qui seront des instance de cette class.

Nous recevons des valeurs en OSC, par exemple une position en profondeur,
la distance de la personne par rapport à la caméra:
    soit une seule valeur
    ces valeurs sont soit int ou float
    quand la pile est pleine faire la moyenne
    Faire tourner avec une boucle
"""

class PileFIFO():
    """
    Pile FIFO pour faire des statistiques
    sur les dernières valeurs d'une variable.
    """
    def __init__
        """size définit la hauteur de la pile."""

        self.queue = []
        self.average = None


    def append
        """Ajoute pour avoir une pile constante de size valeurs."""
        pass

    def get_average
        """Maj de la valeur moyenne de la pile."""
        pass


if __name__ == '__main__':

    pile = PileFIFO(5)

    for i in range(10, 110, 3):
        pass
        print(f"La moyenne est de {}")
