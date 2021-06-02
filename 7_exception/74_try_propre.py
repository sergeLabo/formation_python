
def divide(x, y):
    result = None
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    except:
        print("Pas de résultat")

    return result

resp = divide(1, 0)
print("Tout va bien !", resp)

print("\n\n")
resp = divide("1", 0)
print("Dernier essai !", resp)
