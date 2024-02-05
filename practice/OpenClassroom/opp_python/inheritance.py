from abc import ABC

## Héritage simple
class Oeuvre(ABC):
    # ABC = Abstract Base Class (Classe abstraite)
    def watch(self):
        print('Surchagée, jamais exécutée')

    # abstract method??? (stop watch)

class Film(Oeuvre):
    def __init__(self, name):
        self.name = name
    def watch(self):
        print(f"Playing '{self.name}'")

    def stop_watch(self):
        print(f"Playing '{self.name}'")

class FilmCassette(Film):
    def __init__(self, name, rewound=True):
        super().__init__(name)
        self.magnetic_tape = True
        self.rewound = rewound

    def rewind(self):
        print(f"'{self.name}' is rewinding")
        super().watch()

class FilmDvd(Film):
    pass

film_cassette = FilmCassette('From dusk till dawn')
film_cassette.watch()

film_cassette = FilmCassette('Plannet terror', False)
film_cassette.rewind()

film_dvd = FilmDvd('Death proof')
film_dvd.watch()


## Héritage multiple
class Cat:
    def meow(self):
        print("Meow!")


class Talker:
    def say(self, to_say):
        print(to_say)


class TalkingCat(Cat, Talker):
    pass


salem = TalkingCat()
salem.meow()
salem.say("Hello Im the cat!")