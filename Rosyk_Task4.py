from utils import number_validation_input

# Multiparadigm programming languages, Task 2
# Rosyk Nikita, №15


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


print('Multiparadigm programming languages, Task 2')
print('Nikita Rosyk gr. IKM-221k, №15')

n = number_validation_input()
for p in range(2, n - 5):
    if is_prime(p) and is_prime(p + 6):
        print(f'({p}, {p + 6})')
