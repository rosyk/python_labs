def number_validation_input():
    while True:
        try:
            return int(input('enter n: '))
        except ValueError:
            print('invalid input. try again')
