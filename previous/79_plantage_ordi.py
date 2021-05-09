
"""Ce progamme va planter votre ordi

python3.x -m pip install opencv-python

"""

import cv2

img = cv2.imread("dammier_vert.png")
print("Taille de l'image:", img.shape)
liste = []
for i in range(100000000000):
    liste.append(img)
