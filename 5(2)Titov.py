from random import randint
n = int(input('вв від 0 до 100'))
m = int(input('вв від 0 до 1000'))
n_random = [randint(1,100) for i in range(n)]
n_random = list(n_random)
print(n_random)
Min = min(n_random)
print(Min)
k = 0
summa = 0
l = len(n_random)
while summa < l:
    if Min+m == n_random[summa]:
        k = summa
        summa += 1

    else:
        summa += 1
        continue
print(k)