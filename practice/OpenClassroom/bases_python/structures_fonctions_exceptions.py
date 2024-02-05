from typing import List

## Les fonctions
def afficher_nom_prenom(nom, prenom, optional='default_value'):
    """
    Un doc bloc python pour commenter la fonction d'affichage/retour prenom/nom
    :param nom (string): Nom
    :param prenom (string): Prénom
    :return:
    string: Concaténation prenom et nom
    """
    print("Nom :", nom)
    print("Prénom :", prenom)
    print("Optional :", optional)
    return prenom + ' ' + nom


print(afficher_nom_prenom('Denard', 'Bob'))
print(afficher_nom_prenom(optional='provided_value', prenom='Bob', nom='Denard'))

def retour_multiple():
    return 'hello', 'world'

result = retour_multiple()
print(result)
print(result[0])
print(result[1])


# Typage
def highest(numbers: List[int]) -> int:
    max_value = 0
    for number in numbers:
        if number > max_value:
            max_value = number
    return max_value

# Les 3 marchent, meme si l'éditeur gueule...
print(f'highest number: {highest([0, 8, 4, 9, 350, 54, 100])}')
print(f'highest number: {highest((0, 8, 4, 9, 350, 54, 100))}')
print(f'highest number: {highest({0, 8, 4, 9, 350, 54, 100})}')

## Les exceptions
dictionary = dict()
class MyException(ValueError):
    pass

try:
    x = 10
except ValueError as error:
    print(f'error class: {type(error)}, error message: {error}')
else:
    print('No problemo')

try:
    x = int('str')
except ValueError as error:
    print(f'error class: {type(error)}, error message: {error}')

try:
    my_value = dictionary['key_notHere']
except KeyError as error:
    print(f'error class: {type(error)}, error message: {error}')

try:
    # On peut extend les exceptions, et leur passer un message d'erreur.
    exception = MyException('Error message perso')
    raise exception
except ValueError as error:
    print(f'ValueError: error class: {type(error)}, error message: {error}')
except MyException as error:
    # Pas exécuté, car un autre block 'valide' est déclaré avant.
    print(f'MyException: error class: {type(error)}, error message: {error}')


