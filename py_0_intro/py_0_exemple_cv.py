
import os
import cv2

img = cv2.imread('./logo-labomedia.png')
if img is None:
    print("Pas d'image")
    os._exit(0)

while 1:

    cv2.imshow('image', img)
    print("ok")
    # Pour quitter
    if cv2.waitKey(100) & 0xFF == 27:
        break

cv2.destroyAllWindows()
