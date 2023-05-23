ERROR = 'invalid input. try again'


def number_validation_input():
    while True:
        try:
            return int(input('enter n: '))
        except ValueError:
            print(ERROR)
