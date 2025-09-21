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


def remove_book(id):
    cursor.execute('DELETE FROM books WHERE id = ?', [id])
    connection.commit()


def get_all_authors():
    books = cursor.execute('SELECT * FROM books')

    authors = []
    for row in books:
        author = row[2]
        if author in authors:
            continue
        authors.append(author)

    return authors


def get_all_books_by_author(author):
    return cursor.execute('SELECT * FROM books WHERE author = ?', [author])
