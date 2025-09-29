import csv
import os

folder_name = 'exports'
os.makedirs(folder_name, exist_ok=True)


def export(data):
    file_path = f'{folder_name}/livros_exportados.csv'
    with open(file_path, mode='w') as file:
        writer = csv.writer(file)
        writer.writerow(['id', 'nome', 'autor', 'ano', 'preço'])
        writer.writerows(data)


def importt():
    pass
