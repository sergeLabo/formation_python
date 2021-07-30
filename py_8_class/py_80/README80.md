# Formation Python

## Portée des variables


``` python
import time
import datetime

time_1 = time.time()
time_2 = datetime.time()
```

time_1 et time_2 ne sont pas la même chose:

time_1 est un élément de l'ensemble time (=le module time)

time_2 est un élément de l'ensemble datetime (=le module datetime)

## Variable locale / globale

### Variable locale

Variable utilisée à l'intérieur d'une fonction

### Variable globale

Variable utilisée à l'intérieur d'un fichier.

Elles sont possibles, nécessaires, elles sont en tout majuscules

Elles ne doivent pas être modifiées, si elles sont modifiées, ce doit être intelligement.



### Fichiers

* py_80.py Variable globale locale
* py_81.py Espace de nom time, datetime
* py_82.py Jeu du PI
