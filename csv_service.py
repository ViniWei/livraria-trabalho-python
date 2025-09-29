import csv
import os
import db

folder_name = 'exports'
os.makedirs(folder_name, exist_ok=True)


def export(data):
    file_path = f'{folder_name}/livros_exportados.csv'
    with open(file_path, mode='w') as file:
        writer = csv.writer(file)
        writer.writerow(['id', 'name', 'author', 'year', 'price'])
        writer.writerows(data)


def importt(file_path):
    with open(file_path) as file:
        data = csv.DictReader(file)
        for row in data:
            print(row)
            db.create_book(
                row['name'],
                row['author'],
                row['year'],
                row['price']
            )
