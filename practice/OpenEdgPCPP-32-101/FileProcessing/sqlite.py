import sqlite3

# SQL: Structured Query Language
# SQLite features.
# Transactional, Zero-configuration, Full-featured SQL implementation, Simple, Fast, Self-contained, Cross-platform.

## sqlite3.connect(): connect to the database.
# File (absolute or relative path).
conn = sqlite3.connect('hello.db')
# Memory.
connMemory = sqlite3.connect(':memory:')
# Get cursor.
c = conn.cursor()


## Manage tables.
# DELETE TABLE.
c.execute('''DROP TABLE IF EXISTS tasks''')
c.execute('''DROP TABLE IF EXISTS authors''')

# Create table (IF NOT EXISTS possible).
c.execute('''CREATE TABLE authors (
author_id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL
)''')
c.execute('''CREATE TABLE tasks (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
priority INT NOT NULL,
author_id INTEGER NOT NULL,
FOREIGN KEY(author_id) REFERENCES authors(author_id) 
);''')

## Insert data.
# cursor.execute(): execute a statement.
c.execute(
    'INSERT INTO authors (name) VALUES (:name)',
    {'name': 'Bod Denard'},  # Tuple not working when only one parameter (in fact yes: (1,))
)
c.execute(
    'INSERT INTO tasks (name, priority, author_id) VALUES (?,?,?)',
    ('Envahir les Commores', 1, 1),
)
# connexion.commit(): commit changes.
conn.commit()

# Insert multiple data.
tasks = [
    ('Envahir le Bénin', 1, 1),
    ('Envahir le Katanga', 5, 1),
    ('Envahir les Commores, encore.', 10, 1),
]

# cursor.executemany(): execute a statement, many times (parameters in an array of tuple).
c.executemany(
    'INSERT INTO tasks (name, priority, author_id) VALUES (?,?,?)',
    tasks
)
conn.commit()

## Select data.
# cursor.fetchall(): get all results.
c.execute('SELECT * FROM tasks')
rows = c.fetchall()

for row in rows:
    print(row)

# cursor.fecthone() (None if no data).
c.execute('SELECT * FROM tasks')
row = c.fetchone()
print(row)

## Update data.
c.execute(
    'UPDATE tasks SET priority = ? WHERE id = ?',
    (20, 1)
)
conn.commit()

## Delete data.
c.execute('DELETE FROM tasks WHERE id = ?', (1,))
conn.commit()

# connexion.close(): close connection.
conn.close()