# Formation Python

## POO

Introduction à la POO programation orientée objet.

### Pourquoi utiliser des objets ?

#### Programmation procédurale et POO

On peut faire des choses très puissante sans Objet

* Présentation des scripts mnist: numpy et keras

#### Intro

Il y a des tas de manières de programmer. Des styles. Des formes que l’on donne au code. On leur donne des noms: programmation procédurale, fonctionnelle, orientée flux, par contrat, etc. C’est ce qu’on appelle des paradigmes, des points de vue sur comment on doit faire le boulot.

En vérité, le point de vue n’est pas déterminant. Vous pouvez faire le même boulot en utilisant n’importe lequel. L’important c’est de coder.

Mais chaque point de vue possède des caractéristiques et des outils différents.

Ce que vous allez voir est ce qu’on appelle la programmation orientée objet, ou POO. C’est un simple point de vue, un outil, mais il est très utilisé en Python, Ruby ou Java.

Quand vous avez appris la programmation, on vous a montré comment stocker des données dans des structures de données:

* les listes
* les chaînes
* les entiers
* les dictionnaires
* etc ...

Et on vous a montré comment créer un comportement pour votre programme en utilisant des mots clés, puis plus tard en utilisant des fonctions pour regrouper ces mots clés.

En Python, à ce stade, vous utilisez des fonctions pour agir sur des structures de données.

La programmation orienté objet, c’est un style de programmation qui permet de regrouper au même endroit le comportement (les fonctions) et les données (les structures) qui sont faites pour aller ensemble.

C’est tout. C’est une simple question d’organisation du programme.

#### Avantage de la POO

__Les objets servent à ranger les choses (les bouts de votre projet)__:

* Pour éviter les répétitions, sources d'erreurs, surtout si une modifications de ces répétitions est nécessaire.
* Pour structurer le projet.
* Pour tester des bouts de code individuellement.
* Pour éviter les problèmes avec les variables globales.
* Pour pouvoir réutiliser des bouts de codes.
* Permettre un travail en équipe en découpant un projet en bout de projet indépendant.

Philosophie: Une fonction fait une chose. Une class fait une chose

### Vocabulaire

Une class permet de créer des objets.
Un objet est un machin:    une voiture, un moteur, une fleur,
                            un amour, un modèle d'IA, un encodeur_decodeur ....

Un objet a des méthodes et des attributs
    - une méthode est une fonction propre  à l'objet
    - un attribut est une variable qui appartient à cet objet

Qu’est-ce qu’un objet

Un objet est un… truc. Un machin. Un bidule.

Ça peut vous paraître une définition floue, mais c’est parce que c’est exactement ce que peut être un objet: n’importe quoi que vous décidiez de coder. L’objet est un moyen de dire à la machine : “ce < entrez_ici_un_nom_de_truc > possède telle donnée, et fait telle chose avec”.

En Python, absolument tout est un objet : une chaîne, un entier, un dictionnaire, une liste, une fonction… Vous avez donc manipulé des objets sans le savoir. Maintenant vous allez créer les vôtres.

Créer des objets se fait en deux étapes: décrire à quoi ressemble votre objet, et demander à l’ordinateur d’utiliser cette description pour le fabriquer.

### Résumé final par sametmax

La classe, c’est un plan.

L’objet, c’est ce qu’on crée avec le plan.

Une méthode, c’est une fonction déclarée dans une classe (qui est attachée à chaque objet produit, et on lui passe en premier paramètre l’objet en cours).

Un attribut, c’est une variable attachée à un objet.

Une instance d’une classe, c’est l’objet issu d’une classe.

Le vocabulaire en informatique, c’est primordial.
