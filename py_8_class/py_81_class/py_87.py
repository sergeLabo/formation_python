# Jeu du 421

# jeter 3 ou 2 ou 1 dés

from time import sleep
from random import randint

NB_PARTIES = 0
NB_LANCER = 0
VERBOSE = 1
SLEEP = 1

def un_lancer():
    """Simulation d'un lancé de 1 dé:
    retourne un entier entre 1 compris et 6 compris
    """
    return randint(1, 6)

def multi_lancer(nb):
    res = []
    for i in range(nb):
        res.append(un_lancer())
    return res

def is_421(lancer):
    if 4 in lancer and 2 in lancer and 1 in lancer:
        return True
    else:
        return False

def une_partie():
    global NB_PARTIES, NB_LANCER, VERBOSE, SLEEP

    print("Nouvelle partie")
    score = 0
    result = []
    nb_des_a_jeter = 3
    score += 1
    good_421 = [0, 0, 0]
    while 1:
        lancer = multi_lancer(nb_des_a_jeter)
        print("Lancer:", lancer)

        if 4 in lancer:
            if not good_421[0]:
                result.append(4)
                nb_des_a_jeter -= 1
                good_421[0] = 1

        if 2 in lancer:
            if not good_421[1]:
                result.append(2)
                nb_des_a_jeter -= 1
                good_421[1] = 1

        if 1 in lancer:
            if not good_421[2]:
                result.append(1)
                nb_des_a_jeter -= 1
                good_421[2] = 1

        if nb_des_a_jeter == 0:
            break

        if VERBOSE:
            print("result:", result)
        score += 1
        sleep(SLEEP)

    NB_LANCER += score
    if VERBOSE:
        print("score", score, "\n")
    bilan = round(NB_LANCER / NB_PARTIES, 4)
    if NB_LANCER % 20000 == 0:
        print("Bilan:", bilan, "\n")

while 1:
    NB_PARTIES += 1
    une_partie()
