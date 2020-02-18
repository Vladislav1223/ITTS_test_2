import math

while True:
    try:
        M = int(input('Введіть натуральне число M:'))
        if 0 < M <= 13:
            print(math.factorial(M))
        else:
            print('Число M має бути більше 0 і менше або рівно 13')
            print()
            continue
        break
    except ValueError:
        print('Ви можете ввести лише ціле число.')
        print()
