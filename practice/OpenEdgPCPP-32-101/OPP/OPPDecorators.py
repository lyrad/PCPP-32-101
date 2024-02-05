## Decorators can be used to :
#  - The validation of arguments;
#  - The modification of arguments;
#  - The modification of returned objects;
#  - The measurement of execution time;
#  - Message logging;
#  - Thread synchronization;
#  - Code refactorization;
#  - Caching.

## Function decorators.
# Call a function (decorated) from within another function (decorator) that take the decorated function as a parameters.
def simple_decorator(function):
    print('simple_decorator')
    return function


@simple_decorator
def simple_hello():
    print("simple_hello")


# When @simple_decorator is present.
simple_hello()
print('##################################')
print()


## Decorators should be universal (work with any function).
# Closure technique to persist arguments *args, **kwargs.
def simple_decorator(own_function):
    def internal_wrapper(*args, **kwargs):
        print('"{}" was called with the following arguments'.format(own_function.__name__))
        print('\t{}\n\t{}\n'.format(args, kwargs))
        own_function(*args, **kwargs)
        print('Decorator is still operating')

    return internal_wrapper


@simple_decorator
def combiner(*args, **kwargs):
    print("\tHello from the decorated function; received arguments:", args, kwargs)

combiner('a', 'b', exec='yes')
print("##########")


## Decorators can accept their own attributes
def warehouse_decorator(material):
    def wrapper(our_function):
        def internal_wrapper(*args):
            print('<strong>*</strong> Wrapping items from {} with {}'.format(our_function.__name__, material))
            our_function(*args)
            print()
        return internal_wrapper
    return wrapper


@warehouse_decorator('kraft')
def pack_books(*args):
    print("We'll pack books:", args)


@warehouse_decorator('foil')
def pack_toys(*args):
    print("We'll pack toys:", args)


@warehouse_decorator('cardboard')
def pack_fruits(*args):
    print("We'll pack fruits:", args)


pack_books('Alice in Wonderland', 'Winnie the Pooh')
pack_toys('doll', 'car')
pack_fruits('plum', 'pear')
print("##########")


## Decorator stacking.
# @outer_decorator calls @inner_decorator calls function.
def outer_decorator(function):
    print('We are about to call "{}" from outer_decorator'.format(function.__name__))
    # Returns subject_matter_function, button inner_decorator is executed before function is called.
    return function


def inner_decorator(function):
    print('We are about to call "{}" from inner_decorator'.format(function.__name__))
    return function


@outer_decorator
@inner_decorator
def subject_matter_function():
    print('In subject_matter_function')
    pass

abcd = subject_matter_function()
print()
print("##########")


## Decorating functions with classes.
# Class must define the __call__ magic method, defining the object behavior when acting as a function.
class SimpleDecorator:
    def __init__(self, own_function):
        # Assigns a decorated function reference to the self.attribute for later use;
        self.func = own_function

    def __call__(self, *args, **kwargs):
        print('"{}" was called with the following arguments'.format(self.func.__name__))
        print('\t{}\n\t{}\n'.format(args, kwargs))
        # Later use of function's reference.
        self.func(*args, **kwargs)
        print('Decorator is still operating')


@SimpleDecorator
def combiner(*args, **kwargs):
    print("\tHello from the decorated function; received arguments:", args, kwargs)


combiner('a', 'b', exec='yes')
print("##########")

# Decorators with arguments, object style.
class WarehouseDecorator:
    def __init__(self, material):
        self.material = material

    def __call__(self, own_function):
        def internal_wrapper(*args, **kwargs):
            print('<strong>*</strong> Wrapping items from {} with {}'.format(own_function.__name__, self.material))
            own_function(*args, **kwargs)
            print()
        return internal_wrapper


@WarehouseDecorator('kraft')
def pack_books(*args):
    print("We'll pack books:", args)


@WarehouseDecorator('foil')
def pack_toys(*args):
    print("We'll pack toys:", args)


@WarehouseDecorator('cardboard')
def pack_fruits(*args):
    print("We'll pack fruits:", args)


pack_books('Alice in Wonderland', 'Winnie the Pooh')
pack_toys('doll', 'car')
pack_fruits('plum', 'pear')
print("##########")


## Class decorators (same syntax than function decorators).
def object_counter(class_):
    class_.__getattr__orig = class_.__getattribute__

    def new_getattr(self, name):
        if name == 'mileage':
            print('We noticed that the mileage attribute was read')
        return class_.__getattr__orig(self, name)

    class_.__getattribute__ = new_getattr
    return class_


@object_counter
class Car:
    def __init__(self, VIN):
        self.mileage = 0
        self.VIN = VIN

car = Car('ABC123')
print('The mileage is', car.mileage)
print('The VIN is', car.VIN)

