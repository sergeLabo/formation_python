# Formation Python

## Import

### Exemples
``` python
import os, sys
import time
import json

# import des lib à installer
import numpy as np
import scipy
import matplotlib

# import des trucs spéciaux

# Pas du tout apprécié des bons programmeurs
from time import *
from datetime import *
```

### L'interpréteur Python va chercher les libs où ?

``` python
import sys
print(sys.path)
```

Le dossier du fichier excécuté est dans la liste sys.path si le fichier est lancé depuis ce dossier.

### Installation d'un module spécifique
Installation dans votre système, qui présente un risque de casser des choses

``` bash
sudo pip3 install numpy 
```
Installation dans votre home, dans .local
``` bash
python3.7 -m pip install numpy --user 
```

La meilleure solution est de créer un [virtualenv](https://ressources.labomedia.org/virtualenv) pour chaque projet.


### Export
Sujet non étudié ! 

### Liens

Tous les modules de la bibliothèque standard

[python.org library](https://docs.python.org/3/library/index.html)

[py-modindex](https://docs.python.org/3/py-modindex.html)


Exemples

[get_cubemos_skeleton.py](https://github.com/sergeLabo/cubemos-skeleton/blob/main/get_skeleton/get_cubemos_skeleton.py)

[datetime.py](https://github.com/python/cpython/blob/main/Lib/datetime.py)

