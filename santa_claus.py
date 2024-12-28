from time import time
from math import *
from numpy import *
from random import *

##############
# SAE S01.01 #
##############

def nb_villes(villes):
    """Retourne le nombre de villes"""
    return len(villes)//3


def noms_villes(villes):
    """Retourne un tableau contenant le nom des villes"""
    noms_v = []
    i = 0
    while 3*i < len(villes):
        noms_v.append(villes[3*i])
        i += 1
    return noms_v


def d2r(nb):
    return nb*pi/180


def distance(long1, lat1, long2, lat2):
    """retourne la distance entre les points (long1, lat1) et (long2, lat2)"""
    lat1 = d2r(lat1)
    long1 = d2r(long1)
    lat2 = d2r(lat2)
    long2 = d2r(long2)
    R = 6370.7
    d = R*arccos(sin(lat1)*sin(lat2)+cos(lat1)*cos(lat2)*cos(long2-long1))
    return d


def indexCity(ville, villes):
    """Retourne l'indice dans le tableau villes de la ville de nom ville,
       et -1 si elle n'existe pas
    """
    res = -1
    i = 0
    while 3*i < len(villes) and villes[3*i] != ville:
        i += 1
    if 3*i < len(villes):
        res = 3*i
    return res


def distance_noms(nom1, nom2, villes):
    """Retourne la distance entre les villes nom1 et nom2
       en fonction de la structure de données villes
    """
    index1 = indexCity(nom1, villes)
    index2 = indexCity(nom2, villes)

    if index1 == -1 or index2 == -1:
        d = -1
    else:
        d = distance(villes[index1+1], villes[index1+2],
                     villes[index2+1], villes[index2+2])
    return d


def lecture_villes(path):
    """Retourne la structure de données villes en fonction des données du fichier path"""
    f_in = open(path, encoding='utf-8', mode='r')
    villes = []
    li = f_in.readline()
    li = li.strip()
    while li != '':
        tab_li = li.split(';')
        villes.append(tab_li[0])
        villes.append(float(tab_li[1]))
        villes.append(float(tab_li[2]))
        li = f_in.readline()
        li = li.strip()
    f_in.close()
    return villes


def long_tour(villes, tournee):
    """Retourne la longueur d'une tournée en fonction de la structure de données villes"""
    long = 0
    i = 0
    while i+1 < len(tournee):
        long += distance_noms(tournee[i], tournee[i+1], villes)
        i += 1
    long += distance_noms(tournee[i], tournee[0], villes)
    return long

##############
# SAE S01.02 #
##############

exemple = {'Paris': {'Lyon': 394.5056834297657,'Marseille': 661.8616554466852,'Lille': 203.67224282542662},'Lyon': {'Paris': 394.5056834297657,'Marseille': 275.87965367431525,'Lille': 558.5472363339435},'Marseille': {'Paris': 661.8616554466852,'Lyon': 275.87965367431525,'Lille': 834.0220261600157},'Lille': {'Paris': 203.67224282542662,'Lyon': 558.5472363339435,'Marseille': 834.0220261600157}}

# Question 1
def dictionary_cities(villes):
    """Prend en paramètre un tableau de villes et renvoie un dictionnaire contenant
    les distances entre les villes du tableau"""
    d = {}
    tab = noms_villes(villes)
    i = 0
    while i < len(tab):
        d[tab[i]] = {}
        j = 0
        while j < len(tab):
            if tab[i] != tab[j]:
                d[tab[i]][tab[j]] = distance_noms(tab[i],tab[j],villes)
            j += 1
        i += 1
    return d

# Question 2
def distance_cities(name1, name2, d_cities):
    """Renvoie la distance entre les villes name1 et name2 si elles sont dans
    le dictionnaire et -1 sinon"""
    if name1 in d_cities and name2 in d_cities[name1]:
        return d_cities[name1][name2]
    else:
        return -1


# Question 3
def tour_length(tour, d_cities):
    """retourne la longeur du tour passé en paramètre"""
    distance = 0
    i = 0
    while i < len(tour)-1:
        distance += distance_cities(tour[i],tour[i+1],d_cities)
        i += 1
    distance += distance_cities(tour[-1],tour[0],d_cities)
    return distance


# Question 5
def closest_city(city, cities, d_cities):
    """Retourne l'indice de la ville la plus proche de la ville passée en paramètre"""
    closest_distance = inf
    i = 0
    while i < len(cities):
        if distance_cities(cities[i],city,d_cities) < closest_distance:
            closest_distance = distance_cities(cities[i],city,d_cities)
            city_index = i
        i += 1
    return city_index

# Question 6
def tour_from_closest_city(city, d_cities):
    """Renvoie un tour en partant de la ville passée" en paramètre et en ajoutant à
    chaque fois la ville la plus proche de la dernière"""
    tab = list(d_cities)
    tour = []
    while tab != []:
        next_city = closest_city(city,tab,d_cities)
        tour.append(tab[next_city])
        city = tab[next_city]
        tab.pop(next_city)
    return tour

# Question 7
def best_tour_from_closest_city(d_cities):
    """Retourne le meilleur tour parmi ceux obtenus avec l'algorithme précédent en
    prenant chaque ville comme ville de départ"""
    best_distance = inf
    best_tour = []
    for city in d_cities.keys():
        tour = tour_from_closest_city(city,d_cities)
        if tour_length(tour,d_cities) < best_distance:
            best_distance = tour_length(tour,d_cities)
            best_tour = tour
    return best_tour

# Question 8
# La fonction best_tour_from_closest_city a une complexité quadratique car elle contient
# une boucle qui elle même fait appel à la fonction tour_from_closest_city qui contient
# aussi une boucle

# Question 9
def reverse_part_tour(tour, ind_b, ind_e):
    """Inverse la partie du tableau passé en paramètre située entre ind_b et ind_e inclus"""
    i = ind_b
    j = ind_e
    while i < j:
        tour[i], tour[j] = tour[j], tour[i]
        i += 1
        j -= 1

# Question 10
def inversion_length_diff(tour, d_cities, ind_b, ind_e):
    """Retourne la différence entre la distance du tour passé en paramètre et celui obtenu en
    inversant la partie du tour entre les ind_b et ind_e inclus"""
    a = tour_length(tour,d_cities)
    reverse_part_tour(tour,ind_b,ind_e)
    b = tour_length(tour,d_cities)
    reverse_part_tour(tour,ind_b,ind_e)
    return a - b


# Question 11

def better_inversion(tour, d_cities):
    """Compare toutes les inversions possibles du tour et remplace tour par la
    meilleure inversion. Renvoie True si une inversion a été faite, False sinon"""
    inversion = False
    j = len(tour) - 1
    while j > 0:
        i = 0
        while i < j:
            if inversion_length_diff(tour,d_cities,i,j) > 0:
                reverse_part_tour(tour,i,j)
                inversion = True
            i += 1
        j -= 1
    return inversion

# Question 12
def best_obtained_with_inversions(tour, d_cities):
    """Effectue plusieurs améliorations par inversions en utilisant l'algorithme précédent
    jusqu'à ce qu'aucune amélioration ne soit possible. Renvoie le nombre d'améliorations
    effectuées"""
    nb_inversions = 0
    while better_inversion(tour,d_cities):
        nb_inversions += 1
        print(nb_inversions,tour)
    return nb_inversions