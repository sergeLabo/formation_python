
print("dir() de called_file.py =", dir())
print("__name__ de called_file.py =", __name__)

def print_merci():
    print("ce cours de python est génial")

if __name__ == "__main__":
    print("Ce fichier est excécuté localement")
    print_merci()
