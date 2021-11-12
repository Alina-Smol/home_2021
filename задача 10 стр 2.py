n = input("Введите n:")
res = int(n, 2) % 15
if res == 0:
    print("делится без остатка")
else:
    print("не делится")
