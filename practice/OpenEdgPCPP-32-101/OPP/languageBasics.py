## Basics
# Package vs. module.
# A module is a .py file, while a package is a collection of modules.
# A package may include one (or many) __init__.py files to distinguish itself from a directory.
# import my_module
# from mypackage.my_module import my_function

# Tips
print('helloworld', end=' !!!\n')
print('Formatting {} amazing {}'.format('this', 'string'), end=' !!!\n')
print(len('123456789'), end='\n')
var = 'lol'
print(f'kikoo {var}', end='\n')
# random.uniform(0, 5)

## Loop : for
# With values
for var in 4, 3, 2, 1:
    print(var)

# With variables
var1 = 1
var2 = 2
var3 = 3
var4 = 4

for var in var1, var2, var3, var4:
    print(var)

# With objects
class Number:
    def __init__(self, value):
        self.value = value


obj1 = Number(1)
obj2 = Number(2)
obj3 = Number(3)
obj4 = Number(4)

for var in obj1, obj2, obj3, obj4:
    print(var.value)

## Conditional : if
animal = 'duck'
if animal == 'duck':
    print('miam')
elif animal == 'cat':
    print('beurk')
else:
    print('meh')


## Operators.
number = 10
number = number.__add__(10)  # number = number +10
print(number)

# When operation not supported (objects), the magic method can be defined to make it happens.
try:
    # Number (defined earlier, does not define __add__).
    number = Number(10) + Number(10)
except TypeError:
    pass


class Person:
    def __init__(self, weight, age, salary):
        self.weight = weight
        self.age = age
        self.salary = salary

    # Magic method __add__
    def __add__(self, other):
        return self.weight + other.weight

    # Magic method __eq__
    def __eq__(self, other):
        return self.weight == other.weight

    # Magic method __ne__
    def __ne__(self, other):
        return self.weight != other.weight


p1 = Person(60, 40, 50)
p2 = Person(80, 45, 55)

print(p1 + p2)


## Variables types.
namesList = ['Kévin', 'Brian', 'John', 'Bod', 'Bill']
namesTuple = ('Kévin', 'Brian', 'John', 'Bod', 'Bill')
namesSet = {'Kévin', 'Brian', 'John', 'Bod', 'Bill'}

print(type(namesList))
print(namesList[-1])
print(type(namesTuple))
print(namesTuple[-1])
print(type(namesSet))
print()


## Function calls.
# *args: refers to a tuple of all unexpected positional arguments.
# **kwargs: refers to a dictionary of all unexpected named arguments (name=value).
# args/kwargs are convention, but names can be changed in function declaration.
def super_combiner(my_c, *my_args, **my_kwargs):
    print(my_c)  # my_c: 30.
    print(my_args, type(my_args))  # (40, 60, 30) <class 'tuple'>.
    print(my_kwargs, type(my_kwargs))  # {'argument1': 50, 'argument2': '66'} <class 'dict'>


# ! Argument order matters.
#  - Default value args must be declared after non-default value args (1).
#  - *args and **kwargs must be placed AFTER the related positional/named args (2).
#  - *args must be placed BEFORE **kwargs (3)
# Not working: combiner(c=30, a, b, *args, **kwargs): (1)
# Not working: combiner(*args, a, b, c=30, **kwargs), combiner(a, b, *args, **kwargs, c=30) (2)
# Not working: combiner(a, b, c=30, **kwargs, *args) (3)
# Working: combiner(a, b, *args, c=30, **kwargs)
# Working: combiner(a, b, c=30, *args, **kwargs)
def combiner(a, b, *args, c=30, **kwargs):
    print(a, b)  # 10 20
    print(type(b))  # <class 'str'>
    print(c)  # 30 (not given so default)
    print(args)  # (40, 60, 30)
    print(kwargs)  # {'argument1': 50, 'argument2': '66'}

    # How to pass *args and **kwargs to another function, unpacking (no wildcard = ONE arg tuple/dict).
    super_combiner(c, *args, **kwargs)


# When calling, can't have positional arguments AFTER a named argument.
# Not working: combiner(10, '20', 40, argument1=50, argument2='66', 60, 30)
combiner(10, '20', 40, 60, 30, argument1=50, argument2='66')