k = int(input("Введите число k: "))
s = 0
f = 1
for i in range(1, k+1):
    f = f * i
    s += 1 / f

print("ОТВЕТ: ", s)
