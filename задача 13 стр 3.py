a = list(map(float, input('введите числа а(x,y): ').split()))
b = list(map(float, input('введите числа b(x1,y1): ').split()))
c = list(map(float, input('введите числа c(x2,y2): ').split()))
if ((a[0] - b[0])*(c[1] - b[1]) - (a[1] - b[1])*(c[0] - b[0])) == 0 and ((b[0] < a[0] < c[0]) or (c[0] < a[0] < b[0])):
    print('принадлежит отрезку')
else:
    print('не принадлежит отрезку')
