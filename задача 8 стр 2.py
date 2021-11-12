from itertools import combinations
a = []
n = int(input('n: '))
for i in range(n):
    a.append(i)
for i in range(len(a)+1):
    print([j for j in combinations(a,i)])
