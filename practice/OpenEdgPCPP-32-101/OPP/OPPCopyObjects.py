import copy

##  With strings.
a_string = 'helloworld'
b_string = 'helloworld'
c_string = a_string

# id(): Memory chunk is same object or not.
print(id(a_string))
print(id(b_string))  # Same than a_string, lol.
print(id(c_string))  # Same than a_string, logic.

# '==' compare the values of two different object, 'is' compare the value of id() (same object or not).
print(a_string == b_string)  # True.
print(a_string == c_string)  # True.
print(a_string is b_string)  # True lol.
print(a_string is c_string)  # True.
print()

##  With lists.
a_string = ['10', 'days', 'to', 'departure']
b_string = ['10', 'days', 'to', 'departure']
c_string = a_string

# id(): Memory chunk is same object or not.
print(id(a_string))
print(id(b_string))  # Not the same, logic behavior.
print(id(c_string))

# '==' compare the values of two different object, 'is' compare the value of id() (same object or not).
print(a_string == b_string)  # True.
print(a_string == c_string)  # True.
print(a_string is b_string)  # False.
print(a_string is c_string)  # True.
print()

## Copying a list:
a_list = ['10', 'days', 'to', 'departure']
b_list = a_list[:]  # Slice function.
c_list = a_list.copy() # Copy (first level, same action than [:]).

print(id(a_list))
print(id(b_list))
print(id(c_list))
print(a_list == b_list)  # True.
print(a_list is b_list)  # False.
print(a_list == c_list)  # True.
print(a_list is c_list)  # False.
print()

## But if another list within the list, compound object, the other list is referenced not copied.
# Copy is only one level deep with slice.
a_list = ['helloworld', [3, 4]]
b_list = a_list[:]
c_list = a_list.copy()
b_list[1][0] = 5
b_list[0] = 'hello'
c_list[1][1] = 6

print(a_list)  # ['helloworld', [5, 6]]: [1][0] updated by b_list update, [1][1] updated by c_list update.
print(b_list)  # ['hello', [5, 6]]: [1][1] updated by c_list update.
print(c_list)  # ['helloworld', [5, 6]]
print(id(a_list))  # First level: All id different, they are not the same object.
print(id(b_list))
print(id(c_list))
print(id(b_list[1]))  # Second level: All id the same, they are the same object.
print(id(b_list[1]))
print(id(c_list[1]))

print(a_list == b_list)  # False.
print(a_list == c_list)  # True.
print(a_list is b_list)  # False.
print()

## Deep copy: copy.deepcopy().
print("Let's make a deep copy")
a_list = [10, "banana", [997, 123]]
b_list = copy.deepcopy(a_list)  # Need copy module to make a total/deep copy.
print("a_list contents:", a_list)
print("b_list contents:", b_list)
print("Content egals?", a_list == b_list)  # True.
print("Is first level the same object?", a_list is b_list)  # False.
print("Is second level the same object?", a_list[2] is b_list[2])  # False.

print()
print("Let's modify b_list[2]")
b_list[2][0] = 112
print("a_list contents:", a_list)
print("b_list contents:", b_list)
print("Is it the same object?", a_list is b_list)


## Dictionnaries ans objects (same behavior than lists).
a_dict = {
    'first name': 'James',
    'last name': 'Bond',
    'movies': ['Goldfinger (1964)', 'You Only Live Twice']
}
b_dict = copy.deepcopy(a_dict)
print('Memory chunks:', id(a_dict), id(b_dict))
print('Same memory chunk?', a_dict is b_dict)
print("Let's modify the movies list")
a_dict['movies'].append('Diamonds Are Forever (1971)')
print('a_dict movies:', a_dict['movies'])
print('b_dict movies:', b_dict['movies'])