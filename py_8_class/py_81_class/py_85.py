# # py_85.py

from time import sleep
from random import randint

class Skeleton:

    def __init__(self, nb_points, nb_coord):

        self.nb_coord = nb_coord
        self.nb_points = nb_points
        self.points = None
        self.average = None

    def update_average(self):
        if self.nb_points == 1 and self.nb_coord == 3:
            self.average = (self.points[0][0] +\
                            self.points[0][1] +\
                            self.points[0][2])/3
        else:
            self.average = None

    def add_points(self, points):
        # Ajout des points
        self.points = points

        # Mise à jour de la moyenne
        self.update_average()


if __name__ == '__main__':

    skelet = Skeleton(1, 3)
    print(skelet.average)
    print(dir(skelet))

    while 1:
        points = [[randint(50, 100), randint(0, 100), randint(-50, 50)]]
        skelet.add_points(points)
        moyenne = skelet.average
        print("moyenne", moyenne)
        sleep(1)
