## Polymorphism.
# With string / ints
a = 10
print(a.__add__(20)) # 30
b = 'abc'
print(b.__add__('def'))  # abcdef

# With inheritance.
# Inheritance can be used to create polymorphic behavior, but that's not what polymorphism is about.
# When all instances define a method overloading their parent's method, to define a different behavior.

# With Duck typing.
# When An object suitability is determined by the presence of certain attributes, rather than by the object type itself.
for element in 'object1', 'object2', 'object3', 'object4':
    try:
        # If element does not have a melt method, exception and another behavior may be then defined.
        element.melt()
    except AttributeError:
        print('No melt() method')
        try:
            element.fire()
        except AttributeError:
            print('No fire() method')


## Multiple inheritance: The diamond problem
# mro: C3 linearization algorithm.
class A:
    def info(self):
        print('Class A')

class B(A):
    def info(self):
        print('Class B')

class C(A):
    def info(self):
        print('Class C')

class D(C, B): pass

# Class B (resolve from left).
D().info()
print()

try:
    # TypeError: Cannot create a consistent method resolution order(MRO) for bases A, B.
    # A and B not same 'level" (B inherits from A...).
    class E(A, B):
        pass

    E().info()
except TypeError as e:
    print(e.args)
    pass

