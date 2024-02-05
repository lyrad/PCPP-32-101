# Basic exemple
class Person:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f"{self.name} marche.")


class Fish:
    def __init__(self, name):
        self.name = name

    def swim(self):
        print(f"{self.name} nage.")


volunteers = [Person("Alice"), Fish("Wanda"), Person("Bob")]

for volunteer in volunteers:
    try:
        volunteer.walk()
    except AttributeError:
        volunteer.swim()