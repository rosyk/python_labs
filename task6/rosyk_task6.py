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
        file.write(f'{number} is even') if number % 2 == 0 else file.write(f'{number} is odd')


def python_posibilities_print():
    with open('learning_python.txt', encoding='utf8') as file:
        text = file.readlines()
    list(map(print, text))


def python_change():
    with open('learning_python.txt', encoding='utf8') as file:
        for line in file:
            print(line.replace('Python', 'C'))


def guests_greeting():
    while True:
        name = input('Enter guest name, enter "exit" if list is done: ')
        if name == 'exit':
            break
        greeting = f'Welcome, {name}. Have a nice day!'
        with open('guest_book.txt', 'w', encoding='utf8') as file:
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
        lines = [line for line in book if 'CHAPTER' in line]
        chapters.writelines(lines)


def small_big_letters():
    with open('book.txt', encoding='utf8') as file:
        alpha_text = [char for char in file.read() if char.isalpha()]
        upper_perc = sum(i.islower() for i in alpha_text) / len(alpha_text) * 100
        print(f'small letters: {upper_perc}%, big letters: {100 - upper_perc}%')


def imdb_rating():
    conn = sql.connect('imdb.db')
    curs = conn.cursor()
    curs.execute('CREATE TABLE ratings (id INTEGER PRIMARY KEY, '
                 'title VARCHAR(20), '
                 'year INT, '
                 'rating FLOAT)')
    curs.execute('INSERT INTO ratings VALUES(0, "The last of us", 2023, 9.0)')
    curs.execute('INSERT INTO ratings VALUES(1, "Everything Everywhere All at Once", 2022, 7.9)')
    curs.execute('INSERT INTO ratings VALUES(2, "Avatar: way of water", 2023, 7.8)')
    curs.execute('INSERT INTO ratings VALUES(3, "The Whale", 2023, 7.8)')
    conn.commit()
    curs.execute('SELECT * FROM ratings ORDER BY title')
    for row in curs:
        print(row)
    curs.execute('SELECT * FROM ratings WHERE rating > 8.7')
    for row in curs:
        print(row)
    curs.close()
    conn.close()


if __name__ == '__main__':
    numbers_sum()
    odd_even_write()
    python_posibilities_print()
    python_change()
    guests_greeting()
    the_counter()
    text_format()
    chapters_write()
    small_big_letters()
    imdb_rating()
