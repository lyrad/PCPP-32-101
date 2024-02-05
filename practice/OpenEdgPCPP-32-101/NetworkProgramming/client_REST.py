import requests
import simplejson as json
import string
import random

## REST: REpresentational, State, Transfer.
## HTTP status code dictionary: print(requests.codes.__dict__)

## HTTP basics request and errors
try:
    # Working.
    # reply = requests.get('http://localhost:3000', timeout=1)
    # Connection error.
    # reply = requests.get('http://localhost:3001', timeout=1)
    # Invalid URL error
    reply = requests.get('http://////', timeout=1)
except requests.exceptions.Timeout:
    print('Sorry, Mr. Impatient, you didn\'t get your data')
except requests.exceptions.ConnectionError as error:
    print(f'error class: {type(error)}, error message: {error}')
except requests.exceptions.InvalidURL as error:
    print(f'error class: {type(error)}, error message: {error}')
else:
    print(reply.status_code)
    print(reply.headers)
    print(reply.headers['Content-Type'])
    # Print the content of server response.
    print(reply.text)

## HTTP CRUD
# READ (GET), LIST
try:
    reply = requests.get("http://localhost:3000/cars")
except requests.RequestException:
    print("Communication error")
else:
    if reply.status_code == requests.codes.ok:
        print(f'The server returned {len(reply.json())} car(s).')
    else:
        print("Server error")


# READ (GET, LIST, SORT BY PROPERTY)
print(f'### READ (GET, LIST, SORT BY PROPERTY)')
try:
    reply = requests.get("http://localhost:3000/cars?_sort=production_year&_order=desc")
except requests.RequestException:
    print("Communication error")
else:
    if reply.status_code == requests.codes.ok:
        print(f'Response status code: ' + str(reply.status_code))
        print(f'Response headers: {reply.headers}')
        print(f'Response content: ({len(reply.json())} car(s)):')
        print(f"id|brand|model|production_year|convertible")
        for car in reply.json():
            print(f"{car['id']}|{car['brand']}|{car['model']}|{car['production_year']}|{car['convertible']}")
    else:
        print("Server error")

# READ (GET, RESOURCE)
print(f'### READ (GET, RESOURCE)')
try:
    reply = requests.get('http://localhost:3000/cars/3')
except requests.RequestException:
    print('Communication error')
else:
    if reply.status_code == requests.codes.ok:
        # Print the content as JSON of server response.
        print(reply.json())
    elif reply.status_code == requests.codes.not_found:
        print("Resource not found")
    else:
        print('Server error')

# CREATE (POST)
print(f'### CREATE (POST)')
new_car = {
    'brand': 'Porsche',
    'model': '911',
    'production_year': 1963,
    'convertible': False
}

try:
    reply = requests.post(
        'http://localhost:3000/cars',
        json=new_car,
        headers={'Connection': 'Close', 'Content-Type': 'application/json'}
    )
except requests.RequestException:
    print('Communication error')
else:
    print('Connection=' + reply.headers['Connection'])
    if reply.status_code == requests.codes.created:
        print(f'Response status code: ' + str(reply.status_code))
        print(f'Response content: ' + str(reply.json()))
        new_car = reply.json()
    elif reply.status_code == requests.codes.not_found:
        print("Resource not found")
    else:
        print(f'Server error {reply.status_code}')

# REMOVE (DELETE)
print(f'### REMOVE (DELETE)')
try:
    reply = requests.delete('http://localhost:3000/cars/' + str(new_car['id']))
except requests.RequestException:
    print('Communication error')
else:
    if reply.status_code == requests.codes.ok:
        print(f'Response status code: ' + str(reply.status_code))
    elif reply.status_code == requests.codes.not_found:
        print("Resource not found")
    else:
        print(f'Server error {reply.status_code}')

# UPDATE ALL (PUT)
print(f'### UPDATE ALL (PUT)')
car = {
    'id': 3,
    'brand': 'Aston Martin ' + random.choice(string.ascii_letters),
    'model': '300SL ' + random.choice(string.ascii_letters),
    'production_year': random.randint(0,2020),
    'convertible': True
}

try:
    reply = requests.put(
        'http://localhost:3000/cars/3',
        headers={'Connection': 'Close', 'Content-Type': 'application/json'},
        json=car
    )
except requests.RequestException:
    print('Communication error')
else:
    print('Connection=' + reply.headers['Connection'])
    if reply.status_code == requests.codes.ok:
        print(f'Response content: ' + str(reply.json()))
    elif reply.status_code == requests.codes.not_found:
        print("Resource not found")
    else:
        print('Server error')
