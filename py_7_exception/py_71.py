# # py_71.py

#### Exception intro

from time import sleep

# #a = 1
# #b = 0

# #try:
    # #infini = a / b
    # #print("ok")
# #except:
    # #infini = "infini"

# #print("L'infini est ", infini)

# Exemple d'exceptions
# #while True print('Hello world')
# #d = 10 * (1/0)
# #e = 4 + spam*3
# #f = '2' + 2

def divide(x, y):
    # #result = None
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
        result = None
    except:
        print("Pas de résultat")
        result = None
    return result

# #print("\n    divide(2, 1)")
# #d = divide(2, 1)
# #print(d)

# #print("\n    divide(2, 0)")
# #d = divide(2, 0)
# #print(d)

# #print('\n    divide("2", "1")')
# #d = divide("2", "1")
# #print(d)

# #def divide_toto(x, y):
    # #try:
        # #result = toto / y
    # #except ZeroDivisionError:
        # #print("division by zero!")
    # #except:
        # #print("Pas de résultat")

# divide_toto(2, 1)

try:
    a = 10
    oui = 1/0
except:
    pass

print("a final =", a)
print(oui)
