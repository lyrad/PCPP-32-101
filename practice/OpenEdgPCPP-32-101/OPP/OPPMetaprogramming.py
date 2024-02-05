## Differences decorators / metaclasses.
# Decorators bind the names of decorated functions or classes to new callable objects.
# Class decorators are applied when classes are instantiated.
# Metaclasses redirect class instantiations to dedicated logic, contained in metaclasses.
# Metaclasses are applied when class definitions are read to create classes, well before classes are instantiated.

## Usages
# logging, registering classes at creation time, interface checking, automatically adding new methods, automatically
# adding new variables.

def bark(self):
    print('Woof, woof')

class Dog:
    pass


class Animal:
    def feed(self):
        print('It is feeding time!')

# <class 'type'>: type is the default metaclass responsive for creating classes.
# The type of the metaclass type is type.
# An object is an instance of a class which is an instance of a metaclass.
print(type(Dog))

# When the type() function is called with three arguments, then it dynamically creates a new class.
Cat = type('Cat', (Animal, ), {'age': 0, 'bark': bark})

print('The class name is:', Cat.__name__)  # Cat
print('The class is an instance of:', Cat.__class__)  # <class 'type'>
print('The class is based on:', Cat.__bases__)  # (<class '__main__.Animal'>,)
print('The class attributes are:', Cat.__dict__)  # {'age': 0, 'bark': <function bark at 0x7f0baf26e520>, '__module__': '__main__', '__doc__': None}

cat = Cat()
cat.feed()
cat.bark()
print('#################')
print()

## __new__()
# Adding attribute.
class My_Meta(type):
    # call the __new__ method of the parent class to create a new class.
    def __new__(mcs, name, bases, dictionary):
        new_class = super().__new__(mcs, name, bases, dictionary)
        new_class.custom_attribute = 'Added by My_Meta'
        return new_class


class MyObject(metaclass=My_Meta):
    pass


print(MyObject.__dict__)
print('#################')
print()


# Adding method.
class MyMeta(type):
    # Could be outside the class, or even inside the __new__ method.
    def greetings(self):
        print('Greeting meta function')

    def __new__(mcs, name, bases, dictionary):
        if 'greetings' not in dictionary:
            dictionary['greetings'] = mcs.greetings
        new_class = super().__new__(mcs, name, bases, dictionary)
        return new_class


class MyClass1(metaclass=MyMeta):
    pass


class MyClass2(metaclass=MyMeta):
    def greetings(self):
        print('greetings MyClass2')


myobj1 = MyClass1()
myobj1.greetings()  # Greeting meta function (Added by meta).
myobj2 = MyClass2()
myobj2.greetings()  # greetings MyClass2 (not added because already in dictionary).
print('#################')
print()

# Adding method (constructor overriding).
class Meta(type):
    def __new__(cls, name, bases, attrs):
        new_class = super().__new__(cls, name, bases, attrs)
        new_class.instances = 0
        # Store original __init__ method for later use.
        original_init = new_class.__init__

        def new_init(self, *args, **kwargs):
            # Add operations.
            new_class.instances += 1
            # Call original init.
            original_init(self, *args, **kwargs)

        # Replace original constructor by a new one.
        new_class.__init__ = new_init
        return new_class


class MyClass(metaclass=Meta):
    pass


a = MyClass()
b = MyClass()
c = MyClass()
print(MyClass.instances)  # 3.
print('#################')
print()

# Updating class name.
# Strange example... Make sense when class is instanciated ? If so, redef constructor with __init__.
class Meta(type):
    def __new__(cls, name, bases, dictionary):
        new_class = super().__new__(cls, name, bases, dictionary)
        new_class.__name__ = new_class.__name__.upper()
        return new_class


class MyClass(metaclass=Meta):
    pass


print(MyClass.__name__)  # MYCLASS

