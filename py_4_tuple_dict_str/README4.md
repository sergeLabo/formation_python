# Formation Python

## Tuple Dictionnaire String

### Tuple comme dans sextuple

En mathématiques, si n est un entier naturel, alors un n-uplet ou n-uple est une
collection ordonnée de n objets, appelés « composantes » ou « éléments » ou
« termes » du n-uplet.

L'utilisation du terme anglais tuple, suffixe de quin-tuple/sex-tuple/…, est
courante dans des ouvrages de programmation informatique en français.
```python
un_tuple = ("192.168.1.101", 8000)
```
Un tuple est immuable, en anglais immutable.
On ne peut pas faire:
```python
un_tuple[0] = "chez moi"
```
### Dictionnaire

Un dictionnaire est un ensemble d'éléments:
* un élément = à une clé, on associe une valeur. La clé doit être immuable donc pas une liste

dictionnaire_des_vacciners = {"martin": "oui", "dupond": "non"}

Les éléments du dictionnaire sont appelé par dictionnaire_des_vacciners["martin"]

Exemple plus complet:
```python
dico = {
            1: "fqfsd",
            "premier": "machin",
            ("127.0.0.1", 8000): "PC1",
            0: [11, 12, 45]
        }
```
Un dictionnaire n'est pas ordonné, l'interpréteur python les lit comme il les trouve. dico[0] n'est pas le premier, c'est le dernier car le dernier à cette clé.

#### Parcours d'un dictionnaire

```python
for key, value in dico.items():
    print("key", key, "value", value)
```

### String
```python
string = "Maître Corbeau sur un arbre perché, tenait en son bec un fromage."
print(len(string), string[3], string[-3])
```