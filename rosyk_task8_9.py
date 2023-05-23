import calendar
import random
import utils


FIGURES = ['triangle', 'rectangle', 'pentagon', 'hexagon']
PERSONS = {1: 'Volodymyr Velykiy', 2: 'Yaroslav Mydriy', 5: 'Bohdan Hmelnitsky',
           10: 'Ivan Mazepa', 20: 'Ivan Franko', 50: 'Myhaylo Hrushevsky',
           100: 'Taras Shevchenko', 200: 'Lesya Ukrainka', 500: 'Grigory Skovoroda',
           1000: 'Volodymyr Vernadsky'}
COMBINATIONS = {('rock', 'rock'): 'draw',
                ('paper', 'paper'): 'draw',
                ('scissors', 'scissors'): 'draw',
                ('rock', 'scissors'): 'you win',
                ('rock', 'paper'): 'you lose',
                ('paper', 'rock'): 'you win',
                ('paper', 'scissors'): 'you lose',
                ('scissors', 'rock'): 'you lose',
                ('scissors', 'paper'): 'you win'}


def site_users_greeting(users):
    if len(users) == 0:
        print('We need to find some users')
    else:
        for user in users:
            print('Hello, Admin, I hope you`re doing well' if user == 'Admin'
                  else f'Hello, {user}, thank you for logging in again')


def figure_name(sides):
    print(
        f'it`s {FIGURES[sides - 3]}' if 2 < sides < 7
        else 'the number of sides is less than 3 or more than 6')


def ordinals(numbers):
    for number in numbers:
        if number == 1:
            print(f'{number}st')
        elif number == 2:
            print(f'{number}nd')
        elif number == 3:
            print(f'{number}rd')
        else:
            print(f'{number}th')


def odd_even():
    number = utils.number_validation_input()
    print(f'{number} is even' if number % 2 == 0 else f'{number} is odd')


def number_of_days():
    month = input('input month: ').lower().title()
    try:
        month_num = list(calendar.month_name).index(month)
        print(f'in {month} {calendar.monthrange(2023, month_num)[1]} days')
    except ValueError:
        print('month doesn`t exist')


def ordinary_leap_year(year):
    print('leap year' if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)) else 'ordinary year')


def numbers_sum():
    numbers = list(iter(lambda: utils.number_validation_input(), 0))
    print(sum(numbers))


def calculator():
    first_number = utils.number_validation_input()
    operation = input('input operation(+, -, *, /, mod, pow, div)')
    second_number = utils.number_validation_input()
    try:
        if operation == '+':
            print(first_number + second_number)
        elif operation == '-':
            print(first_number - second_number)
        elif operation == '/':
            print(first_number / second_number)
        elif operation == '*':
            print(first_number * second_number)
        elif operation == 'mod':
            print(first_number % second_number)
        elif operation == 'pow':
            print(first_number ** second_number)
        elif operation == 'div':
            print(first_number // second_number)
        else:
            print('incorrect operation')
    except ZeroDivisionError:
        print('division by zero')


def person_on_money(nominal):
    print(f'{nominal} - {PERSONS.get(nominal, "nominal doesn`t exist")}')


def cell_color():
    cell = input('input cell in format a1: ')
    if len(cell) == 2 and cell[0] in 'abcdefgh' and cell[1] in '12345678':
        print('cell is black' if (ord(cell[0])) % 2 == int(cell[1]) % 2 else 'cell is white')
    else:
        print("incorrect cell")


def decimal_to_binary(number):
    result = ''
    n = number
    while n != 0:
        result = str(n % 2) + result
        n //= 2
    print(f'{number} is {result}')

    n = 0
    for i in range(len(result)):
        if result[len(result) - 1 - i] == '1':
            n += 2 ** i
    print(f'{result} is {n}')


def check_win(player_move, computer_move):
    return COMBINATIONS.get((player_move, computer_move), None)


def input_player_move(options):
    while True:
        move = input('input your move(rock, paper, scissors): ').lower()
        if move not in options:
            print(f'{move} doesn`t look like rock, paper or scissors')
            continue
        return move


def is_play_again():
    while True:
        play_again = input('want to play again?(y/n): ').lower()
        if play_again not in 'yn':
            print('write only y or n')
            continue
        return play_again == 'y'


def rock_paper_scissors():
    options = ['rock', 'paper', 'scissors']
    while True:
        computer_move = random.choice(options)
        player_move = input_player_move(options)
        print(f'you choose {player_move}, computer choose {computer_move}...'
              f'\n{check_win(player_move, computer_move)}')
        if is_play_again():
            continue
        break


if __name__ == '__main__':
    # site_users_greeting(['Admin', 'Alex', 'Steve'])
    figure_name(7)
    # ordinals(list(range(1, 10)))
    # odd_even()
    # number_of_days()
    # ordinary_leap_year(2100)
    # numbers_sum()
    # calculator()
    # person_on_money(3)
    # cell_color()
    # decimal_to_binary(155)
    # rock_paper_scissors()
