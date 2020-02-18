m=int(input('Введіть число: '))
if 0 < m <= 20:
    if m % 2 !=0:
        p=l
        for i in range(1,m+2):
            p *= i
            print(p)
    else:
        p = 1
        for i in range(2,m+2):
            p *= i
            print(p)
            
