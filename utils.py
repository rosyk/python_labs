def number_validation_input():
    while True:
        try:
            n = int(input('enter n: '))
            return n
            break
        except ValueError:
            print('invalid input. try again')