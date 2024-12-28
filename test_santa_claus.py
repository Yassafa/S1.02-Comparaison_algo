from math import *
from santa_claus import *

dico_exemple = {
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
def test_dictionary_cities():
    assert dictionary_cities(["Paris",2.33, 48.86, "Lyon", 4.85, 45.75, "Marseille", 5.40, 43.30, "Lille", 3.06, 50.63]) == dico_exemple
    assert dictionary_cities([]) == {}
    assert dictionary_cities(["Paris",2.33,48.86]) == {"Paris":{}}
    print("test de la fonction dictionary_cities : ok")

def test_distance_cities():
    assert distance_cities("Bordeaux","Paris",dico_exemple) == -1
    print("test de la fonction distance_cities : ok")

def test_tour_length():
    assert isclose(tour_length(["Paris", "Lyon", "Marseille", "Lille"],dico_exemple),1708.0796060895232)
    print("test de la fonction tour_length : ok")

def test_closest_city():
    assert closest_city("Paris",["Marseille","Lyon"],dico_exemple) == 1
    assert closest_city("Marseille",["Lyon","Lille"],dico_exemple) == 0
    print("test de la fonction closest_city : ok")

def test_tour_from_closest_city():
    assert tour_from_closest_city("Marseille",dico_exemple) == ["Marseille", "Lyon", "Paris", "Lille"]
    assert tour_from_closest_city("Lyon",[]) == []
    print("test de la fonction tour_from_closest_city : ok")

def test_best_tour_from_closest_city():
    assert best_tour_from_closest_city(dico_exemple) == ["Paris", "Lille", "Lyon", "Marseille"] or best_tour_from_closest_city(dico_exemple) == ["Lyon", "Marseille", "Paris", "Lille"]
    assert best_tour_from_closest_city({}) == []
    print("test de la fonction best_tour_from_closest_city : ok")

def test_reverse_part_tour():
    tab = ["Agen", "Belfort", "Cahors", "Dijon", "Épinay", "Fréjus", "Grenoble", "Hyères"]
    reverse_part_tour(tab,2,5) 
    assert tab == ["Agen", "Belfort", "Fréjus","Épinay", "Dijon", "Cahors", "Grenoble", "Hyères"]
    tab2 = ["a","e","i","o","u"]
    reverse_part_tour(tab2,1,2) 
    assert tab2 == ["a","i","e","o","u"]
    print("test de la fonction reverse_part_tour : ok")

def test_inversion_length_diff():
    assert  isclose(inversion_length_diff(["Marseille", "Lyon", "Paris", "Lille"],dico_exemple,1,2),-740.8569952808871)
    assert inversion_length_diff(["Marseille", "Lyon", "Paris", "Lille"],dico_exemple,0,0) == 0
    print("test de la fonction inversion_length_diff : ok")

def test_better_inversion():
    tab = ["Marseille", "Paris", "Lyon", "Lille"]
    assert better_inversion(tab,dico_exemple) == True
    assert tab == ["Paris", "Marseille", "Lyon", "Lille"]
    tab2 = ["Marseille", "Lyon", "Lille", "Paris"]
    assert better_inversion(tab2,dico_exemple) == False
    assert tab2 == ["Marseille", "Lyon", "Lille", "Paris"]
    print("test de la fonction better_inversion")

def test_best_obtained_with_inversion():
    tab = ["Marseille", "Paris", "Lyon", "Lille"]
    assert best_obtained_with_inversions(tab,dico_exemple) == 2
    assert tab == ["Marseille", "Lyon", "Lille", "Paris"]
    print("test de la fonction best_obtained_with_inversion : ok")