import sqlite3 as sql
from utils import number_validation_input


def numbers_sum():
    result = 0
    with open('numbers.txt', encoding='utf8') as file, \
            open('sum_numbers.txt', 'w', encoding='utf8') as output:
        for line in file:
            try:
                result += float(line)
            except ValueError:
                print('file contains something except numbers')
                return
        output.write(str(result))
    print(result)


def odd_even_write():
    with open('even_or_odd.txt', 'w', encoding='utf8') as file:
        number = number_validation_input()
        file.write(f'{number} is even' if number % 2 == 0 else f'{number} is odd')


def python_posibilities_print():
    with open('learning_python.txt', encoding='utf8') as file:
        text = file.readlines()
    list(map(print, text))


def python_change():
    with open('learning_python.txt', encoding='utf8') as file:
        for line in file:
            print(line.replace('Python', 'C'))


def guests_greeting():
    with open('guest_book.txt', 'w', encoding='utf8') as file:
        while True:
            name = input('Enter guest name, enter "exit" if list is done: ')
            if name == 'exit':
                break
            greeting = f'Welcome, {name}. Have a nice day!'
            file.write(greeting)
            print(greeting)


def the_counter():
    with open('book.txt', encoding='utf8') as book:
        print(book.read().lower().count('the'))


def text_format():
    with open('book.txt', encoding='utf8') as book, \
            open('formatted_text.txt', 'w', encoding='utf8') as formatted_text:
        formatted_text.write(book.read().replace('\n', ' '))


def chapters_write():
    with open('robinson_crusoe.txt', encoding='utf8') as book, \
            open('chapters.txt', 'w', encoding='utf8') as chapters:
        chapters.writelines([line for line in book if 'CHAPTER' in line])


def small_big_letters():
    with open('book.txt', encoding='utf8') as file:
        alpha_text = [char for char in file.read() if char.isalpha()]
        upper_perc = sum(i.islower() for i in alpha_text) / len(alpha_text) * 100
        print(f'small letters: {upper_perc}%, big letters: {100 - upper_perc}%')


def create_table(curs):
    curs.execute('CREATE TABLE IF NOT EXISTS ratings (id INTEGER PRIMARY KEY, '
                 'title VARCHAR(20), '
                 'year INT, '
                 'rating FLOAT)')


def insert_ratings(curs):
    ratings = [
        (0, "The last of us", 2023, 9.0),
        (1, "Everything Everywhere All at Once", 2022, 7.9),
        (2, "Avatar: way of water", 2023, 7.8),
        (3, "The Whale", 2023, 7.8)
    ]
    curs.executemany('INSERT INTO ratings VALUES(?, ?, ?, ?)', ratings)


def select_all_rows(curs):
    curs.execute('SELECT * FROM ratings ORDER BY title')
    for row in curs.fetchall():
        print(row)


def select_high_ratings(curs):
    curs.execute('SELECT * FROM ratings WHERE rating > 8.7')
    for row in curs.fetchall():
        print(row)


def imdb_rating():
    with sql.connect('imdb.db') as conn:
        curs = conn.cursor()
        create_table(curs)
        insert_ratings(curs)
        conn.commit()
        select_all_rows(curs)
        select_high_ratings(curs)


# def imdb_rating():
#     conn = sql.connect('imdb.db')
#     curs = conn.cursor()
#     curs.execute('CREATE TABLE IF NOT EXISTS ratings (id INTEGER PRIMARY KEY, '
#                  'title VARCHAR(20), '
#                  'year INT, '
#                  'rating FLOAT)')
#     curs.execute('INSERT INTO ratings VALUES(0, "The last of us", 2023, 9.0)')
#     curs.execute('INSERT INTO ratings VALUES(1, "Everything Everywhere All at Once", 2022, 7.9)')
#     curs.execute('INSERT INTO ratings VALUES(2, "Avatar: way of water", 2023, 7.8)')
#     curs.execute('INSERT INTO ratings VALUES(3, "The Whale", 2023, 7.8)')
#     conn.commit()
#     curs.execute('SELECT * FROM ratings ORDER BY title')
#     for row in curs:
#         print(row)
#     curs.execute('SELECT * FROM ratings WHERE rating > 8.7')
#     for row in curs:
#         print(row)
#     curs.close()
#     conn.close()


if __name__ == '__main__':
    # numbers_sum()
    # odd_even_write()
    # python_posibilities_print()
    # python_change()
    # guests_greeting()
    # the_counter()
    # text_format()
    # chapters_write()
    # small_big_letters()
    imdb_rating()
