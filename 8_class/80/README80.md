# Formation Python

## Portée des variables

[Qu'est ce qu'un namespace](https://sametmax.com/quest-ce-quun-namespace/)

Un namespace, ou espace de noms, est simplement un conteneur de noms, un groupe. On s’en sert pour pouvoir distinguer deux choses qui ont le même nom.

``` python
import time
import datetime

time_1 = time.time()
time_2 = datetime.time()
```

time_1 et time_2 ne sont pas la même chose:

time_1 est un élément de l'ensemble time (=le module time)

time_2 est un élément de l'ensemble datetime (=le module datetime)

### Variable locale / globale

### Variable globale

Elles sont possibles, nécessaires, elles sont en tout majuscules

Elles ne doivent pas être modifiées, si elles sont modifiées, ce doit être intelligement.

Ce qui compte dans l'effort, c'est avant tout l'action, plutôt que le résultat. Ludwig Van.

__Ce n'est pas le mal qu'on s'est donné qui compte, mais le résultat.__

__Le chemin pour atteindre un résultat doit être décidé en fonction du contexte.__
