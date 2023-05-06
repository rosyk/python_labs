# Multiparadigm programming languages, Task 2
# Rosyk Nikita, №15
from itertools import takewhile, count


def row_sum(eps):
    row = (n / (n - 1) ** 2 for n in count())
    return sum(list(takewhile(lambda x: x >= eps, row)))


def numbers_amount(num):
    if num == 0:
        return 1
    num = abs(num)
    char_count = 0
    while num:
        char_count += 1
        num //= 10
    return char_count


def geron_sqrt(num, eps):
    if num < 0:
        raise ValueError
    if num == 0:
        return 0
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
    print(f'square root is {geron_sqrt(0, EPSILON):.4f}')
