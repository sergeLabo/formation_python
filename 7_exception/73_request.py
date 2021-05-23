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
        print("dir(e) =", dir(e))
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
print(response)
response = request("https://labomedia.org/toto/", timeout=0.01)
print(response)
response = request("https://ressources.labomedia.org/toto/", timeout=10)
print(response)
