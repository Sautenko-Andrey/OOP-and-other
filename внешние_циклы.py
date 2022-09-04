a=[]
stroka_stolb=int(input())

for i in range(stroka_stolb):
    a.append([0]*stroka_stolb)

for i in range(stroka_stolb):
    for j in range(stroka_stolb):
        if i==j:
            a[i][j]=10
        elif i>j:
            a[i][j]=3
        else:
            a[i][j]=5
for i in a:
    print(i)


