from utils import number_validation_input
import sqlite3 as sql


def numbers_sum():
    result = 0
    with open('numbers.txt') as file, open('sum_numbers.txt', 'w') as output:
        for line in file:
            try:
                result += float(line)
            except ValueError:
                print('file contains something except numbers')
        output.write(str(result))
    print(result)


def odd_even_write():
    with open('even_or_odd.txt', 'w') as file:
        n = number_validation_input()
        file.write(f'{n} is even') if n % 2 == 0 else file.write(f'{n} is odd')


def python_posibilities_print():
    with open('learning_python.txt') as file:
        lines = file.readlines()
    for i in range(len(lines)):
        print(lines[i])


def python_change():
    with open('learning_python.txt') as file:
        for line in file:
            print(line.replace('Python', 'C'))


def guests_greeting():
    while True:
        name = input('Enter guest name, enter "exit" if list is done: ')
        if name == 'exit':
            break
        greeting = f'Welcome, {name}. Have a nice day!'
        with open('guest_book.txt', 'w') as file:
            file.write(greeting)
        print(greeting)


def the_counter():
    counter = 0
    with open('book.txt') as book:
        for line in book:
            counter += line.count('the')
    print(counter)


def text_format():
    with open('book.txt') as book, open('formatted_text.txt', 'w') as ft:
        ft.write(book.read().replace('\n', ' '))


def chapters_write():
    with open('robinson_crusoe.txt', encoding='utf8') as book, open('chapters.txt', 'w', encoding='utf8') as chapters:
        for line in book:
            if 'CHAPTER' in line:
                chapters.write(line)


def small_big_letters():
    with open('book.txt') as file:
        text = file.read()
        alpha_text = []
        for char in text:
            if char.isalpha():
                alpha_text.append(char)
        print(
            f'small letters: {sum(i.islower() for i in alpha_text) / len(alpha_text) * 100}%, big letters: {sum(i.isupper() for i in alpha_text) / len(alpha_text) * 100}%')


def imdb_rating():
    conn = sql.connect('imdb.db')
    curs = conn.cursor()
    curs.execute('CREATE TABLE ratings (id INTEGER PRIMARY KEY, title VARCHAR(20), year INT, rating FLOAT)')
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
