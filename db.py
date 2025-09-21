import sqlite3
import os

os.makedirs('data', exist_ok=True)

connection = sqlite3.connect('data/livraria.db')
cursor = connection.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS books(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(150),
    author VARCHAR(150),
    publication_year INT,
    price NUMERIC)
''')


def create_book(title, author, publication_year, price):
    data = [title, author, publication_year, price]
    cursor.execute('''INSERT INTO books
                   (title, author, publication_year, price)
                   VALUES(?, ?, ?, ?)''', data)

    connection.commit()


def return_all_books():
    return cursor.execute('SELECT * FROM books')


def update_book_price(id, price):
    cursor.execute('UPDATE books SET price = ? WHERE id = ?', [price, id])
    connection.commit()
