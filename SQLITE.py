import sqlite3 as sq

with sq.connect('saper.db') as my_connect:
    my_cursor=my_connect.cursor()

    my_cursor.execute('''CREATE TABLE users (
        name TEXT,
        sex INTEGER,
        old INTEGER,
        score INTEGER
        )''')



