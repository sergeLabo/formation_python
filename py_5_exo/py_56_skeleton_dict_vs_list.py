# replit_main

# # py_56_skeleton_dict_vs_list.py

"""
Pourquoi choisir un dictionnaire ou une liste, pour stocker ses données ?

Cubemos utilise une 'norme' pour les numéros des articulations qui s'appelle
MPI (Massachusetts ...) avec 15 points.

Il y en a une autre COCO (Common Object in Context) avec 18 points.

Les noms des clés de JOINTS correspondent à l'index des points

Ecrire main()
"""

# Les clés sont les objets (des sphères) Blender matérialisant les articulations
JOINTS = {
            "00": "head",
            "01": "cou",
            "02": "epaule.r",
            "03": "coude.r",
            "04": "poignet.r",
            "05": "epaule.l",
            "06": "coude.l",
            "07": "poignet.l",
            "08": "hanche.r",
            "09": "genou.r",
            "10": "cheville.r",
            "11": "hanche.l",
            "12": "genou.l",
            "13": "cheville.l",
            "14": "torso"
        }

PAIRS_MPI = {   "upper_arm.L": [5, 6],
                "forearm.L": [6, 7],
                "upper_arm.R": [2, 3],
                "forearm.R": [3, 4],
                "thigh.L": [11, 12],
                "shin.L": [12, 13],
                "thigh.R": [8, 9],
                "shin.R": [9, 10],
                "shoulder.L": [1, 5],
                "shoulder.R": [1, 2],
                "tronc.L": [5, 11],
                "tronc.R": [2, 8],
                "bassin": [8, 11],
                "head": [1, 0]}


def get_points_blender(data):
    """ data = list(coordonnées des points empilés d'une frame
            soit 3*18 soit 3*15 items avec:
            mutipliées par 1000
            les None sont remplacés par (-1000000, -1000000, -1000000)
            le numéro du body (dernier de la liste) doit être enlevé,
            et le time() si existe
        Conversion de cubemos en blender
            Les coords sont multipliées par 1000 avant envoi en OSC
            Permutation de y et z, z est la profondeur pour RS et OpenCV
            et inversion de l'axe des y en z
    """

    # Réception de 54=3*18 ou 45=3*15
    if len(data) == 54 or len(data) == 45:
        nombre = int(len(data)/3)
        points = []
        for i in range(nombre):
            # Reconstruction par 3
            val = [ data[(3*i)],
                    data[(3*i)+1],
                    data[(3*i)+2]]
            if val == [-1000000, -1000000, -1000000]:
                points.append(None)
            else:
                # Conversion cubemos vers blender
                points.append([val[0]/1000, val[2]/1000, -val[1]/1000])
    else:
        points = None

    return points


def main(points):
    """Mettre les coordonnées (blender) dans un dictionnaire human readable"""

    dico = {"tête": [x, y, z], ...........}


if __name__ == "__main__":

    """les points sont lus dans un json: la liste est une frame.
    [[15*3 coordonnées, numéro du body], time()]
    time() sert à tracer les courbes x,y,z; c'est l'abcisse
    """
    points = [[17, -666, 1725, 1, -528, 1821, -163, -544, 1879, -1000000,
            -1000000, -1000000, -318, -79, 1904, 158, -517, 1784, 203, -295, 1887,
            185, -27, 1882, -123, -42, 1767, -132, 339, 1896, -119, 686, 1986, 66,
            -26, 1776, 70, 337, 1887, 70, 679, 1912, 1, -697, 1727, 47, -698, 1731,
            -60, -714, 1811, 80, -708, 1796, 1], 1619353644.9007664]


    main(points)
