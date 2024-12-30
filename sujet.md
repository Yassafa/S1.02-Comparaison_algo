# SAÉ S1.02 : Santas Claus


Ce document correspond au sujet de la SAÉ S1.02 de l'année universitaire 2023/2024. Ce travail est à faire par binôme en autonomie. Il correspond à la suite de la SAÉ S01.01.

**La SAÉ devra être rendue au plus tard le 23 janvier 2024 à 23h59.**

## Évaluation

La SAÉ sera notée de la manière suivante : 
- Évaluation du rendu : 8 points répartis de la manière suivante
    - Correction automatique du code via des tests unitaires : 2 points
    - Tests unitaires rendus : 2 points
    - Qualité du code (clarté, efficacité, commentaires, docstring) : 2 points
    - Comparaison expérimentale et théorique (fichier notebook) : 2 points
- Contrôle du 24 janvier : 12 points 

**Attention :** Pour le contrôle du 24 janvier, il faut connaître le sujet et le code (les structures de données utilisées et les diffférentes fonctions définies) dans les SAÉ S01.01 et S01.02.

## Sujet

Le sujet est la suite de la SAÉ S01.01. La correction de cette SAÉ est donnée dans le fichier `santa_claus.py`. 

**Remarque :** Les noms des fonctions à définir sont en anglais pour faire la différence avec les fonctions définies dans la SAÉ S01.01. 


### Question 1

On souhaite calculer les distances entre toute paire de villes avant de chercher un tour *intéressant*, c'est-à-dire de petite longueur. 

Pour stocker les distances, on utilisera un dictionnaire dont les clés sont les noms des villes et les valeurs des dictionnaires contenant pour chaque ville différente de la clé la distance de cette ville à la clé du dictionnaire. Dans la suite du sujet, on appellera un *dictionnaire de distances* un tel dictionnaire.

Par exemple, les distances entre les villes de Paris, Lyon, Marseille et Lille sont stockées dans le dictionnaire de distances suivant.

```python
{
    'Paris': {
        'Lyon': 394.5056834297657, 
        'Marseille': 661.8616554466852, 
        'Lille': 203.67224282542662
    }, 
    'Lyon': {
        'Paris': 394.5056834297657, 
        'Marseille': 275.87965367431525, 
        'Lille': 558.5472363339435
    }, 
    'Marseille': {
        'Paris': 661.8616554466852, 
        'Lyon': 275.87965367431525, 
        'Lille': 834.0220261600157
    }, 
    'Lille': {
        'Paris': 203.67224282542662, 
        'Lyon': 558.5472363339435, 
        'Marseille': 834.0220261600157
    }
}
```




Définir la fonction `dictionary_cities` prenant en paramètre un tableau `villes` comme définie dans la partie 1 et retournant un dictionnaire de distances contenant les distances entre les villes du tableau passé en paramètre.

Par exemple, l'appel de la fonction `dictionary_cities` avec le tableau 
```python
["Paris",2.33, 48.86, "Lyon", 4.85, 45.75, "Marseille", 5.40, 43.30, "Lille", 3.06, 50.63]
```
doit retourner le dictionnaire de distances donné en exemple.



### Question 2

Définir la fonction `distance_cities` prenant en paramètre deux noms de villes et un dictionnaire de distances, et retournant la distance entre les deux villes passées en paramètre si cette valeur est stockée dans le dictionnaire de villes, et -1 sinon.

**Remarque :** Cette fonction retourne le même résultat que la fonction `distance_noms` de la SAÉ S01.01 mais utilise un dictionnaire de distances plutôt qu'un tableau de villes.


### Question 3

Définir la fonction `tour_length` prenant en paramètre un tour et un dictionnaire de distances, et retournant la longueur du tour. 

Par exemple, l'appel de cette fonction avec le tour `["Paris", "Lyon", "Marseille", "Lille"]` et le dictionnaire de distances donné en exemple doit retourner 1708.0796060895232.

**Remarque :** Un tour est un tableau de nom de villes (comme pour la SAÉ S01.01). Cette fonction retourne le même résultat que la fonction `long_tour` mais utilise un dictionnaire de distances plutôt qu'un tableau de villes.


### Question 4

Comparer théoriquement et expériementalement les complexités des fonctions `long_tour` et `tour_length`.


### Question 5

Définir la fonction `closest_city` prenant en paramètre un nom de ville `city`, un tableau de noms de villes `cities` et un dictionnaire de distances, et retournant l'indice de la ville de `cities` la plus proche de `city`.

Par exemple, l'appel de la fonction `closest_city` avec les valeurs `"Paris"` (pour `city`), `["Marseille", "Lyon"]` (pour `cities`) et le dictionnaire de distances donné en exemple doit retourner 1 car Lyon est plus proche de Paris que Marseille.


### Question 6


On souhaite construire un petit tour passant par toutes les villes. Pour cela, partant d'une ville de départ, on construit ce tour par étape en ajoutant à chaque fois la ville restante la plus proche de la dernière ville ajoutée.

Définir la fonction `tour_from_closest_city` prenant en paramètre un nom de ville et un dictionnaire de distances et retournant le tour obtenu par l'algorithme décrit ci-dessus. La ville de départ sera celle donnée en paramètre.

L'appel de cette fonction avec la valeur `"Marseille"` et le dictionnaire donné en exemple doit retourner : `["Marseille", "Lyon", "Paris", "Lille"]`.

### Question 7

