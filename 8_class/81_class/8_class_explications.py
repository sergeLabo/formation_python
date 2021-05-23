
from random import randint

class Skeleton:

    def __init__(self, nb_points, nb_coord, age_du_capitaine):

        self.nb_coord = nb_coord
        self.nb_points = nb_points
        self.points = self.set_points()
        # self.average = [None, None, None]

    def set_points(self):
        print(age_du_capitaine)
        points = None
        self.update_average()
        return points

    def update_average(self):
        self.average = None
        pass

    def add_points(self, points):
        # ajout des points

        # Mise à jour de la moyenne
        self.get_average()

    def get_average(self):
        average = None
        return average

if __name__ == '__main__':

    skelet = Skeleton(1, 3, 55)
    print(skelet.average)
    print(dir(skelet))

    # #while 1:
        # #points = [[randint(50, 100), randint(0, 100), randint(-50, 50)]]
        # #skelet.add_points(points)
        # #moyenne = skelet.get_average()
        # #print(moyenne)
