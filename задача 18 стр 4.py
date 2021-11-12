#from random import randint
n = input('n: ')
m = input('m: ')
#a = [[randint(1, 10) for j in range(int(m))] for i in range(int(n))]
a = []
for i in range(0, int(n)):
    a.append([int(j) for j in input().split()])

print(a)
k = True
k1 = True
for i in range(0, int(n)):
    for j in range(0,(int(m) - 1)):
        if a[i][j] > a[i][j + 1]:
            k = True
        else:
            k = False
            print('no')
            exit()

for i in range(0, (int(n) - 1)):
    for j in range(0, int(m)):
        if a[i][j] > a[i + 1][j]:
            k1 = True
        else:
            k1 = False
            print('no')
            exit()
if k == True and k1 == True:
    print('yes')
