## No class, make a list iterable.
users = ['Alice', 'Bob', 'Carl', 'David']
# convert the list to an iterator
users_iterator = iter(users)
x = next(users_iterator)
print(x)
# Output: 'Alice'
x = next(users_iterator)
print(x)
# Output: 'Bob'
x = next(users_iterator)
print(x)
# Output: 'Carl'
x = next(users_iterator)
print(x)

## Iterable class.
# The Iterable object implements __iter__() method and returns an Iterator object.
# The Iterator object implements the __next__() method and raises a StopIteration when the elements of the iterable object are exhausted.
# Additionally, the Iterator object is itself an Iterable as it must also implement the __iter__() method and simply return itself.

class Counter:
    def __init__(self, low, high):
        self.current = low - 1
        self.high = high

    def __iter__(self):
        return self

    def __next__(self): # Python 2: def next(self)
        self.current += 1
        if self.current < self.high:
            return self.current
        raise StopIteration


for c in Counter(3, 9):
    print(c)

##########


class Playlist:
    def __init__(self):
        self.songs = ['song0', 'song1', 'song2']
        self.current = 0
        pass

    def add_song(self, song):
        self.songs.append(song)

    # Returns an iterator (any object with a method called next).
    def __iter__(self):
        return self

    # Returns iterators "next" value.
    # In fact, returns current and pass to next.
    def __next__(self):
        if self.current == len(self.songs):
            raise StopIteration

        current_song = self.songs[self.current]
        self.current += 1
        return current_song

p = Playlist()
for song in p:
    print(song)
