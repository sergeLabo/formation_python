# Formation Python

## Exception

### Exemple

#### Exemple d'erreur
``` python
print(a)
```
``` bash
Traceback (most recent call last):
  File "71_exception.py", line 2, in <module>
    print(a)
NameError: name 'a' is not defined
```
L'erreur est un __NameError__

#### Comment cacher les erreurs ?

``` python
a = 1
b = 0
try:
    infini = a / b
except:
    infini = "infini"
print(infini)
```

### Liste des exceptions standards

* [Built-in Exceptions](https://docs.python.org/3/library/exceptions.html)

### Il faut bien traiter les erreurs

Excécuter les scripts

* 72_try_dangereux.py
* 73_
* 74_
