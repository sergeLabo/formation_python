# # py_26_points_to_msg.py

""" Construire un Message à envoyer en OSC

Le message sera envoyé avec:
    osc_client.send('/points', msg)

le chien de Emmanuel: Emmanuel's dog

mais cette fonction n'est pas implémentée ici,
vous construisez le msg seulement.

Faire des plier déplier.
"""

# il y a toujours 8 points dans points: len(points) = 8
points = [[0, 0], [-1.56,  -2.78], [0, 1.2], [1.2, 0], [45, 54],
          [10, 10], [45, 78], None, None]

"""
Si None --> insérer -1000, -1000,
Consruire le msg avec les coordonnées empilées dans une seule liste
msg = [0, 0, -1.56, ....., -1000, -1000]
"""

# msg = []
# for point in points:
    # if point:
