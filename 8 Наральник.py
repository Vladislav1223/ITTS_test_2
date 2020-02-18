import random #Наральник Богдан
N_a = float(input('Довжина списку а: '))
N_b = float(input('Довжина списку б: '))
if N_a >= 0 and N_a <= 100 and N_b >= 0 and N_b <= 100:    
 a = []
 b = []
 c = []
while N_a != 0:
    a.append(random.randint(1, 1000))
    N_a -= 1
while N_b != 0:
    b.append(random.randint(1, 1000))
    N_b -= 1
for i in a:
    if i not in b:
        c.append(i)
for i in b:
    if i not in a:
        c.append(i)
print('a:', a)
print('b:', b)
print('c:', c)

