import db

menu_ui = '''
1. Adicionar novo livro
2. Exibir todos os livros
3. Atualizar preço de um livro
4. Remover um livro
5. Buscar livros por autor
6. Exportar dados para CSV
7. Importar dados de CSV
8. Fazer backup do banco de dados
9. Sair
'''
option = 0


def menu():
    global option
    print(menu_ui)
    option = int(input('-> '))

    match option:
        case 1:
            create_new_book()
        case 2:
            res = db.return_all_books()
            print('=============')
            for row in res:
                print('Id:', row[0])
                print('Titulo:', row[1])
                print('Autor:', row[2])
                print('Ano de publicação:', row[3])
                print('Preço', row[4])
                print('=============')
        case 3:
            print('Teste')
        case 4:
            print('Teste')
        case 5:
            print('Teste')
        case 6:
            print('Teste')
        case 7:
            print('Teste')
        case 8:
            print('Teste')
        case 9:
            print('Saindo')
        case _:
            print('Opção invalida')


def create_new_book():
    title = input('Titulo:')
    author = input('Autor:')
    publication_year = input('Ano de publicação:')
    price = input('Preço:')
    db.create_book(title, author, publication_year, price)


while option != 9:
    menu()
