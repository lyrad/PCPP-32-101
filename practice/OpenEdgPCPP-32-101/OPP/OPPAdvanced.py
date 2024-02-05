import abc

## Definitions.
# Encapsulation:
# A technique used to hide the internal implementation details of an object from its external users.
# It provides data protection and ensures that the object's internal state can only be modified through defined methods.

# Method overriding vs. method overloading:
# Method overriding allows a subclass to provide a different implementation of a method inherited from a superclass.
# Method overloading allows a method to have multiple definitions (same scope) with different parameters (last definition used).

## Class Method.
# Used for class variables access or to access class itself (can serve as alternative constructors for instance).
class ExampleCounter:
    __internal_counter = 0

    def __init__(self, value):
        ExampleCounter.__internal_counter +=1

    @classmethod
    def get_internal(cls):
        # Access __internal_counter class variable.
        return '# of objects created: {}'.format(cls.__internal_counter)


print(ExampleCounter.get_internal())

example1 = ExampleCounter(10)
print(ExampleCounter.get_internal())

example2 = ExampleCounter(99)
print(ExampleCounter.get_internal())
print("##########")

# Define a alternative constructor.
class Car:
    def __init__(self, vin):
        print('Ordinary __init__ was called for', vin)
        self.vin = vin
        self.brand = ''

    @classmethod
    def including_brand(cls, vin, brand):
        print('Class method was called')
        _car = cls(vin) # Return a new instance of the current class.
        _car.brand = brand
        return _car

car1 = Car('ABCD1234')
car2 = Car.including_brand('DEF567', 'NewBrand')

print(car1.vin, car1.brand)
print(car2.vin, car2.brand)
print("##########")

## Static methods.
# When method is not related to the object (class used as a library).
# Can't access the class attributes or methods.
class Bank_Account:
    def __init__(self, iban):
        print('__init__ called')
        self.iban = iban

    def amethod(self):
        pass

    @staticmethod
    def validate(iban):
        if len(iban) == 20:
            return True
        else:
            return False

print(Bank_Account.validate('111-222-333'))
print("##########")


## Abstract class and methods.
# Used with interfaces to enforce the implementation of certain methods in child classes.
# Abstract Base Classe (ABC) can only be inherited from.
class BluePrint(abc.ABC):
    @abc.abstractmethod
    def hello(self):
        pass


class GreenField(BluePrint):
    def hello(self):
        print('Hello')


class RedField(BluePrint):
    def yellow(self):
        pass

# Method overriden, will display hello.
gf = GreenField()
gf.hello()

try:
    # Can't instanciate an abstract class.
    t = BluePrint()
except TypeError:
    pass

try:
    # Can't instanciate a class not overriding all abstract class abstract methods.
    t = RedField()
except TypeError:
    pass

print("##########")


## Attribute encapsulation.
# Encapsulation is used to hide the attributes inside a class like in a capsule.
# May use the @property decorator the enable and control access to attributes.
class TankError(BaseException):
    pass

class Tank:
    def __init__(self, capacity):
        self.capacity = capacity
        self.__level = 0

    # Getter.
    @property
    def level(self):
        return self.__level

    # Setter.
    @level.setter
    def level(self, amount):
        if amount > 0:
            # fueling
            if amount <= self.capacity:
                self.__level = amount
            else:
                raise TankError('Too much liquid in the tank')
        elif amount < 0:
            raise TankError('Not possible to set negative liquid level')

    # Deleter (del object.attribute).
    @level.deleter
    def level(self):
        if self.__level > 0:
            print('It is good to remember to sanitize the remains from the tank!')
        self.__level = None
