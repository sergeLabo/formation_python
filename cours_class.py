#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Subliminale:
    pass

class Minimale:
    print("Un objet Minimale créé !")

class MyTest:
    def my_test(self):
        print("Premier test")

class Bicycle:
    """Un vélo"""

    def __init__(self, color, kind):
        """C'est le constructeur"""
        
        self.color = color
        self.kind = kind

s = Subliminale()
print(type(s))

m = Minimale()

b = Bicycle("rouge", "vtt")
print(b.color)
print(b.kind)

class Contact:

    def __init__(self, name):
        self.name = name
        
    def set_phone(phone):
        self.phone = phone
        
    def get_phone(self):
        return self.phone
        
class Book(Contact):

    def __init__(self):
        pass

c = Contact("toto")
print(c.get_phone())
