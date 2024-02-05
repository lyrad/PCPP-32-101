### Bases of OOP.

## Basic class.
# Instance attributes.
# Attributes/methods visibility.
class Duck:
    class_var = 'myclassduck'

    def __init__(self, height=2, weight=2.4, sex='male'):
        # Instance attributes.
        self.height = height
        self.weight = weight
        self.sex = sex
        # Protected attribute (_).
        # Supposed to limit attribute visibility to class and subclass.
        # But in fact, still can access from outside with <obj>.getattr(<attr>), obj.<attr>, obj[<attr>].
        self._color = 'green'
        # Private attribute (__).
        # Supposed to limit attribute visibility to class.
        # But in fact, still can access from outside.
        self.__food = 'bread'

    def walk(self):
        pass

    def quack(self):
        return 'Quack'

    def double_quack(self):
        # Self to refer to internal methods.
        return self.quack() + self.quack()

    # Property decorator.
    # The method will behave as an attribute.
    # Used to access private, and protected attributes.
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @name.deleter
    def name(self):
        del self._name


# Create some class instances, using named parameters.
duckling = Duck(height=10, weight=3.4)
drake = Duck(height=25, weight=3.7)
hen = Duck(height=20, weight=3.4, sex="female")

# Instance method access.
print(drake.quack())
print(Duck.quack(drake))   # Working?
print(Duck().double_quack())

# Instance attribute access.
print(duckling.height)
duckling.new_var = 'new_var'
print(duckling.new_var, duckling.__getattribute__('new_var'), getattr(duckling, 'new_var'))

# Instance protected attribute access.
# Even when marked protected, still can be accessed.
print(getattr(duckling, '_color'))
setattr(duckling, '_color', 'red')
print(duckling._color)
# name behave as an attribute because of @property and @property.setter decorators.
duckling.name = 'CoinCoin'
print(duckling.name)
# Protected attribute _name can still be accessed from outside.
print(duckling._name)

# Instance private attribute access
try:
    # Can't access a private attribute from outside.
    print(duckling.__food)
except AttributeError:
    pass
finally:
    # In fact you still can but should not.
    print(duckling._Duck__food)

# Returns a dictionary {'attributes' => 'value'}.
# Contains all INSTANCE attributes types (private: _Duck__food).
print(duckling.__dict__)

# Display class/instance metadata.
print(Duck.__class__)  # type => generic for classes.
print(duckling.__class__)  # __main__.Duck => <scope>.<className>
print(duckling.sex.__class__)  # <class 'str'>
print(duckling.quack.__class__)  # <class 'method'>


## More advanced class.
# Class attributes.
class Mobile:
    # Will be shared in all class instances (reading/writting).
    description = 'Allows to make calls and a lot more.'
    counter = 0

    def __init__(self, number):
        self.number = number
        # Also use class name to update class variable from inside (same thing from outside).
        Mobile.counter += 1

    def turn_on(self):
        return print('Mobile phone ' + self.number + ' is turned ON.')

    def turn_off(self):
        return print('Mobile phone ' + self.number + ' is turned OFF.')

    def call(self, number):
        return print('Mobile phone ' + self.number + ' is calling ' + number)


mobile1 = Mobile('0606060606')
mobile1.turn_on()
mobile1.call('0808080808')
mobile1.turn_off()

mobile2 = Mobile('0707070707')
# May access a class variable by instance.
print(mobile2.description)
# But can't write a class variable by instance (would define an instance variable overwritting the class variable).
mobile2.description = 'updated'
print(mobile2.description)  # updated
print(mobile1.description)  # original value.
# A class variable should be updated using class name.
Mobile.description = 'really updated'
print(Mobile.description)  # really updated
print(mobile1.description)  # really updated
print(mobile2.description)  # updated (overwritten)
print(mobile2.counter)  # 2 (not overwritten)
# __dict__ does not contain class variables when called on instance.
print(mobile1.__dict__)
print(Mobile.__dict__)


