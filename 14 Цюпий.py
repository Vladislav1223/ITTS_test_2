#14 Серебренніков
a=[56, 76, 56, 87,65]
for i in a:
    if 100>i>0:
        print('ERROR')
while len(a)>0:
    for i in a:
        if i==min(a):
            b=min(a)
            print(b)
            a.remove(b)
    
