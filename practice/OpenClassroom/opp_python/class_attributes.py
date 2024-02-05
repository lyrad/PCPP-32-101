## Basic class
class Rectangle:
    def __init__(self, length, width, color="red"):
        self.length = length
        self.width = width
        self.color = color

    def calculate_area(self):
        return self.length * self.width

    def __repr__(self):
        # Retourne une représentation de l'objet
        return f'Rectange de largeur {self.width} et de longueur {self.length}'

    def __str__(self):
        # Retourne une représentation sous forme de string de l'objet
        return f'Rectangle de surface {self.calculate_area()}'

rectangle = Rectangle(2,3)
print(rectangle.__dict__)

area = rectangle.calculate_area()
# area = Rectangle.calculate_area(rectangle)
print(f'rectangle area: {area}')
# retournent le résultat __str__, prioritaire sur __repr__ dans ces cas.
print(f'rectangle representation str: {rectangle}')
print(rectangle)


## Attributs d'instance, de classe, et statiques (methode only)
class Bird:
    # Ici on défini deux attributs de classe.
    names = ("mouette", "pigeon", "moineau", "hirrondelle")
    positions = {}

    def __init__(self, name):
        # Les attributs définis ici sont des attributs d'instance.
        # Dans toutes les méthodes, self est une convention (dans l'absolu ca marcherait avec un autre nom)
        self.position = 1
        self.name = name

        # On accède à l'attribut de classe depuis l'instance, avec self.
        # On peut donc mettre à jour un attribut de classe depuis une instance, avec self? (j'avais lu le contraire...)
        self.positions[self.position] = self.name

    def getPositions(self):
        # Retourne l'attribut de classe, qui est donc 'mis à jour par self dans le constructeur'
        return Bird.positions

    @classmethod
    def find_bird(cls, position):
        # Ca marcherait avec 'self' (le nom n'est qu'une convention...),
        # mais pour les méthode de classe, cls par (grosse) convention.
        # Retrouve un oiseau selon la position donnée
        if position in cls.positions:
            return f"On a trouvé un {cls.positions[position]} !"

        return "On a rien trouvé..."

    @staticmethod
    def get_definition():
        # Dans une methode statique, self n'est pas défini, mais on peut accéder aux attribut/méthode de classe
        return 'Un piaf avec des ailes et des plumes, ' + Bird.find_bird(1)


# On peut accéder aux variables de classe sans instanciation.
print(f'Bird.names: {Bird.names}')
print(f'Bird.positions: {Bird.positions}')
print(f'find_bird(1): {Bird.find_bird(2)}')

# On instancie un oiseau, et on le retrouve avec la méthode find_bird.
bird = Bird("mouette")
print(f'find_bird(1): {Bird.find_bird(1)}')
print(f'Bird.positions: {Bird.positions}')
print(f'bird.positions: {bird.positions}')
print(f'bird.getPositions: {bird.getPositions()}')
print(Bird.__dict__)

# Appel méthode statique.
print(bird.get_definition())


## Tests scopes, mise à jour depuis l'extérieur de la classe
class Cercle:
    rayon = 2

# Constructeur 'automatique', pas obligé de le déclarer
cercle = Cercle()
# On ne peut pas mettre à jour un attribut de classe, depuis l'extérieur de la classe, à partir d'un objet
cercle.rayon = 3
print(f'cercle.rayon: {cercle.rayon}')
print(f'Cercle.rayon: {Cercle.rayon}')

# Attribut de classe mis à jour, mais pas celui de l'objet
Cercle.rayon = 4
print(f'cercle.rayon: {cercle.rayon}')
print(f'Cercle.rayon: {Cercle.rayon}')