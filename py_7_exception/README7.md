# Formation Python

## Exception

### Exemple

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

### Comment cacher les erreurs ?

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

* py_71.py Exception intro
* py_72_.py Try dangereux.py
* py_73_.py Exemple propre create_directory()
* py_74_.py Utilisation courrante
