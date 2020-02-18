from random import randint

k = 0
n = int(input('n = '))
r = [randint(1, 10) for i in range(n)]
print(r)
for m in range(1, n):
    if r[m] < r[m - 1]:
        print(m)
        k += 1
print('Всього таких чисел = ', k)
