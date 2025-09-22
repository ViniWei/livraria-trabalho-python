import sqlite3
import os
import datetime

backup_folder = 'backups'

os.makedirs('data', exist_ok=True)
os.makedirs(backup_folder, exist_ok=True)

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
    backup()


def return_all_books():
    return cursor.execute('SELECT * FROM books')


def update_book_price(id, price):
    cursor.execute('UPDATE books SET price = ? WHERE id = ?', [price, id])
    connection.commit()
    backup()


def remove_book(id):
    cursor.execute('DELETE FROM books WHERE id = ?', [id])
    connection.commit()
    backup()


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


def backup():
    backup_file_name = f'backup_{datetime.datetime.now()}.db'
    backup_file_name = backup_file_name.replace(' ', '_')

    backup_connection = sqlite3.connect(f'{backup_folder}/{backup_file_name}')
    with backup_connection:
        connection.backup(backup_connection)

    clear_old_backups()


def clear_old_backups():
    max_number_of_backups = 5
    files = os.listdir(backup_folder)

    if len(files) <= max_number_of_backups:
        return

    files.sort(key=lambda x: os.path.getmtime(f'{backup_folder}/{x}'))

    files_to_delete = files[:-max_number_of_backups]
    for file in files_to_delete:
        os.remove(f'{backup_folder}/{file}')
