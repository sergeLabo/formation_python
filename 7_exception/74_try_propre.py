
def divide(x, y):
    result = None
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    except:
        print("Pas de résultat")

    return result

result = divide(1, 0)
if result:
    print("Tchernobyl explose")
