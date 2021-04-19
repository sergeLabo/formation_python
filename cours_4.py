
i = 0
while i <= 10:
    print(str(i) + " x 4 =", i * 4)
    i += 1
    
chaine = "Labomedia"
for lettre in chaine:
    print(lettre)
    
def test1():
    """Retourne None"""
    print("toto")
    
def test2():
    """Retourne """
    print("toto")
    return "Python c'est fun"
    
test1()
print(test1())

test2()
print(test2())

def test(a):
    if a < 0:
        print("a<0")
        return 1
    else:
        print("a>0")
        return 0
    print("fin")
        
test(1)
test(-1)

def ma_fonction():
    print("Demain")

def ta_fonction(a):
    print(a)

def sa_fonction(a, n):
    while i < n:
        print(a, i)
        
ma_fonction()
ta_fonction("1")
ta_fonction("Guido")
sa_fonction(5, 3)

def fonct(a=1, b=2, c=3):
    print(a, b, c)
    
fonct()
fonct(10)
fonct(b=10)

import time

print(dir(time))
print("Il est", time.time())

import datetime

print(dir(datetime))
print("Nous sommes le", datetime.date.today())
