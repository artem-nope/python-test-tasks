import sqlite3

DB = 'db1.sqlite3'


with sqlite3.connect(DB) as connection:
    cursor = connection.cursor()
    cursor.executescript(open('create1.sql').read())
