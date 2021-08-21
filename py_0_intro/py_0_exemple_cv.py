# replit_main


import os
import cv2

current = os.getcwd()
print(current)

img = cv2.imread(current + '/logo-labomedia.png')
if img is None:
    print("Pas d'image")
    os._exit(0)

i = 0
while i < 100:
    i += 1
    cv2.imshow('image', img)
    print(i)
    # Pour quitter
    if cv2.waitKey(100) & 0xFF == 27:
        break

cv2.destroyAllWindows()
