# # py_80.py

#### Variable globale locale

# #variable = "python"

# #def simple():
    # #print("dans simple, variable =", variable)

# #simple()

# #def test():
    # #variable = "tu vas te faire avoir"
    # #print("dans test, variable =", variable)

# #print("dans le script, variable =", variable)
# #test()

# #variable = "autre valeur"
# #def danger():
    # #variable = "danger"
    # #print("dans danger, variable =", variable)

# #danger()
# #print("dans le script, variable =", variable)

VARIABLE = "python"

def pertinent():
    global VARIABLE
    VARIABLE = "npoveau"
    variable = "machin"
    print("dans pertinent, variable locale =", variable)
    print("dans pertinent, variable globale =", VARIABLE)

pertinent()
print("dans le script, variable =", VARIABLE)
