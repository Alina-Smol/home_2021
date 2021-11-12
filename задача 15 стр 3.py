x = list(map(int, input('введите числа x(x1,x2): ').split()))
y = list(map(int, input('введите числа y(y1,y2): ').split()))
z = list(map(int, input('введите числа z(z1,z2): ').split()))
xy = ((y[0] - x[0])**2+(y[1] - x[1])**2)**0.5 #A
yz = ((z[0] - y[0])**2+(z[1] - y[1])**2)**0.5 #B
zx = ((x[0] - z[0])**2+(x[1] - z[1])**2)**0.5 #C

if yz**2 <= xy**2 + zx**2 and zx**2 <= xy**2 + yz**2:
    print('перпендикуляр попадает на отрезке XY')
else:
    print('попадает на продолжениу отрезка')
