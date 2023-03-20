# Multiparadigm programming languages, Task 2
# Rosyk Nikita, №15


def row_sum(e):
    series_sum = 0
    n = 1
    a = 1
    try:
        while abs(a) >= e:
            a = n / (n-1) ** 2
            series_sum += a
            n += 1
    except ZeroDivisionError:
        a = 'infinity. series diverges'
    return a


def numbers_amount(num):
    i = 0
    while num > 0:
        i += 1
        num //= 10
    return i


def geron_sqrt(num, e):
    x = 1
    while True:
        x_n = (x + num / x) / 2
        if abs(x - x_n) < e * x_n:
            break
        x = x_n
    return x


if __name__ == '__main__':
    print('Multiparadigm programming languages, Task 2')
    print('Nikita Rosyk gr. IKM-221k, №15')

    eps = 0.0001
    print(f'row sum = {row_sum(eps)}')
    print(f'amount of numbers is {numbers_amount(123456789)}')
    print(f'square root is {geron_sqrt(25, eps):.4f}')
