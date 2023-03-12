from math import tan, sqrt, pow, cos

# Multiparadigm programming languages, Task 2
# Rosyk Nikita, №15

print('Multiparadigm programming languages, Task 2')
print('Nikita Rosyk gr. IKM-221k, №15')

while True:
    try:
        x, b = [float(x) for x in input("Enter two values, divided by ',': ").split(',')]
        if x < b or b == 0 or cos(x) == 0:
            print('Function value is not defined for the entered values')
        else:
            result = (sqrt(x - b) / 2 * b) - (tan(x) / pow(b, 2))
            break
    except:
        print('Something is wrong! Try again')

print(result)
