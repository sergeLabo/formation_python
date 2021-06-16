# # py_86.py

# Créer une class

from time import time, sleep


STEP = 3

# class Comptage:

def update(nombre):
    return nombre + STEP


def run():
    nbr = 0
    t_zero = time()
    fps = 0
    while 1:

        nbr = update(nbr)
        sleep(0.001)
        if nbr % 1000 == 0:
            print("1000", nbr)

        fps += 1
        if time() - (t_zero + 1) > 0:
            print("FPS", fps)
            fps = 0
            t_zero = time()

run()
