# Formation Python

Support pour atelier d'initiation python

### Installation

Matériel exigé:

* Un PC sous Linux
* Une version de python >= 3.6

```bash
sudo apt install git geany geany-plugins python3-pip
cd ~
mkdir projets
cd /projets
git clone https://github.com/sergeLabo/formation_python.git
```

Dans le dossier /votre_home/.config/, supprimer le dossier “geany” si il existe,
puis coller à la place le dossier geany du dossier formation_python.

#### Mise à jour
Le hard reset du git va écraser formation_python.geany
Copier le fichier formation_python.geany ailleurs que dans le dossier formation_python soit puis recherge du git.

```bash
cp ~/projets/formation_python/formation_python.geany  ~/projets/formation_python.geany
git fetch origin
git reset --hard origin/master
```

#### Geany - The Flyweight IDE

[__Geany__](https://www.geany.org) is a powerful, stable and lightweight programmer's text editor that provides tons of useful features without bogging down your workflow. It runs on Linux, Windows and MacOS is translated into over 40 languages, and has built-in support for more than 50 programming languages.

#### PyCharm

[__PyCharm Community__](https://www.jetbrains.com/pycharm/download/#section=linux) est beaucoup plus fort, mais quelle usine à gaz. Son gros avantage est de bien présenter la doc pendant l'édition, et de permettre de trouver toute les occurences d'une variable, fonction, class, leur utilisation et leur définition.

### Edition collaborative en ligne

S'inscrire sur

#### codecollab

* https://codecollab.io
* Le upload d'un dossier n'est pas possible
* le lien avec un git non plus
* le fichier à excécuter est obligatoirement main.py

#### replit

* https://replit.com
* modération possible
* gratuit pour moins de 50 élèves
* pull d'un git possible


### 1 Variable bloc boucle

### 2 Liste

### 3 Fonctions

### 4 Tuple Dict String

### 5 Exercices

### 6 Import

### 7 Class

### 8

### 9 Divers

#### Venv

#### Mnist
