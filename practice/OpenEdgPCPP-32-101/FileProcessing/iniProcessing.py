import configparser

## Parsing.
config = configparser.ConfigParser()

# Parse from a python dictionary: config.read_dict().
dict = {
    'DEFAULT': {
        'host': 'localhost'
    },
    'mariadb': {
        'name': 'hello',
        'user': 'root',
        'password': 'password'
    },
    'redis': {
        'port': 6379,
        'db': 0
    }
}
config.read_dict(dict)

# Parse from a file: config.read().
config.read('config.ini')

print(config.sections())  # List of sections, except DEFAULT.
print(config['mariadb']['host'])  # host is in DEFAULT section, so will be displayed (comment displayed???).
print(config['mariadb']['name'])
print(config['redis']['host'])  # Overriding default section host value.
# config.get(<section>, <option>)
print(config.get('redis', 'dsn'))  # Interpolation: %(<option>)s replaced with option value.
try:
    # Option does not exist.
    print(config.get('redis', 'portqsd'))
except configparser.NoOptionError:
    pass


## Writing.
# From a list of dictionaries, in config object.
config = configparser.ConfigParser()

config['DEFAULT'] = {'host': 'localhost'}
config['mariadb'] = {
    'name': 'hello',
    'user': 'root',
    'password': 'password',
}
config['redis'] = {
    'port': 6379,
    'db': 0,
    'dsn': ' %(host)s'  # Interpolating values (%(<option>)s): Parser will replace with option value.
}

with open('configNew.ini', 'w') as configfile:
    config.write(configfile)


# From a dictionary.
config = configparser.ConfigParser()

dict = {
    'DEFAULT': {'host': 'localhost'},
    'postgresql': {'name': 'hello', 'user': 'root123', 'password': 'pass123'},
    'redis': {'port': 6379, 'db': 0},
}

# Read the dictionary.
config.read_dict(dict)

with open('configNew.ini', 'w') as configfile:
    config.write(configfile)
