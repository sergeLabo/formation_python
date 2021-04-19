
# #a = -6

# #if a < 0:
    # #print("bingo")
    # #print("")
    # #print("tu")
    # #print("as")
    # #print("gagné")
    # #print("")
    # #if a < -5:
        # #print("2 ème niveau d'indentation")
# #else:
    # #print("tu as perdu")
    # #print(type("tu as perdu"))

# #print("je fais autre chose")


# Introspection

class Car:
    """doc ok"""

    def __init__(self):
        self.test = "je sius un attribut"

# ##print(help(Car))

# #cd = Car.__dict__

# #for k, v in cd.items():
        # #print(k, ":", v)

# #print(Car.__dict__['__doc__'])

# #print(help(cd.__doc__))

 
# ##!/usr/bin/python3
# #""" Demonstrates the usage of dir(), with better output. """

# #__author__ = "ivanleoncz"

# #obj = "I am a string."
# #count = 0

# #print("\nObject Data: ", obj)
# #print("Object Type: ", type(obj),"\n")

# #for method in dir(obj):
    # ## the end=" " at the end of the print statement, 
    # ## makes it printing in the same line, 4 times (count)
    # #print("|    {:20}".format(method), end=" ")
    # #count += 1
    # #if count == 4:
        # #count = 0
        # #print("")

import inspect

car = Car()

i = inspect.getmembers(car)
print(i)

print(inspect.getdoc(car))

print(getattr(car, "test"))
