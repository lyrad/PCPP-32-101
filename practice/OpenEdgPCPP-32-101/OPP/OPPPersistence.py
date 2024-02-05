import pickle
# pickle may raise PicklingError, RecursionError or AttributeError exceptions.
# pickle not secured, do not load from untrusted data.
# pickle is evolving, use the same versions for serialization / deserialization.
# function definition cannot be pickled.
import shelve

### Pickle.
# Generally used for serializing a single object at a time.
a_dict = dict()
a_dict['EUR'] = {'code': 'Euro', 'symbol': '€'}
a_dict['GBP'] = {'code': 'Pounds sterling', 'symbol': '£'}
a_dict['USD'] = {'code': 'US dollar', 'symbol': '$'}
a_dict['JPY'] = {'code': 'Japanese yen', 'symbol': '¥'}

a_list = ['a', 123, [10, 100, 1000]]

## Binary serialization.
# Write the output to a file (b for binary).
with open('multidata.pckl', 'wb') as file_out:
    pickle.dump(a_dict, file_out)
    pickle.dump(a_list, file_out)

with open('multidata.pckl', 'rb') as file_in:
    data1 = pickle.load(file_in)
    data2 = pickle.load(file_in)


print(type(data1))
print(data1)
print(type(data2))
print(data2)

# dumps / loads: return / except a byte object.
a_list = ['a', 123, [10, 100, 1000]]
bytes = pickle.dumps(a_list)
print('Intermediate object type, used to preserve data:', type(bytes))

b_list = pickle.loads(bytes)
print('A type of deserialized object:', type(b_list))
print('Contents:', b_list)



## Functions.
def f1():
    print('Hello from the jar!')


with open('function.pckl', 'wb') as file_out:
    pickle.dump(f1, file_out)


# Will not work if f1 not defined (this code runs in another file where f1 not previously defined.
# Same thing with objects.
with open('function.pckl', 'rb') as file_in:
    data = pickle.load(file_in)


print(type(data))
print(data)
data()


### Shelve.
# The dictionary keys MUST be strings.
# Changes are buffered, call sync to flush (or close).
# Dictionary functions work on shelve objects.
# Allows you to serialize multiple objects at times.
# Built on pickle module.
# r: read, w: read and write, c: read, write, create when not exist, n: read, write, always recreate.
my_shelve = shelve.open('first_shelve.shlv', flag='c')
my_shelve['EUR'] = {'code': 'Euro', 'symbol': '€'}
my_shelve['GBP'] = {'code': 'Pounds sterling', 'symbol': '£'}
my_shelve['USD'] = {'code': 'US dollar', 'symbol': '$'}
my_shelve['JPY'] = {'code': 'Japanese yen', 'symbol': '¥'}
my_shelve.close()

new_shelve = shelve.open('first_shelve.shlv')
print(new_shelve['USD'])
new_shelve.close()

# When used as a context manager, no need to close the file.
with shelve.open('first_shelve.shlv', 'w') as db:
    db['key'] = 'value'