import simplejson as json

## Python to JSON.
# dict => object
# list or tuple => array
# string => string
# int or float => number
# True / False => true / false
# None => null

## Basic serialization.
my_dict = {
    'me': "Python",
    'pi': 3.141592653589,  # int/float => number JSON type.
    'data': (1, 2, 4, 8),
    'list': [1, 2.34, True, "False", None, ['a', 0]],
    'set': None,
    'movie': '"The Meaning of Life" by Monty Python\'s Flying Circus',
    'emptyList': [],
    'emptyDict': {},
}

# Into a string (json.dumps).
my_dict_json = json.dumps(my_dict)

# Into a file (json.dump).
with open('my_dict.json', 'w', encoding='utf-8') as f:
    json.dump(my_dict, f, ensure_ascii=False, indent=4)


## Objects serialization.
class Who:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# First approach: using a dedicated function.
# Should return the object __dict__ or throw an exception.
def json_encode_who(w):
    if isinstance(w, Who):
        return w.__dict__
    else:
        # Type error mandatory to inform dump object is not serializable
        raise TypeError(w.__class__.__name__ + ' is not JSON serializable')


rambo = Who('Sylvester Stallone dedicated function serialization', 80)
# default: function name.
rambo_json = json.dumps(rambo, default=json_encode_who)
print(rambo_json)


# Second approach: create an encoder extending json.JSONEncoder
class MyJsonEncoder(json.JSONEncoder):
    # Function used for serialization, no need to raise an exception.
    def default(self, w):
        if isinstance(w, Who):
            return w.__dict__
        else:
            # When not instance call the parent.
            return super().default(self, w)


rambo = Who('Sylvester Stallone encoder serialization', 90)
# cls: encoder class name.
json_rambo = json.dumps(rambo, cls=MyJsonEncoder)
print(json_rambo)
print('#####################')


## Basic deserialization.
# Types examples.
jnumber = '16021766189.98'
number = json.loads(jnumber)
print(f'type: {type(number)}, value: {number}')

jstr = '"\\"The Meaning of Life\\" by Monty Python\'s Flying Circus"'
str = json.loads(jstr)
print(f'type: {type(str)}, value: {str}')

jlist = '[1, 2.34, true, "False", null, ["a", 0]]'
list = json.loads(jlist)
print(f'type: {type(list)}, value: {list}')

jdict = '{"me":"Python","pi":3.141592653589, "data":[1,2,4,8],"friend":"JSON","set": null}'
dict = json.loads(jdict)
print(f'type: {type(dict)}, value: {dict}')

# From a file.
with open('my_dict.json', 'r', encoding='utf-8') as f:
    print(json.load(f))

## Objects  deserialization.
# First approach: use a dedicated function
def json_decode_who(w):
    return Who(w['name'], w['age'])

rambo = json.loads(
    '{"name": "Sylvester Stallone dedicated function deserialization", "age": 80}',
    object_hook=json_decode_who
)
print(f'type: {type(rambo)}, value: {rambo.__dict__}')


# Second approach: extend json.JSONDecoder
class MyJsonDecoder(json.JSONDecoder):
    # Need to redefine superclass constructor
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.json_decode_who)

    def json_decode_who(self, w):
        # Here w is the dictionary of __init__ arguments (def __init__(self, name, age)), so unpacking the dictionary.
        return Who(**w)
        # BUT: if init is a list (def __init__(self, *list), with Who('hello', 'world', 'kikoo')), unpack the list.
        # return Who(*w['list'])


# ! Does not work since simple json not up to date (TypeError: got an unexpected keyword argument 'encoding')
rambo = json.loads(
    '{"name": "Sylvester Stallone decoder deserialization", "age": 90}',
    cls=MyJsonDecoder
)
print(f'type: {type(rambo)}, value: {rambo.__dict__}')