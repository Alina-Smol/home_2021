from itertools import combinations
a = []
n = input('n: ')
k = input('k: ')
for i in range(0, int(n)):
    a.append(i + 1)
print(list(combinations(a,int(k))))
