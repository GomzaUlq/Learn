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
#for i in range(1, 5):
#    cursor.execute('INSERT INTO Products (id, title, description, price) VALUES(?, ?,?,?)',
#                   (f'{i}', f'Продукт{i}', f'Описание {i}', f'{i * 100}'))


def get_all_products():
    products = []
    cursor.execute('SELECT * FROM Products ')
    data = cursor.fetchall()
    for row in data:
        return data


connection.commit()

