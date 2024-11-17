import sqlite3

connection = sqlite3.connect('initiate.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Products(
id INT,
title TEXT NOT NULL,
description TEXT,
price INT NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INT PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INT NOT NULL,
balance INT NOT NULL
);

''')
#for i in range(1, 5):
#    cursor.execute('INSERT INTO Products (id, title, description, price) VALUES(?, ?,?,?)',
#                   (f'{i}', f'Продукт{i}', f'Описание {i}', f'{i * 100}'))


def add_user(username, email, age, balance=1000):
    cursor.execute('INSERT INTO Users  (username,email,age,balance) VALUES(?,?,?,?)', (username, email, age, balance))

    connection.commit()


def is_included(username):
    is_incl = bool(cursor.execute(f'SELECT username FROM Users WHERE username=?', (username,)).fetchone())
    connection.commit()
    return is_incl


def get_all_products():
    products = []
    cursor.execute('SELECT * FROM Products ')
    data = cursor.fetchall()
    for row in data:
        return data


connection.commit()
