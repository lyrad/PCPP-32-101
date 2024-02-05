import traceback
# ImportError: Can't import a module. Agrs: args, name, path
# UnicodeError: Unicode-related encoding or decoding error. Args: encoding, reason, object, start, end.
# AttributeError: When trying to access an undefined attribute.
# BaseException: Root od the exception hierarchy (Exception is a subclass).


## Simple exemple.
try:
    import abcdefghijk

except ImportError as e:
    #  BaseException attribute.
    print(e.args)  # ("No module named 'abcdefghijk'",)

    print(e.name)  # Not a default attribute.
    print(e.path)  # Not a default attribute.


print()

## Implicitly chained exceptions:
# __context__ references the n+1 exception level ($e->getParent php).
a_list = ['First error', 'Second error']

try:
    print(a_list[3])
except Exception as e:
    try:
        # the following line is a developer mistake - they wanted to print progress as 1/10	but wrote 1/0
        print(1 / 0)
    except ZeroDivisionError as f:
        print('Inner exception (f):', f)
        print('Outer exception (e):', e)
        print('__context__: Outer exception referenced:', f.__context__)  # display e name/args (srt())
        print('__context__: Is it the same object:', f.__context__ is e)  # True, it is a reference.
        print('__cause__:', f.__cause__)  # None: __cause__ for explicit exceptions.
        print('__traceback__:', f.__traceback__)  # Traceback object.


print()


## Explicitly chained exceptions:
class RocketNotReadyError(Exception):
    pass


def personnel_check():
    try:
        print("The captain's name is", crew[0])
        print("The pilot's name is", crew[1])
        print("The mechanic's name is", crew[2])
        print("The navigator's name is", crew[3])
    except IndexError as e:
        raise RocketNotReadyError('test') from e



crew = ['John', 'Mary', 'Mike']
print('Final check procedure')

try:
    personnel_check()
except RocketNotReadyError as f:
    # The __cause__ attribute allows to access the higher level exception.
    print(f.__cause__)  # list index out of range.
    print(f.__context__)  # Also working?? Supposed to be only for the implicit exceptions... meh.
    print('General exception: "{}", caused by "{}"'.format(f, f.__cause__))

    # Traceback attribute: __traceback__
    print(traceback.format_tb(f.__traceback__))  # Format traceback object to a list of strings.
    traceback.print_tb(f.__traceback__)  # Print the as a list of strings to the standard output.


class OwnMath:
    pass

def c(num, dem):
    try:
        v = num / dem
    except ZeroDivisionError as e:
        raise OwnMath from e
    return v

c(2,0)