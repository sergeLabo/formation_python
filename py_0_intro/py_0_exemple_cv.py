
import cv2

img = cv2.imread('./logo-labomedia.png')

while 1:

    cv2.imshow('image', img)

    # Pour quitter
    if cv2.waitKey(1000) & 0xFF == 27:
        break

cv2.destroyAllWindows()
