## Methods.
# __new__(mcs, name, bases, attrs)
# Executed when class instantiated, allows to add (class) attributes to the class.
# Responsive for creating a new instance of a class before it is initialized.
# Used in meta classes.

# __init__(self)
# Class constructor. May be omitted, child class world inherit if not overridden.

# Numeric unary: __pos__, __neg__, __abs__, __round__
# Numeric binary operators (augumented: _iadd__, __isub__, __imul__...).
# __add__(): var1 + var2 <===> var1.__add__(var2).
# __sub__(): var1 - var2 <===> var1.__sub__(var2).
# __mul__(): var1 * var2 <===> var1.__mul__(var2).
# __truediv__(): var1 / var2 <===> var1.__truediv__(var2) (__div__: python 2).
# __floordiv__(): var1 // var2 <===> var1.__floordiv__(var2) (integer division).
# __pow__(): var1 ** var2 <===> var1.__pow__(var2).
# __matmul__(): matrix multiplication (@).
#  __mod__(): var1 % var2 <===> var1.__imod__(var2).

# Comparison operators.
# __eq__(), __ne__(), __lt__(), __le__(), __gt__(), __ge__()
# When ==, !=, <, <=, >, >= are called to compare objects.
# __contains__(self, val): called when "'value' in obj" called.

# __iter__() and __next__()
# Iterators methods, allow an object to be used in a for loop.

# __str__()
# Converting an object's contents into a more or less readable string representation.
# Used when str() or print() methods are called on the object.

# __len__()
# Used when len() is called on the object.

# __size__()

# __count__()

# __repr__()
# Return a more detailed and unambiguous (formal) representation of an object (can be used to recreate the object).
# Used for debugging or informational purposes, and is invoked when the repr() function is called on the object.


# __getitem__()
# Allows objects to define their own custom behavior when the index operator ([]) is used on them.
# Should accept an index as an argument and return the corresponding element from the object.

# __setitem__()
# same than __getitem() but when setting value.

# __instancecheck__()
# Handle the isinstance() call on the object.

# __subclasscheck__()
# Handle the issubclass() call on the object.

# __mro__()
# Called when mro() is called on the CLASS (not working on instances, do type(<i>).mro()).
# Tuple of "classes" that represents the method resolution order (MRO) for the class.
# <Child> -> <Parent> -> "object"

# __call__()
# Define the behavior when an object is called as a function.
# Used in decorator (when using a class as a decorator: object style).

# __getattribute__(), __setattr__(), __getattr__()
# When getattr() and setattr() called on the object, __getattr__() called when attr not found with __getattribute__.


## Attributes.
# __name__ : The name of the CLASS object (not working on instances, do type(<i>).__name__ or <i>.__class__.__name__).
# __class__ : The class object (working on instances, returns type for classes).
# __bases__ : Tuple of class objects that classe is DIRECTLY inheriting from. Returned when type called on the object.

# __dict__
# A dictionary or other mapping object used to store an object’s attributes.
# When object is an instance, class attributes won't be part of dict.

# __doc__
# Contain the class/function's docstring (first statement in the class/function body).
# Returned when help() is called on the class/object.

# __context__
# Point the exception that caused the currently handled exception.
# Used in implicit exceptions chaining.

# __cause__
# Point the exception that caused the currently handled exception.
# Used in explicit exceptions chaining.

# __traceback__
# Back trace of the exception
# Used in implicit AND explicit exceptions chaining.
