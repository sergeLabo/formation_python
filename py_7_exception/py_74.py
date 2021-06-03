
#### Exemples courrants

def divide(x, y):
    result = None
    try:
        result = x / y
    except:
        print("Pas de résultat")

    return result

resp = divide(1, 0)
print("Tout va bien !", resp)

print("\n\n")
resp = divide("1", 0)
print("Dernier essai !", resp)



def get_data():

    data = None
    try:
        data = socket.receive()
    except:
        print("Pas de data reçue")

    return data
