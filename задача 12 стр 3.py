a = list(map(float, input('введите числа а(x1,y1): ').split()))
b = list(map(float, input('введите числа b(x2,y2): ').split()))
if (a[0]*b[1] - a[1]*b[0]) < 0:
   print('OA больше угол, чем OB')
if (a[0]*b[1] - a[1]*b[0]) > 0:
   print('OA меньше угол, чем OB')
if (a[0]*b[1] - a[1]*b[0]) == 0:
   print('углы равны')
