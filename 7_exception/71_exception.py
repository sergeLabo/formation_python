from time import sleep

a = 1
b = 0

try:
    infini = a / b
except:
    infini = "infini"

# print(infini)

# while True print('Hello world')
# d = 10 * (1/0)
# e = 4 + spam*3
# f = '2' + 2


#  Exception hierarchy
#  https://docs.python.org/3/library/exceptions.html#exception-hierarchy

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    except:
        print("Pas de résultat")

# print("\n    divide(2, 1)")
# divide(2, 1)
# print("\n    divide(2, 0)")
# divide(2, 0)
# print('\n    divide("2", "1")')
# divide("2", "1")

def divide_toto(x, y):
    try:
        result = toto / y
    except ZeroDivisionError:
        print("division by zero!")
    except:
        print("Pas de résultat")
divide_toto(2, 1)

try:
    a = 1
    b = 1/0
except:
    pass

print("a final =", a)
