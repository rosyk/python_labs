# Multiparadigm programming languages, Task 2
# Rosyk Nikita, №15

print('Multiparadigm programming languages, Task 2')
print('Nikita Rosyk gr. IKM-221k, №15')

while True:
    try:
        x, y, z = [float(x) for x in input("Enter three values, devided by ',': ").split(',')]
        result = (x / (z - 11.3)) + (y / (z + 11.3))
        break
    except ZeroDivisionError:
        print('You try divide by zero. Enter another numbers')
    except:
        print('Something is wrong! Try again')

print(result)
