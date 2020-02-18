 #15  Серебренніков
a=[56, 76, 56, 87,65]
for i in a:
    if 100>i>0:
        print('ERROR')
b=list(filter(lambda x: x%2==0, a))
for i in a:
    if i in b:
        print(i)
for i in a:
    if i not in b:
        print(i)
