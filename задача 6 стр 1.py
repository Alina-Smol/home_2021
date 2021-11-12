n = int(input('n: '))
a = []
for i in range(0, n):
    a.append(int(input()))
for i in range(n):
    if a[i] < n:
        print('Человека ',i + 1, 'можно познакомить с ', a[i])
    else:
         print('Человека ',i + 1, 'нельзя познакомить с ', a[i])
