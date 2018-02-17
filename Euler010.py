import math
t = int(input())
lst = []
for _ in range (t):
    lst.append(int(input()))
limit = max(lst) + 1
sum = [0] * limit
a = [True] * limit
a[0] = a[1] = False
for i, isprime in enumerate(a):
    if isprime:
        sum[i] = sum[i-1] + i
        for n in range(i*i, limit, i):
            a[n] = False
    else:
        sum[i] = sum[i-1]

for n in lst:
    print(sum[n])