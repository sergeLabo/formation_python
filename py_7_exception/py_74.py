# # py_74.py

#### Utilisation courrante

# #def divide(x, y):
    # #result = None
    # #try:
        # #result = x / y
    # #except:
        # #print("Pas de résultat")

    # #return result

# #resp = divide(1, 0)
# #print("Tout va bien !", resp)

# #print("\n\n")
# #resp = divide("1", 0)
# #print("Dernier essai !", resp)

def get_data(socket):

    data = None
    try:
        data = socket.receive()
    except:
        # #print("Pas de data reçue")
        pass

    return data

while 1:
    socket = "essai"
    data = get_data(socket)
    print(data)
