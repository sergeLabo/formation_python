# # called_file.py

#### Appelé par py_62.py

print("dir() de called_file.py =", dir())
print("__name__ de called_file.py =", __name__)

def print_merci():
    print("\n\nce cours de python est génial")

if __name__ == "__main__":
    print("Ce fichier est excécuté localement")
    print_merci()