Définir la fonction `best_tour_from_closest_city` prenant en paramètre un dictionnaire de distances. Cette fonction devra retourner le meilleur tour parmi ceux obtenus avec l'algorithme précédent en prenant chaque ville comme ville de départ.

L'appel de cette fonction avec le dictionnaire donné en exemple doit retourner `["Paris", "Lille", "Lyon", "Marseille"]` ou `["Lyon", "Marseille", "Paris", "Lille"]`.

### Question 8

Quelle est la complexité asymptotique de la fonction `best_tour_from_closest_city` ? Justifiez.

### Question 9

Si l'algorithme précédent fournit un tour avec une petite distance au total, il ne fournit pas forcément le meilleur tour. Cette question et les suivantes proposent de créer un algorithme pour améliorer un tour en effectuant plusieurs modifications successives.

À partir d'un tour, on peut obtenir un deuxième tour en inversant une partie des villes du tour.
Par exemple, à partir du tour :

 `["Agen", "Belfort", "Cahors", "Dijon", "Épinay", "Fréjus", "Grenoble", "Hyères"]` 

 on peut obtenir un deuxième tour en inversant toutes les villes entre `"Cahors"` et `"Fréjus"` : 
 
`["Agen", "Belfort", "Fréjus","Épinay", "Dijon", "Cahors", "Grenoble", "Hyères"]`.

Définir la fonction `reverse_part_tour` prenant en paramètre un tour et deux indices `ind_b` et `ind_e`, et inversant la partie du tableau donnée par les indices `ind_b` et `ind_e` inclus.

L'appel de cette fonction avec le tour contenant les huit villes dans l'ordre alphabétique et les valeurs 2 et 5 pour  `ind_b` et `ind_e` doit modifier le tour comme indiqué dans l'exemple.

### Question 10

Définir la fonction `inversion_length_diff` prenant en paramètre un dictionnaire de distances, un tour et deux indices `ind_b` et `ind_e` et retournant la différence entre la distance du tour passé en paramètre et celui obtenu en inversant la partie du tour entre les `ind_b` et `ind_e` inclus.

L'appel de la fonction avec le dictionnaire des distances donné en paramètre, le tour 
`["Marseille", "Lyon", "Paris", "Lille"]` et les valeurs 1 et 2 pour les indices doit retourner -740.8569952808871 car le tour `["Marseille", "Lyon", "Paris", "Lille"]` a une distance totale de 1708.0796060895232 et `["Marseille",  "Paris", "Lyon", "Lille"]` a une distance totale de 2448.9366013704102.

### Question 11

On peut chercher à améliorer un tour en explorant toutes les inversions possibles et en appliquant l'inversion permettant d'obtenir le plus petit tour si cela l'améliore, c'est-à-dire donne un nouveau tour avec une distance strictement plus petite. Si aucune inversion n'améliore la distance du tour, on ne fait rien. Définir la fonction `better_inversion` prenant en paramètre un tour et un dictionnaire de distances et appliquant cette amélioration au tour si elle existe. La fonction doit renvoyer `True` si une inversion du tour a été faite, et `False` sinon.

L'appel de cette fonction avec le dictionnaire de distances donné en exemple et le tour `["Marseille", "Paris", "Lyon", "Lille"]` doit retour `True` et modifier le tableau pour qu'il soit égal à `["Paris", "Marseille", "Lyon", "Lille"]`.

Par contre, L'appel de la fonction avec le dictionnaire de distances donné en exemple et le tour `["Marseille", "Lyon", "Lille", "Paris"]` doit retourner `False` et ne pas modifier le tour car aucune inversion donne un tour de plus petite distance.

### Question 12

L'amélioration de la question précédente peut généralement être appliquée plusieurs fois. Définir la fonction `best_obtained_with_inversions` prenant en paramètre un tour et un dictionnaire de distances. La fonction doit effectuer successivement des améliorations par inversion comme indiqué dans la question précédente. Elle s'arrête lorsque aucune inversion ne peut améliorer le tour. La fonction retournera le nombre d'inversions effectuées.

L'appel de la fonction avec le dictionnaires de distances donné en exemple et le tour `["Marseille", "Paris", "Lyon", "Lille"]` doit retourner 2 et modifier le tour pour qu'il soit égal à `["Marseille", "Lyon", "Lille", "Paris"]`.
En effet, la meilleure amélioration du tour `["Marseille", "Paris", "Lyon", "Lille"]` est le tour `["Marseille", "Lyon", "Paris", "Lille"]`, et la meilleure amélioration de ce dernier est `["Marseille", "Lyon", "Lille", "Paris"]`. Il n'est pas possible d'améliorer ce tour par une inversion.


### Question 13

Comparer expérimentalement les différentes manières d'obtenir un tour : 
- algorithme construisant un tour en ajoutant successivement la ville la plus proche (en partant d'une ville aléatoire),
- cet algorithme répété en essayant chaque ville comme ville de départ,
- l'utilisation de la méthode d'amélioration par inversion pour améliorer les tours obtenus par les deux précédentes méthodes, 
- d'autres méthodes que vous aurez implémentées (optionnel).

Comparer pour plusieurs fichiers de villes le temps d'exécution et la qualité des solutions obtenues par les différentes méthodes. Quelle est la meilleure méthode ?


## Développement et rendu

La SAÉ devra être faite en binôme. Les fonctions doivent être implémentées dans un module appelé `santa_claus.py` et les tests unitaires des fonctions dans le module `test_santa_claus.py`. Les comparaisons théoriques et expérimentales demandées devront être données dans un notebook appelé `using_santa_claus.ipynb`. 

