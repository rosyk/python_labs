# Multiparadigm programming languages, Task 2
# Rosyk Nikita, №15


def row_sum(eps):
    series_sum = 0
    n = 1
    row_number = 1
    try:
        while abs(row_number) >= eps:
            row_number = n / (n - 1) ** 2
            series_sum += row_number
            n += 1
    except ZeroDivisionError:
        series_sum = 'infinity. series diverges'
    return series_sum


def numbers_amount(num):
    char_count = 0
    while num > 0:
        char_count += 1
        num //= 10
    return char_count


def geron_sqrt(num, eps):
    x = 1
    while True:
        x_n = (x + num / x) / 2
        if abs(x - x_n) < eps * x_n:
            break
        x = x_n
    return x


if __name__ == '__main__':
    print('Multiparadigm programming languages, Task 2')
    print('Nikita Rosyk gr. IKM-221k, №15')

    EPSILON = 0.0001
    print(f'row sum = {row_sum(EPSILON)}')
    print(f'amount of numbers is {numbers_amount(123456789)}')
    print(f'square root is {geron_sqrt(25, EPSILON):.4f}')
