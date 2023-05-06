import calendar
import random
import utils


def site_users_greeting(users):
    if len(users) == 0:
        print('We need to find some users')
    else:
        for user in users:
            print('Hello, Admin, I hope you`re doing well' if user == 'Admin'
                  else f'Hello, {user}, thank you for logging in again')


def figure_name(sides):
    figures = ['triangle', 'rectangle', 'pentagon', 'hexagon']
    print(
        'the number of sides is less than 3 or more than 6' if sides < 3 or sides > 6
        else f'it`s {figures[sides - 3]}')


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
    print('leap year' if year % 400 == 0 else 'ordinary year')


def numbers_sum():
    numbers = []
    n = 1
    while n:
        n = utils.number_validation_input()
        numbers.append(n)
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
    persons = {1: 'Volodymyr Velykiy', 2: 'Yaroslav Mydriy', 5: 'Bohdan Hmelnitsky',
               10: 'Ivan Mazepa', 20: 'Ivan Franko', 50: 'Myhaylo Hrushevsky',
               100: 'Taras Shevchenko', 200: 'Lesya Ukrainka', 500: 'Grigory Skovoroda',
               1000: 'Volodymyr Vernadsky'}
    try:
        print(f'{nominal} - {persons[nominal]}')
    except KeyError:
        print('nominal doesn`t exist')


def cell_color():
    cell = input('input cell in format a1: ')
    if len(cell) == 2 or cell[0] in 'abcdefgh' or cell[1] in '12345678':
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
    if player_move == computer_move:
        return 'draw!'
    if player_move == 'rock' and computer_move == 'scissors':
        return 'you win!'
    if player_move == 'scissors' and computer_move == 'paper':
        return 'you win!'
    if player_move == 'paper' and computer_move == 'rock':
        return 'you win!'
    return 'you lose!'


def rock_paper_scissors():
    options = ['rock', 'paper', 'scissors']
    while True:
        player_move = input('input your move(rock, paper, scissors): ').lower()
        if player_move not in options:
            print('wrong move')
            continue
        computer_move = random.choice(options)
        print(f'you choose {player_move}, computer choose {computer_move}...'
              f'\n{check_win(player_move, computer_move)}')
        if input('want to play again?(y/n): ').lower() == 'n':
            break


if __name__ == '__main__':
    site_users_greeting(['Admin', 'Alex', 'Steve'])
    figure_name(6)
    ordinals(list(range(1, 10)))
    odd_even()
    number_of_days()
    ordinary_leap_year(2100)
    numbers_sum()
    calculator()
    person_on_money(3)
    cell_color()
    decimal_to_binary(155)
    rock_paper_scissors()
