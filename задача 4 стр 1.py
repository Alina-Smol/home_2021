a = list(map(int, input('введите числа: ').split()))
sum1 = 0
sum2 = 0
a.sort()
a1 = []
a2 = []
for i in reversed(a) :
    if sum1 * 2 > sum2:
        a2.append(i)
        sum2 = sum2 + i
    else: 
         a1.append(i)
         sum1 = sum1 + i

if sum1/sum2 <= 2:
    print('Можно разбить на две кучи.')
    print('Первая куча: ', a1)
    print('Вторая куча: ', a2)
    print('Отношение: ', sum1/sum2)
else:
    print('Нельзя разбить на две кучи.')
    print('Первая куча: ', a1)
    print('Вторая куча: ', a2)
    print('Отношение: ', sum1/sum2)

