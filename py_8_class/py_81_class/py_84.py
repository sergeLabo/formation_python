
"""
Utilisation d'une classe à la place d'un dictionnnaire

Pour moi: voir le module enum
"""


perso_1 = { 'center': (1, 1, 1),
            'who': 0,
            'points_3D': None,
            'since': 1,
            'score': 0.5 }

# Je veux appeler
c = perso_1.center
# au lieu de
c = perso_1['center']
