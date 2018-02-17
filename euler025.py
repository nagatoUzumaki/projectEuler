import math
t = int(input())
lst = []
for _ in range(t):
    lst.append(int(input()))
for n in lst:
    if n == 1:
        print(1)
    else:
        num = math.ceil((math.log(10) * (n - 1) + math.log(5) / 2) / math.log(1.61803398875))
        print(num)