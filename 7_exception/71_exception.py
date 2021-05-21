from time import sleep

a = 1
b = 0

try:
    infini = a / b
except:
    infini = "infini"

print(infini)

# while True print('Hello world')
# d = 10 * (1/0)
# e = 4 + spam*3
# f = '2' + 2

print("Exemple de try dangereux ...")

try:
    print("Je ne veux plus que ça plante !")
    erreur = 1 / 0
except:
    pass

print("Génial c'est passé comme une fleur ...")
# sleep(10)
# print("Génial, la centrale de Tchernobyl a explosé ... ")
# print("\nFin du try dangereux.")
#print("erreur", erreur)

#  Exception hierarchy
#  https://docs.python.org/3/library/exceptions.html#exception-hierarchy

# def divide(x, y):
    # try:
        # result = x / y
    # except ZeroDivisionError:
        # print("division by zero!")
    # else:
        # print("result is", result)
    # finally:
        # print("executing finally clause")

# print("\n    divide(2, 1)")
# divide(2, 1)
# print("\n    divide(2, 0)")
# divide(2, 0)
# print('\n    divide("2", "1")')
# divide("2", "1")

# Raise
# https://docs.python.org/3/tutorial/errors.html#raising-exceptions
# Le prof doit approfondir la question

from urllib.request import Request, urlopen
from urllib.error import URLError
import socket

def request(someurl, timeout=2):
    req = Request(someurl)
    # Simulation d'un navigateur
    req.add_header('User-agent', 'Cours de python')

    response = None
    try:
        response = urlopen(req, timeout=timeout)
        response = response.read()
    except URLError as e:
        print(dir(e))
        if hasattr(e, 'reason'):
            print('Server is unreachable.')
            print('Reason: ', e.reason)
        elif hasattr(e, 'code'):
            print('The server couldn\'t fulfill the request.')
            print('Error code: ', e.code)
    except socket.timeout as e:
        print('Request connection timeout, no response from server ')
    except:
        print("Final Error with", someurl, "Response None")

    return response

response = request("https://labomedia.org/toto/", timeout=1)
# response = request("https://labomedia.org/toto/", timeout=0.01)
response = request("https://ressources.labomedia.org/toto/", timeout=10)
print(response)
