
port = 0
ip = ""

# tuple
address = (ip, port)
# ou
address = (ip,
           port)

# un tuple est immuable, en EN immutable

# Sans (), très souvent fait mais déconseillé
address = ip, port

# Affectation de valeurs
a, b = ip, port
print(type((a, b)))

# un tuple est immuable
# #address[0] = "chez moi"

address = ("chez moi", port)
print("address", address)
