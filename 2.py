a=[56, 44, 65, 56]#2  Серебренников
for i in a:
    if 100>i>0:
        print('ERROR')
b=list(map(lambda x: x**2, a))
for i in a:
    c=b[0]+b[1]
    print(c/2)
    a=a[2:]
