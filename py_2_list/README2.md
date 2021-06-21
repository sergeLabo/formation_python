# Formation Python

## Liste

### Exemples
liste = [1, 2, 3, 4, 5]
index    0  1  2  3  4
On compte à partir de zéro

__Une liste est un ensemble d'éléments ordonnés.__

Pour obtenir un élément:
``` python
liste[1] = 2
liste[0] = 1
```

[sametmax.com valeurs et references en python](https://sametmax.com/valeurs-et-references-en-python/)

### Parcours d'une liste
``` python
for item in liste:
    print(item)

for i in range(len(liste)):
    print(liste[i])

for item in liste:
    i = liste.index(item)
    print(liste[i])
```

### Quelques opérations sur les listes

``` python
suite = [5, 6, 7, 21.3, "oh!", [3.21, 1478000]]
suite.append(3.14159)
```


### Slices 
``` python
liste = [1, 2, 3, 4, 5, 5, 6, 7, 21.3, 'oh!', [3.21, 1478000], 3.14159]
part = liste[3:6]
print(part)
liste[-1]
liste[-3]
liste[3:-2]
```

### Copie de liste
``` python
a = [0, 1]
b = a
print("a =", a, "b =", b)

a[0] = "toto"
print("a =", a, "b =", b)

a[0] = "toto"
print("a =", a, "b =", b)
```
Pour avoir une nouvelle liste indépendantes, faire
``` python
a = [0, 1]
b = a.copy()
```

### List Comprehension

Définitions de compréhension en Logique: Ensemble des caractères propres à un concept.
``` python
liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
pair = [p for p in liste if p % 2 == 0]
print(pair)
```