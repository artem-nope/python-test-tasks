import sqlite3
import datetime

DB = 'db2.sqlite3'
script = '''
    DROP TABLE IF EXISTS languages;

    CREATE TABLE IF NOT EXISTS languages
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        year INTEGER,
        rating REAL,
        created TEXT
    );
'''
query_insert = '''
    INSERT INTO languages (name, year, rating, created)
    VALUES
    (?, ?, ?, ?);
'''
rows = [
    ('python', 1991, 8.1, str(datetime.datetime.now())),
    ('c++', 1984, 7.5, str(datetime.datetime.now())),
    ('js', 1994, 7.9, str(datetime.datetime.now())),
    ('java', 1994, 7.7, str(datetime.datetime.now()))
]

with sqlite3.connect(DB) as connection:
    cursor = connection.cursor()
    cursor.executescript(script)
    # 1
    # for row in rows:
    #     cursor.execute(query_insert, row)
    # 2
    cursor.executemany(query_insert, rows)