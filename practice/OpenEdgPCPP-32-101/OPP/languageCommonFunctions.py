# dir(): Glance at an object’s capabilities and returns a list of the attributes and methods of the object.
# Will return the  result of the __dir__(self) magic method.
print(dir(10))

# help(): Display documentation
# Will display content of the __doc__ magic attribute.
# help(10)

# print(): Print may be called with no/many argument(s).
# Will display result of the __str__() magic method.
print(1, 2)

# type(<instance>)|type(<class>, (<inheriting_classes), <class_attributes>).
# Gives the type of an object, or create a class (with additional args).
# Returns the value of class __bases__ special attribute.
# type is also the foremost type that any class can be inherited from.
print(type('my_string'))  # <class 'str'>
# Create a MyClass class, inheriting list in second arg, class args as a dictionary in 3rd arg.
# ! __b will not be seen as private (not turned to '__MyClass_b').
MyClass = type('MyClass', (), dict(a=1, __b=2))
obj = MyClass()
print(type(obj))  # <class '__main__.MyClass'>
print(type(MyClass))  # <class 'type'>

# getattr(<instance|class>, <attr>).
# Will call the __getattribute__() magic method (__getattr__ called when attribute not found with __getattribute__).
# Get a instance or class attribute. When private: _<ClassName>__<attribute_name>.
print(getattr(obj, 'a'))  # 1 (type: int).
print(getattr(MyClass, 'a'))  # 1 (type: int).
print(getattr(MyClass, '__b'))  # 2 (type: int). When created with 'type', not seen as private...

# setattr(<instance|class>, <attribute>, <value>)
# Will call the __setattr__() magic method.
# Works on instance and class var.
setattr(MyClass, 'c', 3)  # MyClass.c = 3 works.
print(MyClass.c)  # 3, c class variable.
print(obj.c)  # 3: class variable can be accessed from object.
setattr(obj, 'd', 4)  # obj.d = 4 works.
obj.d = 4
print(obj.d)  # 4.
# print(MyClass.d)  # AttributeError: added on object so instance variable not visible by class.

# hasattr(<instance|class>, <attribute>).
# No dedicated magic method.
# Return true when instance or class has variable.
print(hasattr(obj, 'd'))  # True.
print(hasattr(MyClass, 'd'))  # False (d not a class variable).
print(hasattr(obj, 'c'))  # True (c class variable but can be accessed from instance).
print(hasattr(MyClass, 'c'))  # True.

# issubclass(<Class>, <ParentClass>).
# Will call the __subclasscheck__(self, subclass)
# Is the provided class inheriting from the provided parent class (any level).

# isinstance(<instance>, <Class>).
# Will call the __instancecheck__(self, instance)
# Is the provided instance an instance of the provided class (or its parent class).

# id()
# Returns an unique identifier of an object (the 'memory address' ?).

# <str>.isalpha().
# Is the string alphanumeric.

print()

# Type conversion: int(), float(), oct(), hex()
## Object introspection
# str()	    __str__(self)	            responsible for handling str() function calls
# repr()	__repr__(self)	            responsible for handling repr() function calls
# format()	__format__(self, formatstr)	called when new-style string formatting is applied to an object
# hash()	__hash__(self)	            responsible for handling hash() function calls
# dir()	    __dir__(self)	            responsible for handling dir() function calls
# bool()	__nonzero__(self)	        responsible for handling bool() function calls
## Object retrospection
# isinstance(object, class)	    __instancecheck__(self, object)	    responsible for handling isinstance() function calls
# issubclass(subclass, class)	__subclasscheck__(self, subclass)	responsible for handling issubclass() function calls

## Methods allowing access to containers
## Complete list: https://docs.python.org/3/reference/datamodel.html#special-method-names
# len(container)	        __len__(self)	                returns the length (number of elements) of the container
# container[key]	        __getitem__(self, key)	        responsible for accessing (fetching) an element identified by the key argument
# container[key] = value	__setitem__(self, key, value)	responsible for setting a value to an element identified by the key argument
# del container[key]	    __delitem__(self, key)	        responsible for deleting an element identified by the key argument
# for element in container	__iter__(self)	                returns an iterator for the container
# item in container	        __contains__(self, item)	    responds to the question: does the container contain the selected item?