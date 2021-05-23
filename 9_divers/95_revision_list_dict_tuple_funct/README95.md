# Formation Python

## Révision liste dict tuple fonction

### Variable

* integer = int() = 1
* décimal virgule flottante = float() = 1.0
* string = chaîne de caractères = str() = "labomedia" = "ùàöô" = 'l\'échange'

__Nom de variable__

Oui: variable, my_var, toto, ...

Non= MyVariable, myVariable, 1_toto, ...

### Listes

``` python
liste = [25, 45.789, [1, 2, 0], {"nom": "labomedia"}]
```
Parcours d'une liste:
``` python
for item in liste:
for i in range(len(liste)):
for item in liste:
    i = liste.index(item)
```

### Dictionnaires  

``` python
dico = {"nom": "CAMUS", "prénom": "ALBERT", "profession": "auteur à succès"}
```
Les clés peuvent être int, str, tuples, faux entiers = "01"

Parcours d'un dict:
``` python
for key, value in dico.items():
```

### Tuples

``` python
ADDRESS = ("127.0.0.1", 8000)
a, b = "127.0.0.1", 8000  # les parenthèses sont sous-entendues
```

### List Versus Dict

* Les listes sont compactes, beaucoup de méthodes puissantes
* Il ne faut pas se tromper quand on cherche une valeur particulière
* Les dict sont plus verbeux, mais c'est beaucoup plus facile de retrouver une valeur par sa clé
* Les dict ont moins de méthodes que les listes

### Fonction

``` python
def somme(a, b):
    """Fait la somme de a et b,
    retourne la somme si a et b sont entiers
    None sinon
    """
    if isinstance(a, int) and isinstance(b, int):
        return a + b
        
somme(1, 2)
somme(1, b=2)
somme(a=1, b=2)
```


