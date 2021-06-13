
# Ranger dans une ou 2 class
# Faire une comparaison des 2 overlay

import cv2
import numpy as np
from time import time


def simple_overlay(background, overlay, x, y):
    """
    Python: cv2.addWeighted(src1, alpha, src2, beta, gamma[, dst[, dtype]]) → dst¶
    Python: cv.AddWeighted(src1, alpha, src2, beta, gamma, dst) → None

    Parameters:
    src1 – first input array.
    alpha – weight of the first array elements.
    src2 – second input array of the same size and channel number as src1.
    beta – weight of the second array elements.
    dst – output array that has the same size and number of channels as the
            input arrays.
    gamma – scalar added to each sum.
    dtype – optional depth of the output array; when both input arrays have
            the same depth, dtype can be set to -1, which will be equivalent
            to src1.depth().

    """
    (rows, cols, channels) = overlay.shape

    overlay = cv2.addWeighted(  background[y:y+rows, x:x+cols],
                                1,
                                overlay,
                                1,
                                0)

    background[y:y+rows, x:x+cols ] = overlay
    return background


def overlay(src1, alpha, src2, beta):
    """
    Python: cv2.addWeighted(src1, alpha, src2, beta, gamma[, dst[, dtype]]) → dst¶
    Python: cv.AddWeighted(src1, alpha, src2, beta, gamma, dst) → None

    Parameters:
    src1 – first input array.
    alpha – weight of the first array elements.
    src2 – second input array of the same size and channel number as src1.
    beta – weight of the second array elements.
    dst – output array that has the same size and number of channels as the
            input arrays.
    gamma – scalar added to each sum.
    dtype – optional depth of the output array; when both input arrays have
            the same depth, dtype can be set to -1, which will be equivalent
            to src1.depth().
    """

    (x, y) = (src1.shape[0], src1.shape[1])
    dst = np.zeros((x, y, 3), dtype = "uint8")
    cv2.addWeighted(src1, alpha, src2, beta, 1.0, dst)

    return dst


def viewer():
    # test est un string
    img = cv2.imread("sun_sea.png")
    moon = cv2.imread("moon.png")
    t0 = time()
    num = 0
    cv2.namedWindow('Image',
                    cv2.WINDOW_NORMAL+cv2.WINDOW_KEEPRATIO+cv2.WINDOW_AUTOSIZE)
    while num < 2000:
        x = int(num/2)
        y = int(num/4)
        new_img = simple_overlay(img.copy(), moon, x, y)
        if new_img.any():
            cv2.imshow('Image', new_img)
        else:
            break
        num += 1
        if cv2.waitKey(1) == 27:
            break
    temps = int(time() - t0)
    print("Durée du test", temps)  # 10/1000=10ms
    cv2.destroyAllWindows()


def video():
    cv2.namedWindow('Image',
                    cv2.WINDOW_NORMAL+cv2.WINDOW_KEEPRATIO+cv2.WINDOW_AUTOSIZE)
    cap = cv2.VideoCapture('sorcier.mkv')
    moon = cv2.imread('moon.png')
    x, y = 0, 0
    nb = 0
    while cap.isOpened():
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        new = simple_overlay(frame, moon, 1, 1)
        nb += 1
        if nb % 20 == 0:
            x += 1
            y += 1

        cv2.imshow('Image', new)
        if cv2.waitKey(1) == 27:
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    viewer()
    # #video()
